import json

def save_matched_urls_to_json(matched_urls_map, filename="output.json"):
    # Convert defaultdict to regular dict for JSON serialization
    output_data = {domain: sorted(list(set(urls))) for domain, urls in matched_urls_map.items()}
    
    with open(filename, "w") as f:
        json.dump(output_data, f, indent=2)

    print(f"\nSaved matched URLs to {filename}")