#
# Autogenerated by Thrift Compiler (0.12.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def ComposePost(self, req_id, user_name, user_id, text, media_ids, media_types, post_type):
        """
        Parameters:
         - req_id
         - user_name
         - user_id
         - text
         - media_ids
         - media_types
         - post_type

        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def ComposePost(self, req_id, user_name, user_id, text, media_ids, media_types, post_type):
        """
        Parameters:
         - req_id
         - user_name
         - user_id
         - text
         - media_ids
         - media_types
         - post_type

        """
        self.send_ComposePost(req_id, user_name, user_id, text, media_ids, media_types, post_type)
        self.recv_ComposePost()

    def send_ComposePost(self, req_id, user_name, user_id, text, media_ids, media_types, post_type):
        self._oprot.writeMessageBegin('ComposePost', TMessageType.CALL, self._seqid)
        args = ComposePost_args()
        args.req_id = req_id
        args.user_name = user_name
        args.user_id = user_id
        args.text = text
        args.media_ids = media_ids
        args.media_types = media_types
        args.post_type = post_type
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_ComposePost(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = ComposePost_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.se is not None:
            raise result.se
        return


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["ComposePost"] = Processor.process_ComposePost

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_ComposePost(self, seqid, iprot, oprot):
        args = ComposePost_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ComposePost_result()
        try:
            self._handler.ComposePost(args.req_id, args.user_name, args.user_id, args.text, args.media_ids, args.media_types, args.post_type)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ServiceException as se:
            msg_type = TMessageType.REPLY
            result.se = se
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("ComposePost", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class ComposePost_args(object):
    """
    Attributes:
     - req_id
     - user_name
     - user_id
     - text
     - media_ids
     - media_types
     - post_type

    """


    def __init__(self, req_id=None, user_name=None, user_id=None, text=None, media_ids=None, media_types=None, post_type=None,):
        self.req_id = req_id
        self.user_name = user_name
        self.user_id = user_id
        self.text = text
        self.media_ids = media_ids
        self.media_types = media_types
        self.post_type = post_type

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.req_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.user_name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.user_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.text = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.media_ids = []
                    (_etype96, _size93) = iprot.readListBegin()
                    for _i97 in range(_size93):
                        _elem98 = iprot.readI64()
                        self.media_ids.append(_elem98)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.media_types = []
                    (_etype102, _size99) = iprot.readListBegin()
                    for _i103 in range(_size99):
                        _elem104 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.media_types.append(_elem104)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.post_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ComposePost_args')
        if self.req_id is not None:
            oprot.writeFieldBegin('req_id', TType.I64, 1)
            oprot.writeI64(self.req_id)
            oprot.writeFieldEnd()
        if self.user_name is not None:
            oprot.writeFieldBegin('user_name', TType.STRING, 2)
            oprot.writeString(self.user_name.encode('utf-8') if sys.version_info[0] == 2 else self.user_name)
            oprot.writeFieldEnd()
        if self.user_id is not None:
            oprot.writeFieldBegin('user_id', TType.I64, 3)
            oprot.writeI64(self.user_id)
            oprot.writeFieldEnd()
        if self.text is not None:
            oprot.writeFieldBegin('text', TType.STRING, 4)
            oprot.writeString(self.text.encode('utf-8') if sys.version_info[0] == 2 else self.text)
            oprot.writeFieldEnd()
        if self.media_ids is not None:
            oprot.writeFieldBegin('media_ids', TType.LIST, 5)
            oprot.writeListBegin(TType.I64, len(self.media_ids))
            for iter105 in self.media_ids:
                oprot.writeI64(iter105)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.media_types is not None:
            oprot.writeFieldBegin('media_types', TType.LIST, 6)
            oprot.writeListBegin(TType.STRING, len(self.media_types))
            for iter106 in self.media_types:
                oprot.writeString(iter106.encode('utf-8') if sys.version_info[0] == 2 else iter106)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.post_type is not None:
            oprot.writeFieldBegin('post_type', TType.I32, 7)
            oprot.writeI32(self.post_type)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ComposePost_args)
ComposePost_args.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'req_id', None, None, ),  # 1
    (2, TType.STRING, 'user_name', 'UTF8', None, ),  # 2
    (3, TType.I64, 'user_id', None, None, ),  # 3
    (4, TType.STRING, 'text', 'UTF8', None, ),  # 4
    (5, TType.LIST, 'media_ids', (TType.I64, None, False), None, ),  # 5
    (6, TType.LIST, 'media_types', (TType.STRING, 'UTF8', False), None, ),  # 6
    (7, TType.I32, 'post_type', None, None, ),  # 7
)


class ComposePost_result(object):
    """
    Attributes:
     - se

    """


    def __init__(self, se=None,):
        self.se = se

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.se = ServiceException()
                    self.se.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ComposePost_result')
        if self.se is not None:
            oprot.writeFieldBegin('se', TType.STRUCT, 1)
            self.se.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ComposePost_result)
ComposePost_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'se', [ServiceException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs
