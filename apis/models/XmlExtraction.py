#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import xml.etree.ElementTree as ET


class XmlExtract(object):
    # Load all timestamps to list.
    def __new__(cls, file_name: str, frame_rate: str, width: str, height: str, timestamps: dict) -> bytes:
        cls.file_name = file_name
        cls.frame_rate = frame_rate
        cls.video_width = width
        cls.video_height = height
        cls.timestamps = timestamps
        return cls.generate_template()

    # Load xml template.
    @classmethod
    def generate_template(cls) -> bytes:
        xml_str = """<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE xmeml><xmeml version="4"></xmeml>"""
        root = ET.fromstring(xml_str)
        sequence = ET.SubElement(root, 'sequence')
        # sequence.name
        name = ET.SubElement(sequence, 'name')
        name.text = cls.file_name
        # sequence.rate
        rate = ET.SubElement(sequence, 'rate')
        # sequence.rate.timebase (a.k.a. frame rate)
        timebase = ET.SubElement(rate, 'timebase')
        timebase.text = cls.frame_rate
        # sequence.rate.ntsc
        ntsc = ET.SubElement(rate, 'ntsc')
        # NOTICE: ntsc not adapted! This may cause a bug.
        ntsc.text = 'FALSE'
        # sequence.media
        media = ET.SubElement(sequence, 'media')
        # sequence.media.video
        video = ET.SubElement(media, 'video')
        # sequence.media.video.format
        _format = ET.SubElement(video, 'format')
        # sequence.media.video.format.samplecharacteristics
        samplecharacteristics = ET.SubElement(_format, 'samplecharacteristics')
        # sequence.media.video.format.samplecharacteristics.rate
        _rate = ET.SubElement(samplecharacteristics, 'rate')
        _timebase = ET.SubElement(_rate, 'timebase')
        _timebase.text = cls.frame_rate
        _ntsc = ET.SubElement(_rate, 'ntsc')
        # NOTICE: ntsc not adapted! This may cause a bug.
        # ---------------------------------------------------------------------------------------------------
        _ntsc.text = 'FALSE'
        # ---------------------------------------------------------------------------------------------------
        # sequence.media.video.format.samplecharacteristics.codec
        codec = ET.SubElement(samplecharacteristics, 'codec')
        # sequence.media.video.format.samplecharacteristics.codec.name
        _name = ET.SubElement(codec, 'name')
        _name.text = 'Apple ProRes 422'
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata
        appspecificdata = ET.SubElement(codec, 'appspecificdata')
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.appname
        appname = ET.SubElement(appspecificdata, 'appname')
        appname.text = 'Final Cut Pro'
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.appmanufacturer
        appmanufacturer = ET.SubElement(appspecificdata, 'appmanufacturer')
        appmanufacturer.text = 'Apple Inc.'
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.appversion
        appversion = ET.SubElement(appspecificdata, 'appversion')
        # NOTICE: appversion not adapted! This may cause a bug.
        # ---------------------------------------------------------------------------------------------------
        appversion.text = '7.0'
        # ---------------------------------------------------------------------------------------------------
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data
        data = ET.SubElement(appspecificdata, 'data')
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data.qtcodec
        qtcodec = ET.SubElement(data, 'qtcodec')
        # NOTICE: Specs under qtcodec not adapted! This may cause a bug.
        # ---------------------------------------------------------------------------------------------------
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data.qtcodec.codecname
        codecname = ET.SubElement(qtcodec, 'codecname')
        codecname.text = 'Apple ProRes 422'
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data.qtcodec.codectypename
        codectypename = ET.SubElement(qtcodec, 'codectypename')
        codectypename.text = 'Apple ProRes 422'
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data.qtcodec.codectypecode
        codectypecode = ET.SubElement(qtcodec, 'codectypecode')
        codectypecode.text = 'apcn'
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data.qtcodec.codecvendorcode
        codecvendorcode = ET.SubElement(qtcodec, 'codecvendorcode')
        codecvendorcode.text = 'appl'
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data.qtcodec.spatialquality
        spatialquality = ET.SubElement(qtcodec, 'spatialquality')
        spatialquality.text = '1024'
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data.qtcodec.temporalquality
        temporalquality = ET.SubElement(qtcodec, 'temporalquality')
        temporalquality.text = '0'
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data.qtcodec.keyframerate
        keyframerate = ET.SubElement(qtcodec, 'keyframerate')
        keyframerate.text = '0'
        # sequence.media.video.format.samplecharacteristics.codec.appspecificdata.data.qtcodec.datarate
        datarate = ET.SubElement(qtcodec, 'datarate')
        datarate.text = '0'
        # ---------------------------------------------------------------------------------------------------
        # sequence.media.video.format.samplecharacteristics.width
        width = ET.SubElement(samplecharacteristics, 'width')
        width.text = cls.video_width
        # sequence.media.video.format.samplecharacteristics.height
        height = ET.SubElement(samplecharacteristics, 'height')
        height.text = cls.video_height
        # sequence.media.video.format.samplecharacteristics.pixelaspectratio
        pixelaspectratio = ET.SubElement(samplecharacteristics, 'pixelaspectratio')
        # NOTICE: pixelaspectratio not adapted! This may cause a bug.
        # ---------------------------------------------------------------------------------------------------
        pixelaspectratio.text = 'square'
        # ---------------------------------------------------------------------------------------------------
        # sequence.media.video.track
        track = ET.SubElement(video, 'track')
        # sequence.media.video.track.clipitem
        clipitem = ET.SubElement(track, 'clipitem')
        # do a FOR function to fill video track by chunks
        cls.clip_item_enumerate(chunk_type='video', current_node=clipitem)
        # sequence.media.audio
        audio = ET.SubElement(media, 'audio')
        # sequence.media.audio.outputs
        outputs = ET.SubElement(audio, 'outputs')
        # NOTICE: group (a.k.a. channels) not adapted! Only two groups by default. (Stereo)
        # ---------------------------------------------------------------------------------------------------
        # sequence.media.audio.outputs.group (channel 1)
        group = ET.SubElement(outputs, 'group')
        # sequence.media.audio.outputs.group.index
        index = ET.SubElement(group, 'index')
        index.text = '1'
        # sequence.media.audio.outputs.group.numchannels
        numchannels = ET.SubElement(group, 'numchannels')
        numchannels.text = '1'
        # sequence.media.audio.outputs.group.downmix
        downmix = ET.SubElement(group, 'downmix')
        downmix.text = '0'
        # sequence.media.audio.outputs.group.channel
        channel = ET.SubElement(group, 'channel')
        # sequence.media.audio.outputs.group.channel.index
        _index = ET.SubElement(channel, 'index')
        _index.text = '1'
        # sequence.media.audio.outputs.group (channel 2)
        group = ET.SubElement(outputs, 'group')
        # sequence.media.audio.outputs.group.index
        index = ET.SubElement(group, 'index')
        index.text = '2'
        # sequence.media.audio.outputs.group.numchannels
        numchannels = ET.SubElement(group, 'numchannels')
        numchannels.text = '1'
        # sequence.media.audio.outputs.group.downmix
        downmix = ET.SubElement(group, 'downmix')
        downmix.text = '0'
        # sequence.media.audio.outputs.group.channel
        channel = ET.SubElement(group, 'channel')
        # sequence.media.audio.outputs.group.channel.index
        _index = ET.SubElement(channel, 'index')
        _index.text = '2'
        # ---------------------------------------------------------------------------------------------------
        # sequence.media.audio.track (channel 1)
        _track_1 = ET.SubElement(audio, 'track')
        # sequence.media.audio.track.clipitem
        _clipitem_1 = ET.SubElement(_track_1, 'clipitem')
        # do a FOR function to fill audio track by chunks
        cls.clip_item_enumerate(chunk_type='audio_1', current_node=_clipitem_1)
        # sequence.media.audio.track (channel 2)
        _track_2 = ET.SubElement(audio, 'track')
        # sequence.media.audio.track.clipitem
        _clipitem_2 = ET.SubElement(_track_2, 'clipitem')
        # do a FOR function to fill audio track by chunks
        cls.clip_item_enumerate(chunk_type='audio_2', current_node=_clipitem_2)
        return ET.tostring(root, encoding='utf8')

    # Write chunks from args list to template.
    @classmethod
    def clip_item_enumerate(cls, chunk_type, current_node):
        # Use chunk type to sort ids.
        clipitem = current_node
        for i, chunk in enumerate(cls.timestamps.items()):
            if chunk_type == 'video':
                clipitem.attrib['id'] = 'clipitem-{}'.format(i + 1)
            elif chunk_type == 'audio_1':
                clipitem.attrib['id'] = 'clipitem-{}'.format(2 * (i + 1))
            elif chunk_type == 'audio_2':
                clipitem.attrib['id'] = 'clipitem-{}'.format(3 * (i + 1))
            else:
                raise ValueError
            # Set a timer to count start and end, while end = start + (out - in).
            timer = 1
            # clipitem.name
            name = ET.SubElement(clipitem, 'name')
            name.text = cls.file_name
            # clipitem.start
            start = ET.SubElement(clipitem, 'start')
            start.text = ''.format(timer)
            # clipitem.end
            end = ET.SubElement(clipitem, 'end')
            duration = int(chunk[1]['out']) - int(chunk[1]['in'])
            timer += duration
            end.text = ''.format(timer)
            # clipitem.in
            _in = ET.SubElement(clipitem, 'in')
            _in.text = chunk[1]['in']
            # clipitem.out
            _out = ET.SubElement(clipitem, 'out')
            _out.text = chunk[1]['out']
            # clipitem.file
            file = ET.SubElement(clipitem, 'file')
            file.attrib['id'] = 'file-1'
            if i == 0:
                # clipitem.file.name
                _name = ET.SubElement(file, 'name')
                _name.text = cls.file_name
                # clipitem.file.pathurl
                pathurl = ET.SubElement(file, 'pathurl')
                pathurl.text = 'file://localhost/{}'.format(cls.file_name)
                # clipitem.file.rate
                rate = ET.SubElement(file, 'rate')
                # clipitem.file.rate.timebase
                timebase = ET.SubElement(rate, 'timebase')
                timebase.text = cls.frame_rate
                # clipitem.file.rate.ntsc
                ntsc = ET.SubElement(rate, 'ntsc')
                ntsc.text = 'FALSE'
                # clipitem.file.media
                media = ET.SubElement(file, 'media')
                # clipitem.file.media.video
                video = ET.SubElement(media, 'video')
                # clipitem.file.media.video.samplecharacteristics
                samplecharacteristics = ET.SubElement(video, 'samplecharacteristics')
                # clipitem.file.media.video.samplecharacteristics.rate
                _rate = ET.SubElement(samplecharacteristics, 'rate')
                # clipitem.file.media.video.samplecharacteristics.rate.timebase
                _timebase = ET.SubElement(_rate, 'timebase')
                _timebase.text = cls.frame_rate
                # clipitem.file.media.video.samplecharacteristics.rate.ntsc
                _ntsc = ET.SubElement(_rate, 'ntsc')
                ntsc.text = 'FALSE'
                # clipitem.file.media.video.samplecharacteristics.width
                width = ET.SubElement(samplecharacteristics, 'width')
                width.text = cls.video_width
                # clipitem.file.media.video.samplecharacteristics.height
                height = ET.SubElement(samplecharacteristics, 'height')
                height.text = cls.video_height
                # clipitem.file.media.audio
                audio = ET.SubElement(media, 'audio')
                # clipitem.file.media.audio.samplecharacteristics
                _samplecharacteristics = ET.SubElement(audio, 'samplecharacteristics')
                # clipitem.file.media.audio.samplecharacteristics.samplerate
                samplerate = ET.SubElement(_samplecharacteristics, 'samplerate')
                samplerate.text = '48000'
                # clipitem.file.media.audio.channelcount
                channelcount = ET.SubElement(audio, 'channelcount')
                channelcount.text = '2'

'''
# Debug-only
if __name__ == "__main__":
    dic = {'1': {'in': '0', 'out': '42'}, '2': {'in': '135', 'out': '300'}}
    print(XmlExtract('foo.mp4', '30', '1280', '720', dic))

'''
