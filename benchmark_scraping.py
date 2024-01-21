from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re
import json




headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}) 

url = "https://www.userbenchmark.com/EFps/,,,_,,,_Fortnite,2080,9400F,"

page = requests.get(url= url, headers= headers)

print(page)

soup = BeautifulSoup(page.content, "html.parser")

# content = soup.find("span", attrs= {'class': 'select2-hidden-accessible'})

# <a href="javascript:void(0)" class="select2-choice select2-default" tabindex="-1">   <span class="select2-chosen" id="select2-chosen-2">GPU</span><abbr class="select2-search-choice-close"></abbr>   <span class="select2-arrow" role="presentation"><b role="presentation"></b></span></a>
# <div class="select2-container select_choose_efpsLgpuacro" id="s2id_autogen1"><a href="javascript:void(0)" class="select2-choice select2-default" tabindex="-1">   <span class="select2-chosen" id="select2-chosen-2">GPU</span><abbr class="select2-search-choice-close"></abbr>   <span class="select2-arrow" role="presentation"><b role="presentation"></b></span></a><label for="s2id_autogen2" class="select2-offscreen"></label><input class="select2-focusser select2-offscreen" type="text" aria-haspopup="true" role="button" aria-labelledby="select2-chosen-2" id="s2id_autogen2"></div>
# <ul class="select2-results" role="listbox" id="select2-results-2"><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-119" role="option"><span class="">Nvidia 2070S<span class="pull-right">163</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-120" role="option"><span class="">Nvidia 2080<span class="pull-right">159</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-121" role="option"><span class="">AMD 5700-XT<span class="pull-right">137</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-122" role="option"><span class="">Nvidia 2060S<span class="pull-right">130</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-123" role="option"><span class="">Nvidia 2060<span class="pull-right">122</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-124" role="option"><span class="">AMD 5700<span class="pull-right">119</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-125" role="option"><span class="">Nvidia 1660S<span class="pull-right">111</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-126" role="option"><span class="">Nvidia 1660-Ti<span class="pull-right">108</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-127" role="option"><span class="">Nvidia 1070<span class="pull-right">103</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-128" role="option"><span class="">Nvidia 1660<span class="pull-right">94</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-129" role="option"><span class="">Nvidia 1060-6GB<span class="pull-right">82</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-130" role="option"><span class="">AMD 580<span class="pull-right">77</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-131" role="option"><span class="">Nvidia 1060-3GB<span class="pull-right">76</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-132" role="option"><span class="">Nvidia 1650<span class="pull-right">66</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-133" role="option"><span class="">AMD 570<span class="pull-right">56</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-134" role="option"><span class="">Nvidia 1050-Ti<span class="pull-right">49</span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-135" role="option"><span class="mutedtext">3080<span class="pull-right"></span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-136" role="option"><span class="mutedtext">6800-XT<span class="pull-right"></span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-137" role="option"><span class="mutedtext">2080-Ti<span class="pull-right"></span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-138" role="option"><span class="mutedtext">3070<span class="pull-right"></span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-139" role="option"><span class="mutedtext">3060-Ti<span class="pull-right"></span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-140" role="option"><span class="mutedtext">2070<span class="pull-right"></span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-141" role="option"><span class="mutedtext">1080<span class="pull-right"></span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-142" role="option"><span class="mutedtext">5600-XT<span class="pull-right"></span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-143" role="option"><span class="mutedtext">Vega-56<span class="pull-right"></span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-144" role="option"><span class="mutedtext">1650S<span class="pull-right"></span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-145" role="option"><span class="mutedtext">590<span class="pull-right"></span></span></div></li><li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-146" role="option"><span class="mutedtext">480<span class="pull-right"></span></span></div></li></ul>
# <div class="select2-result-label" id="select2-result-label-289" role="option"><span class="">AMD 5700-XT<span class="pull-right">137</span></span></div>
# print(content)

# driver = webdriver.Firefox()
# driver.get(url)

# # Locate the dropdown element by ID
# dropdown = Select(driver.find_element_by_id('select2-chosen-2'))  # Replace 'dropdown-id' with the actual ID of the dropdown

# # Print the values of the options
# for option in dropdown.options:
#     print(option.text)

# # Close the browser window
# driver.quit()

def extract_dropdown_items(js_code):
    pattern = r"data:{results:(.*?)]"
    match = re.search(pattern, js_code)
    if match:
        # Extract the content inside the 'data' string
        data_string = match.group(1)

        # Convert the string to a list of dictionaries
        data_list = json.loads(data_string)

        # Extract 't' and 'p' values from each dictionary
        for entry in data_list:
            t_value = entry.get('t')
            p_value = entry.get('p')
            print(f"'t': {t_value}, 'p': {p_value}")
        return "found"
    return []

def add_quotes(match):
    key = match.group(1)
    value = match.group(2)
    return f'"{key}": {value}'




# Extract dropdown items for each dropdown
dropdown1_js = soup.find('script', string=lambda text:'.select_choose_efpsLgpuacro' in text if text else False).text
print (type(dropdown1_js))
# dropdown1_items = extract_dropdown_items(dropdown1_js)
pattern = r"data:{results:(.*?)]"
match = re.search(pattern, dropdown1_js)
# print(match)
# add_quotes(match)
# # Use regular expressions to find and modify key-value pairs


# print(output_string)
if match:
        # Extract the content inside the 'data' string
        # data_string = match.group(1)
        # print(data_string)
    output_string = re.sub(r'(\w+):([^\s,}]+)', add_quotes, match.group(1))
    # print(match.group(0))
    output_string = output_string.replace('[', '')
    output_string = output_string.replace("'", '"') + ','
    output_string.strip()
    data_list = output_string.split('},')
    del data_list[-1]
    # print(data_list)
    json_data_list = []
    for i in data_list:
        # print(i)
        each = i + "}"
        # print(each)
        json_data = json.loads(each)
        json_data_list.append(json_data) 
    
    # print(json_data_list)
    for entry in json_data_list:
        t_value = entry.get('t')
        p_value = entry.get('p')
        print(f"'t': {t_value}, 'p': {p_value}")

#         # Convert the string to a list of dictionaries
    # data_list = json.loads(output_string)
    # print(data_list)

        # Extract 't' and 'p' values from each dictionary
    

# dropdown2_js = soup.find('script', string=re.compile('.*select_choose_efpsLcpuacro.*')).text
# dropdown2_items = extract_dropdown_items(dropdown2_js)

# specific_script_tag = soup.find('script', string=lambda text: 'specific content' in text if text else False)

# dropdown3_js = soup.find('script', string=re.compile('.*select_choose_efpsLnondefacro.*')).text
# dropdown3_items = extract_dropdown_items(dropdown3_js)

# Print the extracted dropdown items
# print("Dropdown 1 Items:")
# for item in dropdown1_items:
#     print(item)

# print("\nDropdown 2 Items:")
# for item in dropdown2_items:
#     print(item)

# print("\nDropdown 3 Items:")
# for item in dropdown3_items:
#     print(item)