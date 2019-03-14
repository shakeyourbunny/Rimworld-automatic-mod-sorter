import logging
import os
import tkinter as tkinter
import xml.etree.ElementTree as ET
import logging
from time import sleep

from lxml import etree

import RWmanager
import downloader



class ModBase:
    DB = dict()#DB저장
    ActiveModlist = list()#modkey 저장(활성화)
    ConfigXmldir = str() #컨픽파일 경로 저장

    @classmethod
    def setDB(cls, DB):
        cls.DB = DB 
    
    def __init__(self):
        if ModBase.DB == {}:
            ModBase.setDB(ModBase.DB)

        if ModBase.ConfigXmldir == '':
            ModBase.ConfigXmldir = RWmanager.askfiledir('select Rimworld config file.', [('ModsConfig.xml', '*.*')])

        
        else:
            pass

        if ModBase.ActiveModlist == []:
            logging.info('select your ModsConfig.xml')
            configdir = RWmanager.askfiledir('Select your Rimworld config.xml file.', [('ModsConfig.xml', '*.*')])
            ModBase.ConfigXmldir = configdir
            root = RWmanager.LoadXML(configdir)
            ModBase.ActiveModlist = RWmanager.LoadActMod(root)
            logging.info('Active mod list loaded.')
            logging.info('current active mod number : {}'.format(len(ModBase.ActiveModlist)))


class Mod(ModBase):
    Modcount = 0
    MODs = list()

    def __init__(self, moddir, modkey):    
        self.MODkey = str(modkey)
        self.MODdir = str(moddir) # 폴더위치
        self.dir_Aboutxml = '{}/About/About.xml'.format(self.MODdir)
        self.MODname = parseXML(self.dir_Aboutxml, 'name')
        self.OrderNum = self.SetOrderNum()
        if self.OrderNum != None:
            Mod.Modcountplus()

        else:
            self.OrderNum = 30.0 # 고장난 모드 예약번호

    @classmethod
    def Modcountplus(cls):
        cls.Modcount += 1

    @staticmethod
    def getOrderNum(self):
        return self.OrderNum
    
    def SetOrderNum(self):
        if self.MODname in Mod.DB:
            num = Mod.DB[self.MODname]
            logging.info("grant mod number {} to mod name : {}".format(num, self.MODname))
            return float(num)

        else:
            logging.error('error while giving order number to mod : {}'.format(self.MODname))
            return None

class ModWorkshop(Mod):
    def __init__(self, modkey, moddir):
        super().__init__(modkey, moddir)

class ModLocal(Mod):
    def __init__(self, modkey, moddir):
        super().__init__(modkey, moddir)

def parseXML(dir_XML, attribute):
    if type(dir_XML) != type(str()):
        logging.error('cannot read XML file directory. ')
        logging.debug(str(dir_XML), ' - dir_XML 내용')
        return None
    
    if type(attribute) != type(str()):
        logging.error('wrong attribute data type.')
        logging.debug(str(attribute))
        return None

    try:
        doc = ET.parse(dir_XML)
        root = doc.getroot()
        name = root.find(attribute).text
        logging.debug('{}에서 {}를 찾았습니다.'.format(dir_XML, attribute))
        return name

    except Exception as e:
        logging.debug('parseXML에서 에러 발생')
        logging.debug(e)
    
def LoadMod(dir1, type1='Local'):
    '''
        dir = 모드 폴더 경로\n
        type = 'Local' 또는 'Workshop'
    '''
    logging.debug('LoadMod 호출')
    folderlist = os.listdir(dir1)
    logging.debug('dir1 폴더에서 폴더 {} 개를 찾았습니다.'.format(len(folderlist)))
    logging.debug(dir1)
    if type1 == 'Local':
        list1 = list()
        for folder in folderlist:
            try:
                logging.debug('폴더 {}'.format(folder))
                dir2 = dir1 + '/{}'.format(folder)
                list1.append(ModLocal(dir2, folder))
                logging.debug(folder, ' ', dir2)

            except Exception as e:
                logging.debug('LoadMod local 돌던 중 에러 발생')
                logging.debug('에러 코드 : {}'.format(e))
        Mod.MODs = Mod.MODs + list1

    else:
        list1 = list()
        for folder in folderlist:
            try:
                logging.debug('폴더 {}'.format(folder))
                dir2 = dir1 + '/{}'.format(folder)
                list1.append(ModWorkshop(dir2, folder))
                logging.debug('{} {}'.format(dir2, folder))

            except Exception as e:
                logging.debug('LoadMod workshop 돌던 중 에러 발생')
                logging.debug('에러 코드 : {}'.format(e))
        Mod.MODs = Mod.MODs + list1


def config_loader(cfdir, active_mod): #컨픽파일 모드 리스트 가져오기
    os.chdir(cfdir)
    doc = ET.parse('ModsConfig.xml')
    root = doc.getroot()
    ActiveMod = root.find('activeMods')

    for li in ActiveMod.findall('li'):
        active_mod.append(str(li.text))


def config_updater(cfdir, ML_sorted):
    os.chdir(cfdir)
    doc = ET.parse('ModsConfig.xml')
    root = doc.getroot()

    activeMod = root.find('activeMods')
    print('initializing config file...')

    for li in activeMod.findall('li'):
        activeMod.remove(li)

    sorted_mod = ET.SubElement(activeMod, 'li')
    for x in ML_sorted:
        sorted_mod = ET.SubElement(activeMod, 'li')
        sorted_mod.text = str(x[0][1])

    doc.write('ModsConfig.xml', encoding='UTF-8', xml_declaration='False')


if __name__ == '__main__':

    '''
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    x = RWmanager.askfolderdir()
    DB = downloader.download_DB(0.5)
    ModBase.setDB(DB)
    LoadMod(x, 'Workshop')
    print(len(Mod.MODs))
    '''