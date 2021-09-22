from scrapy.pipelines.images import ImagesPipeline

class customImagePipeline(ImagesPipeline):
    def file_path(self,request,response=None, info=None):
        return request.url.split('/')[-1]
