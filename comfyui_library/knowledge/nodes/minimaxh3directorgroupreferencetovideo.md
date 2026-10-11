# MiniMaxH3DirectorGroupReferenceToVideo

## 节点类型

`MiniMaxH3DirectorGroupReferenceToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `ref_images.ref_image_0:IMAGE`（10 次）
- `ref_images.ref_image_1:IMAGE`（10 次）
- `ref_videos.ref_video_0:IMAGE`（10 次）
- `ref_video_audios.ref_video_audio_0:AUDIO`（10 次）
- `ref_audios.ref_audio_0:AUDIO`（10 次）
- `prompt:STRING`（10 次）
- `duration_sec:FLOAT`（10 次）
- `ref_images.ref_image_2:IMAGE`（10 次）
- `ref_videos.ref_video_1:IMAGE`（5 次）
- `ref_audios.ref_audio_1:AUDIO`（2 次）

## 输出

- `group:MMX_DIR_GROUP`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["subject_definitions:\n<Subject 1> is the sleek, brushed aluminum smartphone in <Picture 1>, featuring a titanium-grade`（2 次）
- `["- 将视频1女生说的话：“我们之间不可能在一起的，不是不爱，是我们真的走不到最后的”。改成音频1的台词：“别走了，好吗？这一次，我们不要放开彼此”，并略微调整对应的表演", 15]`（2 次）
- `["主体定义:\n<Picture 1> 是男孩主角，展现正面、侧面与背面的三视图，棕色乱发，身穿带火箭贴布的牛仔外套，卡其工装裤配红白帆布鞋，背景为温馨书房。\n<Picture 2> 是宠物狗主角，同样呈现正侧背三视角，深棕卷毛，佩戴蓝`（2 次）
- `["主体定义:\n<Picture 1> 是魔法少女星野梦，展现正面、侧面、背面的三视图，粉色双马尾，身穿粉白渐变蓬蓬裙，手持星星魔杖，过膝袜，背景为星夜舞台。\n<Picture 2> 是魔法少女月岛铃，同样呈现正侧背三视角，蓝色高马尾，`（1 次）
- `["主体定义:\n<Picture 1> 是一张未来感透明智能手机的概念渲染图，展示了音乐节奏游戏“Dance Magic”的启动界面，图标为两个 Q 版魔法少女组成的心形图案。\n<Subject 1> 是 <Picture 1> 中那部`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
