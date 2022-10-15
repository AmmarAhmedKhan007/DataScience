
from itemadapter import ItemAdapter

class QuotetutorialPipeline:
    def process_item(self, item, spider):
        print("Pipelines: "+ item['title'][0])
        return item