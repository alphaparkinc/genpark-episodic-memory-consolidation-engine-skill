import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import EpisodicMemoryConsolidationEngineClient

def main():
    client = EpisodicMemoryConsolidationEngineClient()
    res = client.consolidate_working_memory()
    print("=== Episodic Memory Consolidation Engine Output ===")
    print(f"Session: {res['session_id']} | Facts Extracted: {res['durable_facts_extracted_count']}/{res['working_memory_turns_ingested']}")
    print(f"Noise Pruned: {res['noise_turns_pruned_count']} turns (Compression: {res['memory_compression_ratio']})")
    print(f"Status: {res['episodic_store_status']} | Action: {res['recommended_action']}")
    print("\nDurable Consolidated Facts:")
    for f in res['consolidated_episodic_facts']:
        print(f"  * [{f['category']}] (Weight: {f['salience_weight']}) {f['extracted_fact']}")

if __name__ == '__main__':
    main()
