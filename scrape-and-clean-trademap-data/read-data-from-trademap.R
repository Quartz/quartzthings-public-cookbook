library(tidyverse)
library(xml2)
library(rvest)

#=== step up ===#

files <- list.files(path = "output_directory/", pattern = '\\.xls')
output_data = as_tibble()

#=== loop through the excel files and combine them into one table ===#

for (i in 1:length(files)) {

  print(i)

  parsed_file <- read_html(paste('output_directory/',files[i],sep=''))
  product_id <- str_extract(str_trim(xml_text(xml_find_all(parsed_file, 'body/table[1]/tr'))[2]), '[:digit:]+')
  
  tmp <- (xml_find_all(parsed_file, "//*[@id='ctl00_PageContent_MyGridView1']") %>%
            html_table())[[1]] %>% 
    tibble::as_tibble() %>%
    mutate(HS = product_id) %>%
    # "Importers" or "Exporters" depending on what you downloaded:
    # (take a look at the excel file to determine the correct colnames)
    gather(key = 'time', value = 'value', -Importers, -HS) 

  if (nrow(chocolate) == 0) {
    output_data = tmp
  } else {
    output_data = output_data %>% bind_rows(tmp)
  }
  
}

#=== get rid of redundancy introduced by downloads ===#

output_data <- unique(output_data) 

#=== output file ===#

write_csv('output.csv', output_data)

