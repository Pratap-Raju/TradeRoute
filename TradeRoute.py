# CMPUT 175 - Assignment 1, Global Trade Analysis
# Name: Pratap Kolukuluri
# Student ID: 1849597

def read_file(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines

def format_currency(value, width=15):
    num_str = "{:,.2f}".format(value)
    padding = " " * (width - len(num_str) - 1)
    return "$" + padding + num_str

def format_percent(value, width=8):
    return ("{:.2f}%".format(value)).rjust(width)

def print_border(width):
    print("-" * width)

def print_row(columns, widths):
    row = "|"
    for i in range(len(columns)):
        value = str(columns[i])

        if len(value) > widths[i]:
            value = value[:widths[i] - 3] + "..."

        if "$" in value or value.strip().isdigit():
            row += " " + value.rjust(widths[i]) + " |"
        else:
            row += " " + value.ljust(widths[i]) + " |"
    print(row)


# files into lists
countries = []
tariffs = []
products = []
product_country = []
shopping = []

# Skip headers in data files during load
for line in read_file("country.txt")[1:]:
    p = line.strip().split(",")
    countries.append([p[0], p[1], float(p[2]), float(p[3])])

for line in read_file("tariff.txt")[1:]:
    p = line.strip().split(",")
    tariffs.append([p[0], p[1], float(p[2])])

for line in read_file("product.txt")[1:]:
    p = line.strip().split(",")
    products.append([p[0], p[1], p[2]])

for line in read_file("product_country.txt")[1:]:
    p = line.strip().split(",")
    product_country.append([p[0], p[1], float(p[2])])

for line in read_file("shopping_list.txt"):
    shopping.append(line.strip())


# SECTION A: Trade Deficits

print("\nSECTION A")
print("\nCountries With Highest Trade Deficit:\n")

deficits = []
for c in countries:
    deficits.append([c[1], c[2] - c[3]])

deficits.sort(key=lambda x: x[1], reverse=True)

headers = ["Country", "Trade Deficit (Billions USD)"]
widths = [35, 28]
table_width = sum(widths) + 3 * len(widths) + 1

print_border(table_width)
print_row(headers, widths)
print_border(table_width)

for i in range(5):
    print_row([deficits[i][0], format_currency(deficits[i][1], widths[1])], widths)

print_border(table_width)


# SECTION B: Product Analysis

print("\nSECTION B")

# Q1 - Products Per Industry
print("\nProducts Per Industry:\n")
industry_count = []

for p in products:
    industry = p[1].strip()
    found = False
    for item in industry_count:
        if item[0] == industry:
            item[1] += 1
            found = True
            break
    if not found:
        industry_count.append([industry, 1])

industry_count.sort(key=lambda x: x[0])

headers = ["Industry", "Number of Products"]
widths = [30, 20]
table_width = sum(widths) + 3 * len(widths) + 1

print_border(table_width)
print_row(headers, widths)
print_border(table_width)

for row in industry_count:
    print_row([row[0], str(row[1])], widths)

print_border(table_width)

# Q2 - Exclusive Products (Sold by exactly one country)
print("\nExclusive Products:\n")
exclusive = []

for p in products:
    pid = p[0].strip()
    match_count = 0
    last_country_code = ""

    for pc in product_country:
        if pc[0].strip() == pid:
            match_count += 1
            last_country_code = pc[1].strip()

    # If only one country sells it, which country iss it
    if match_count == 1:
        for c in countries:
            if c[0].strip() == last_country_code:
                exclusive.append([pid, p[2].strip(), c[1].strip()])

# Q3 - Countries With Most Exclusive Products
print("\nCountries With Most Exclusive Products:\n")
exclusive_count = []

for e in exclusive:
    country = e[2]
    found = False
    for item in exclusive_count:
        if item[0] == country:
            item[1] += 1
            found = True
            break
    if not found:
        exclusive_count.append([country, 1])

# Sort by count descending, then alphabetical name
exclusive_count.sort(key=lambda x: (-x[1], x[0]))

headers = ["Country", "No. of Exclusive Products"]
widths = [35, 30]
table_width = sum(widths) + 3 * len(widths) + 1

print_border(table_width)
print_row(headers, widths)
print_border(table_width)

if exclusive_count:
    max_val = exclusive_count[0][1]
    for row in exclusive_count:
        if row[1] == max_val:
            print_row([row[0], str(row[1])], widths)

print_border(table_width)

# Q4 - Industries With Fewest Exclusives
print("\nIndustries With Fewest Exclusives:\n")
industry_exclusive = []

for e in exclusive:
    pid = e[0]
    industry = ""
    for p in products:
        if p[0].strip() == pid:
            industry = p[1].strip()
            break

    found = False
    for item in industry_exclusive:
        if item[0] == industry:
            item[1] += 1
            found = True
            break
    if not found:
        industry_exclusive.append([industry, 1])

industry_exclusive.sort(key=lambda x: (x[1], x[0]))

headers = ["Industry", "No. of Exclusive Products"]
widths = [35, 30]
table_width = sum(widths) + 3 * len(widths) + 1

print_border(table_width)
print_row(headers, widths)
print_border(table_width)

if industry_exclusive:
    min_val = industry_exclusive[0][1]
    for row in industry_exclusive:
        if row[1] == min_val:
            print_row([row[0], str(row[1])], widths)

print_border(table_width)

# Q5 - Most Productive Countries
print("\nMost Productive Countries:\n")
country_product_count = []

for pc in product_country:
    code = pc[1].strip()
    found = False
    for item in country_product_count:
        if item[0] == code:
            item[1] += 1
            found = True
            break
    if not found:
        country_product_count.append([code, 1])

country_product_full = []
for item in country_product_count:
    for c in countries:
        if c[0].strip() == item[0]:
            country_product_full.append([c[1].strip(), item[1]])

country_product_full.sort(key=lambda x: (-x[1], x[0]))

headers = ["Country", "Number of Products"]
widths = [35, 25]
table_width = sum(widths) + 3 * len(widths) + 1

print_border(table_width)
print_row(headers, widths)
print_border(table_width)

if country_product_full:
    max_prod = country_product_full[0][1]
    for row in country_product_full:
        if row[1] == max_prod:
            print_row([row[0], str(row[1])], widths)

print_border(table_width)

# Q6 - Most Widespread Products
print("\nMost Widespread Products:\n")
product_country_count = []

for p in products:
    pid = p[0].strip()
    count = sum(1 for pc in product_country if pc[0].strip() == pid)
    product_country_count.append([p[2].strip(), count])

product_country_count.sort(key=lambda x: (-x[1], x[0]))

# Identify top 3 distinct country counts
top_values = []
for item in product_country_count:
    if item[1] not in top_values:
        top_values.append(item[1])
    if len(top_values) == 3:
        break

headers = ["Product Name", "Number of Countries"]
widths = [40, 25]
table_width = sum(widths) + 3 * len(widths) + 1

print_border(table_width)
print_row(headers, widths)
print_border(table_width)

for row in product_country_count:
    if row[1] in top_values:
        print_row([row[0], str(row[1])], widths)

print_border(table_width)


# SECTION C: Tariff Policy Analysis

print("\nSECTION C — Analyzing Government's Tariff Decisions")

# 1. Outrageous Tariffs 
print("\nOutrageous Tariffs:\n")
outrageous = []
for t in tariffs:
    if t[2] > 50:
        for c in countries:
            if c[0].strip() == t[0].strip() and c[1] not in outrageous:
                outrageous.append(c[1])

outrageous.sort()
headers = ["Country"]
widths = [40]
table_width = sum(widths) + 3 * len(widths) + 1

print_border(table_width)
print_row(headers, widths)
print_border(table_width)
for country in outrageous:
    print_row([country], widths)
print_border(table_width)

# 2. Tariff-Free Countries
print("\nTariff-Free Countries:\n")
tariff_free = []
for c in countries:
    if not any(t[0].strip() == c[0].strip() for t in tariffs):
        tariff_free.append(c[1])

tariff_free.sort()
print_border(table_width)
print_row(headers, widths)
print_border(table_width)
for country in tariff_free:
    print_row([country], widths)
print_border(table_width)

# 3. Selective Tariff Countries 
print("\nSelective Tariff Countries:\n")
selective = []
for c in countries:
    code = c[0].strip()
    applied = [t[1].strip() for t in tariffs if t[0].strip() == code]
    
    if applied and len(applied) < len(industry_count):
        for ind in industry_count:
            if ind[0] not in applied:
                selective.append([c[1], ind[0]])

selective.sort(key=lambda x: (x[0], x[1]))
headers = ["Country", "Industry"]
widths = [35, 30]
table_width = sum(widths) + 3 * len(widths) + 1

print_border(table_width)
print_row(headers, widths)
print_border(table_width)
for row in selective:
    print_row(row, widths)
print_border(table_width)


# SECTION D: Cost Optimization

print("\nSECTION D — Shopping List Cost Breakdown")
print("\nCheapest Import Strategy Under Tariffs:\n")

# lookup to optimize nested loop search
product_to_industry = {p[0].strip(): p[1].strip() for p in products}

breakdown = []
total_before = 0
total_tariff_paid = 0

for item_id in shopping:
    best_total = None
    
    # costs for every possible supplier
    for pc in product_country:
        if pc[0].strip() == item_id:
            base_price = pc[2]
            export_code = pc[1].strip()
            industry = product_to_industry.get(item_id, "")

            rate = 0
            for t in tariffs:
                if t[0].strip() == export_code and t[1].strip() == industry:
                    rate = t[2]
                    break

            landed_cost = base_price + (base_price * rate / 100)

            if best_total is None or landed_cost < best_total:
                best_total = landed_cost
                best_p, best_rate = base_price, rate
                best_c = next(c[1].strip() for c in countries if c[0].strip() == export_code)

    if best_total is not None:
        t_val = best_p * (best_rate / 100)
        total_before += best_p
        total_tariff_paid += t_val
        
        # Count total suppliers
        suppliers = sum(1 for pc in product_country if pc[0].strip() == item_id)
        
        breakdown.append([
            item_id, str(suppliers), best_c,
            format_currency(best_p), format_percent(best_rate),
            format_currency(t_val), format_currency(best_total)
        ])

headers = ["Product Name", "Countries", "Best Country", "Actual Cost", "Tariff %", "Tariff Val", "Total Cost"]
widths = [25, 12, 25, 15, 12, 15, 15]
table_width = sum(widths) + 3 * len(widths) + 1

print_border(table_width)
print_row(headers, widths)
print_border(table_width)
for row in breakdown:
    print_row(row, widths)
print_border(table_width)

print("Cost Before Tariff:", format_currency(total_before))
print("Total Tariff Paid:", format_currency(total_tariff_paid))
print("Grand Total:", format_currency(total_before + total_tariff_paid))