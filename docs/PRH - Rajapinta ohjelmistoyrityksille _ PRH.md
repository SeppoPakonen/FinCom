# PRH: IXBRL Interface for Software Companies

This guide is intended for companies developing financial management software who want to connect their software to PRH's financial statement interface.

## 1. What is the interface?
* **Type:** REST API.
* **Purpose:** Sending IXBRL-formatted financial statements and metadata directly to the Trade Register.
* **Supported formats:** Currently limited to limited liability companies' financial statements and foundations' annual reports.

## 2. Technical Requirements
* **Format:** The financial statement must comply with the IXBRL standard (Inline XBRL embedded in HTML code).
* **Authentication:** Separate authentication service (Access Token).
* **Validation:** The interface checks the correctness of metadata (Business ID, financial year) and the IXBRL file structure.

## 3. Implementation
* Requires an agreement with PRH.
* PRH provides a test server for development work.
* Estimated workload: About 10–15 person-days.
* **Cost:** Using the interface is free of charge.

---
**Additional information:** digitilinpaatos@prh.fi