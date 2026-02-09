# PRH: IXBRL Interface for Software Companies

This guide is intended for companies developing financial software who want to connect their software to PRH's financial statements interface.

## 1. What is the interface?
* **Type:** REST API.
* **Purpose:** Sending IXBRL format financial statements and metadata directly to the Trade Register.
* **Supported formats:** Currently limited to limited liability companies' financial statements and foundations' annual reports.

## 2. Technical Requirements
* **Format:** The financial statement must be in IXBRL standard format (Inline XBRL embedded in HTML code).
* **Authentication:** Separate authentication service (Access Token).
* **Validation:** The interface checks the validity of metadata (Business ID, financial year) and the structure of the IXBRL file.

## 3. Activation
* Requires an agreement with PRH.
* PRH provides a test server for development work.
* Workload estimate: Approximately 10–15 person-days.
* **Cost:** Using the interface is free of charge.

---
**Additional information:** digitilinpaatos@prh.fi