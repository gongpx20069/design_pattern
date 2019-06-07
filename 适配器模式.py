import abc
class MediaPlayer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self,audioType, filename):
        pass

class AdvanceMediaPlayer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def playVlc(self,filename):
        pass
    @abc.abstractmethod
    def playMp4(self,filename):
        pass

class VlcPlayer(AdvanceMediaPlayer):
    def playVlc(self,filename):
        print("Playing vlc file. Name: {}".format(filename))
    def playMp4(self,filename):
        pass

class Mp4Player(AdvanceMediaPlayer):
    def playVlc(self,filename):
        pass
    def playMp4(self,filename):
        print("Playing mp4 file. Name:{}".format(filename))

class MediaAdapter(MediaPlayer):
    def __init__(self,audioType):
        if audioType=="vlc":
            self.advanceMusicPlayer = VlcPlayer()
        elif audioType=="mp4":
            self.advanceMusicPlayer = Mp4Player()
    def play(self,audioType, filename):
        if audioType=="vlc":
            self.advanceMusicPlayer.playVlc(filename)
        elif audioType=="mp4":
            self.advanceMusicPlayer.playMp4(filename)

class AudioPlayer(MediaPlayer):
    def play(self,audioType, filename):
        if audioType=="mp3":
            print("Playing mp3 file. Name:{}".format(filename))
        elif audioType=="vlc" or audioType=="mp4":
            self.mediaAdapter = MediaAdapter(audioType)
            self.mediaAdapter.play(audioType,filename)
        else:
            print("Invalid media. "+audioType+" format not supported")

if __name__ == '__main__':
    '''
    适配器模式的优点：
    1. 将一个类的接口转换成客户希望的另外一个接口
    2. 适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作
    3. 可以让任何两个没有关联的类一起运行
    4. 提高了类的复用
    5. 增加了类的透明度
    6. 灵活性好
    '''
    #使用AudioPlayer来播放不同类型的音频格式
    audioPlayer=AudioPlayer()
    audioPlayer.play("mp3", "beyond the horizon.mp3");
    audioPlayer.play("mp4", "alone.mp4");
    audioPlayer.play("vlc", "far far away.vlc");
    audioPlayer.play("avi", "mind me.avi");