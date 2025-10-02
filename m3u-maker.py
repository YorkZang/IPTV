import re

def read_file_lines(file_path,output_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if len(line) > 80:
                pattern = r"(?:\')*(.*?)'"
                matches = re.findall(pattern, line.strip())
                for match in matches:
                    if(len(match) > 80): 
                         change_to_dict(match,output_path)

def change_to_dict(rsp_str,output_path):
    lists = rsp_str.replace("UserChannelID","UserID").replace("ChannelID", "tvg-id").replace("ChannelName", "tvg-name").replace("ChannelURL", "tvg-url").split(',')
    m3u = ""    
    for item in lists:
        if 'tvg' in item:
            m3u += item + ','
    name = get_content_between_chars(m3u, 'tvg-name="', '",tvg-url=')
    s = m3u.replace(',',' ').split('tvg-url="')
    if s[1].find('?') != -1:
        url = s[1].split('?')[0]
    else:
        url = s[1][:-2]
    
    create_and_write_file(output_path, '#EXTINF:-1 '+ s[0] + 'tvg-logo="" group-title="",'+ name +'\n' + url + '\n')

def get_content_between_chars(text, char1, char2):
    start_index = text.find(char1) + len(char1)
    end_index = text.find(char2)
    if start_index == -1 or end_index == -1 or start_index >= end_index:
        return ""
    return text[start_index:end_index]

def create_and_write_file(output_path, content):
    with open(output_path,'a', encoding='utf-8') as file:
        if file.tell() == 0:
            file.write('#EXTM3U\n')
            print(f"File created and written to: {output_path}")
        file.writelines(content)
    

if __name__ == "__main__":
    
    #file_path = r'D:\test\dx-getchannellistHWCTC.jsp'
    file_path = r'D:\test\lt-getchannellistHWCU-11.jsp'
    output_path = r'D:\test\lt-output.m3u'
    read_file_lines(file_path,output_path)




