from neo4j.graph import Node, Relationship


class FieldsExtractor:
    def extract(self, results):
        for r in results:
            data = {}
            result_dict = dict(r)
            for k, v in result_dict.items():
                if isinstance(v, Node) or isinstance(v, Relationship):
                    data[f"{k}.id"] = v.id
                    # Parse items
                    for inner_k, inner_v in v.items():
                        data[f"{k}.{inner_k}"] = inner_v
                    # Parse labels
                    if isinstance(v, Node) and v.labels:
                        data[f"{k}.labels"] = ",".join(v.labels)
                    if isinstance(v, Relationship) and v.type:
                        data[f"{k}.type"] = v.type
                else:
                    data[k] = v
            data["_raw"] = str(r)
            yield data
