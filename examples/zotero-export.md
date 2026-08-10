# Example — Search to Zotero Export

This example shows the expected handoff shape, not a claim that the example paper is relevant to a user’s project.

1. During `SI1_LANDSCAPE` or `SI2_BACKBONE`, create a `P-` record for each reviewed result. Store the DOI/arXiv/OpenReview/PMID identifier, exact source URL, `SS-` search session, and whether the metadata is `UNVERIFIED`, `PARTIALLY_VERIFIED`, or `VERIFIED`.
2. Merge duplicate versions using DOI first, then secondary identifiers, then normalized title/author/year. Preserve all provenance and unresolved conflicts.
3. After an authoritative metadata check, set `export_eligible: true` only for a `VERIFIED` record with complete required fields and no unresolved conflict.
4. At S18, generate the project artifact:

   ```text
   <research-project>/exports/references.bib
   ```

5. Import `references.bib` into Zotero with `File → Import → A file`. Use Zotero or a full-text reader to retrieve and annotate papers; use the Research Forge paper/evidence records for claims, reading depth, and provenance.

An excluded record is not deleted. Its `P-` ID and exclusion reason remain in the transaction log so the bibliography can be regenerated after a metadata conflict is resolved.
