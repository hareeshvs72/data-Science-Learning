import csv

# read csv 
data = "Data.csv"
def read_file(data):
    with open(data,"r") as file:
        reader = csv.DictReader(file)
        return list(reader)
       
result = read_file(data)
# print(result)

#remove duplicates based on email 

def remove_Duplicates(data):
    uniqu = []
    seen = set()
    duplicates = []
    
    for row in data:
        email = row["email"]
        if email in seen:
            duplicates.append(row)
        else:
            uniqu.append(row)
            seen.add(email)
            
    return uniqu , duplicates
    
    
    
result2 = remove_Duplicates(result)
# print("result 2  : ",result2)   


# handile missing values

def missing_Values(data):
    
    for row in data:
        # print(row)
        if row["name"] == "" :
            row["name"] = "unknown" 
    
    return data
result3 = missing_Values(result)
print(result3)


# generate summary 

def summery(total,duplicates,cleaned):
    summary = f"""
     Data Processing Summary
    -----------------------
    Total Rows: {total}
    Duplicate Rows: {duplicates}
    Clean Rows: {cleaned}
    """
    return summary
    
def write_output (summary):
    with open("output.txt", "w") as file:
        file.write(summary)
# Main function (CLI entry)
def main():
    file_path = "data.csv"

    data = read_file(file_path)
    total_rows = len(data)

    unique_data, duplicates =  remove_Duplicates(data)
    cleaned_data = missing_Values(unique_data)

    summary = summery(
        total=total_rows,
        duplicates=len(duplicates),
        cleaned=len(cleaned_data)
    )

    write_output(summary)

    print("✅ Processing Complete. Check output.txt")


if __name__ == "__main__":
    main()