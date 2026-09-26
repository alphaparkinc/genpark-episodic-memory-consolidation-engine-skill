import json, sys
from client import EpisodicMemoryConsolidationEngineClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "episodic-memory-consolidation-engine", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "consolidate_working_memory", "description": "Consolidates working conversational memory into durable episodic knowledge and prunes noise."}]}}
    elif method == "tools/call":
        client = EpisodicMemoryConsolidationEngineClient()
        res = client.consolidate_working_memory()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = EpisodicMemoryConsolidationEngineClient()
        print(json.dumps(client.consolidate_working_memory(), indent=2))
