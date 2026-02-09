#!/usr/bin/env python3
"""
Script to identify English documentation files to process next.
Skips Finnish files and potential duplicates.
"""

import os
import re
from pathlib import Path

def is_likely_english_file(file_path):
    """Check if a file is likely to be in English based on its content."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()[:1000]  # Check first 1000 chars
        
        # Files with Finnish characters are likely Finnish
        finnish_chars = ['ä', 'ö', 'å', 'Ä', 'Ö', 'Å']
        for char in finnish_chars:
            if char in content:
                return False
    except:
        return False  # If we can't read the file, assume it's not English
    
    filename = os.path.basename(file_path).lower()
    
    # Check if filename contains Finnish words
    finnish_words = [
        'tieto', 'yritys', 'yrittäjä', 'liiketoiminta', 'markkinointi', 'myynti', 
        'palvelu', 'asiakas', 'kortti', 'sopimus', 'ilmoitus', 'lupa', 'tarkastus',
        'toiminta', 'suunnitelma', 'kannattavuus', 'verotus', 'talouden', 'suunnittelu',
        'perustaminen', 'muistilista', 'koulutus', 'kalenteri', 'viikkokalenteri', 'vuosikello',
        'kauppa', 'kaupan', 'kauppakirja', 'vuokra', 'vuokrasopimus', 'perustamis',
        'yhtiö', 'yhtiosopimus', 'yhtiöjärjestys', 'osake', 'osakas', 'hallitus', 'kokous',
        'edunsaaja', 'rekisteri', 'viranomainen', 'lainsäädäntö', 'sääntö', 'ohje', 'tutkinto',
        'tehtävä', 'arviointi', 'lomake', 'lomautus', 'irtisanominen', 'työsopimus', 'työ',
        'työntekijä', 'työehtosopimus', 'työpaikka', 'työvoima', 'palkka', 'etuus', 'sairaus',
        'vakuutus', 'turvallisuus', 'hyvinvointi', 'terveys', 'suojelun', 'toimintaohjelma',
        'kustannus', 'budjetti', 'tase', 'tuloslaskelma', 'tilinpäätös', 'tositteet', 'kirjanpito',
        'asiakirja', 'standardi', 'sfs', 'tietosuoja', 'tietoturva', 'salassapito', 'suostumus'
    ]
    
    for word in finnish_words:
        if word in filename:
            return False
    
    # If filename doesn't contain obvious Finnish words and no Finnish chars in content, likely English
    return True

def find_english_files(docs_dir, num_files=50):
    """Find English documentation files to process."""
    all_files = list(Path(docs_dir).rglob("*.md"))
    all_files_sorted = sorted(all_files, key=lambda x: str(x).lower())
    
    english_files = []
    processed_counter = 0
    
    for file_path in all_files_sorted:
        try:
            if is_likely_english_file(str(file_path)):
                # Check if this is a duplicate by looking for similar titles
                filename = file_path.name.lower()
                
                # Skip if it's a known duplicate pattern (like Finnish/English versions of same document)
                is_duplicate = False
                for existing_file in english_files:
                    existing_name = existing_file.name.lower()
                    # Check if files are likely duplicates (e.g., one with "english" and one without, or similar names)
                    if (filename.replace("_english", "").replace("english_", "") == 
                        existing_name.replace("_english", "").replace("english_", "")):
                        is_duplicate = True
                        break
                
                if not is_duplicate:
                    english_files.append(file_path)
                    processed_counter += 1
                    print(f"Selected: {file_path.name}")
                    
                    if processed_counter >= num_files:
                        break
            else:
                print(f"Skipped (Finnish): {file_path.name}")
        except Exception as e:
            print(f"Error processing {file_path.name}: {str(e)}")
            continue
    
    return english_files

if __name__ == "__main__":
    docs_dir = "/common/active/sblo/Dev/FinCom/docs"
    english_files = find_english_files(docs_dir, 50)
    
    print(f"\nFound {len(english_files)} English files to process:")
    for i, file_path in enumerate(english_files, 1):
        print(f"{i:2d}. {file_path.name}")
    
    # Write the list to a file for reference
    with open("/common/active/sblo/Dev/FinCom/plan/next_50_english_files.txt", "w") as f:
        for file_path in english_files:
            f.write(f"{file_path}\n")
    
    print(f"\nList of files saved to: /common/active/sblo/Dev/FinCom/plan/next_50_english_files.txt")