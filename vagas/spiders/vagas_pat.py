# -*- coding: utf-8 -*-
import scrapy

class VagasPatSpider(scrapy.Spider):
    name = 'vagas_pat'
    start_urls = ['http://servicos2.sjc.sp.gov.br/servicos/vagas_emprego_pat.aspx']

    def parse(self, response):
        tds = response.xpath('.//table//tr')
        for td in tds:
            #vaga = td.xpath('.//td[@style = "width:245px;"]/text()').extract_first()
            vaga = td.xpath('.//td[contains(@style, "width:245px;")]/text()').extract_first()
            #local = td.xpath('.//td[@style = "width:70px;"]/text()').extract_first()
            local = td.xpath('.//td[contains(@style, "width:70px;")]/text()').extract_first()
            #quantidade = td.xpath('.//td[@style = "width:50px;"]/text()').extract_first()
            quantidade = td.xpath('.//td[contains(@style, "width:50px;")]/text()').extract_first()
            #aceita_pcd = td.xpath('.//td[@style = "width:82px;"]/text()').extract_first()
            aceita_pcd = td.xpath('.//td[contains(@style, "width:82px;")]/text()').extract_first()
            #exclusiva_pcd = td.xpath('.//td[@style = "width:100px;"]/text()').extract_first()
            exclusiva_pcd = td.xpath('.//td[contains(@style, "width:100px;")]/text()').extract_first()
            #escolaridade = td.xpath('.//td[@style = "width:175px;"]/text()').extract_first()
            escolaridade = td.xpath('.//td[contains(@style, "width:175px;")]/text()').extract_first()
            #experiencia = td.xpath('.//td[@style = "width:60px;"]/text()').extract_first()
            experiencia = td.xpath('.//td[contains(@style, "width:60px;")]/text()').extract_first()
            
            yield {
                'vaga': vaga,
                'local': local,
                'quantidade': quantidade,
                'aceita_pcd': aceita_pcd,
                'exclusiva_pcd': exclusiva_pcd,
                'escolaridade': escolaridade,
                'experiencia': experiencia,
            }
