# WujiAudioLoader

## 节点类型

`WujiAudioLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `音频文件:COMBO`（4 次）
- `帧率:FLOAT`（4 次）
- `起始秒:FLOAT`（4 次）
- `结束秒:FLOAT`（4 次）
- `尾静音秒:FLOAT`（4 次）
- `音频分离:BOOLEAN`（4 次）
- `识别字幕:BOOLEAN`（4 次）
- `时间戳字幕:BOOLEAN`（4 次）

## 输出

- `原音频:AUDIO`（4 次）
- `人声:AUDIO`（4 次）
- `背景音:AUDIO`（4 次）
- `帧数:INT`（4 次）
- `字幕文本:STRING`（4 次）
- `SRT字幕:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["3539fc5a75b7f18ccd341f9f50b6a53821b76ebf94f35a7f9d398bb3aa59fdbe.mp3", 25, 0, 6, 2, false, false, false, "image", {"pa`（2 次）
- `["9432f151cd9712b9fc73aacf3283dc1afc38d966dac43854084e1b240c844cf9.mp3", 25, 0, 6, 2, false, false, false, "image", {"pa`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
