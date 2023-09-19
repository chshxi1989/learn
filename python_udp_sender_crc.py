# 导入模块
import socket
import struct
import crcmod
 
class UdpFrame:
    def __init__(self):
        #fe 55 01 00 04 01 01 04 13 00 00 02 00 00 a9 f2
        self.sop1 = 0xfe
        self.sop2 = 0x55
        self.type = 1 #消息指令
        self.flag = 0 #请求帧
        self.srcSysId = 4
        self.srcCompId = 1
        self.dstSysId = 1
        self.dstCompId = 4
        self.msgId = 19
        self.seq = 0
        self.len = 2
        self.payload = [0, 0]

    def get_struct_data(self):
        # B: unsigned char, H: unsigned short, I: unsight int
        data = struct.pack("BBBBBBHBB", self.type, self.flag, self.srcSysId, self.srcCompId, self.dstSysId, self.dstCompId, self.msgId, self.seq, self.len)
        for num in self.payload:
            data += struct.pack("B", num)

        #计算crc值，不包括前面2个字节的sop1和sop2, 0x11021=x16+x12+x5+1
        xmodem_crc_func = crcmod.mkCrcFun(0x11021, rev=True, initCrc=0xFFFF, xorOut=0x0000)
        crc = xmodem_crc_func(data)
        print("crc16: %s" % hex(crc))

        #拼接数据
        result = struct.pack("BB", self.sop1, self.sop2)
        result += data
        result += struct.pack("H", crc)
        return result


  def UdpSender(data):
    # 创建一个UDP套接字对象，注意ip地址要是发送数据的网卡ip地址
    host_ip = "145.192.1.33"
    host_port = 8888
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind
    # 定义目标主机和端口
    remote_ip = "145.192.1.64"
    remote_port = 7894
     
    # 发送消息
    udp_socket.sendto(data, (remote_ip, remote_port))
    print('发送消息：', data)

    # 关闭套接字
    udp_socket.close()


if __name__=="__main__":
    #UdpSender()
    frame = UdpFrame()
    data = frame.get_struct_data()
    str = ""
    for num in data:
       str += "0x%02x " % (num)
    print(str)
    UdpSender(data)


