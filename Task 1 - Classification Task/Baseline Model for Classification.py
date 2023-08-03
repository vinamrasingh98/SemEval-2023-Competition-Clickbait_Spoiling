import json
import os
import csv
import pandas as pd

def main():    
    def predict(inputs):
        for i in inputs:
            yield {'id': i['id'], 'spoilerType': 'passage'}


    with open(path+"/test.jsonl", 'r') as inp, open(path+"/test1.jsonl", 'w') as out:
        inp = [json.loads(i) for i in inp]
        for output in predict(inp):
            out.write(json.dumps(output) + '\n')

    file = pd.read_json(path+"/test1.jsonl", lines=True)
    file.to_csv(path+"/prediction_task1.csv", index=False)
    
if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data")
    main()
