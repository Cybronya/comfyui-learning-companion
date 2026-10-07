# HeyGenReferenceToVideoNode

## 节点类型

`HeyGenReferenceToVideoNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model.reference_images.image_1:IMAGE`（2 次）
- `model.reference_videos.video_1:VIDEO`（2 次）
- `model.reference_audios.audio_1:AUDIO`（2 次）
- `model.reference_images.image_2:IMAGE`（1 次）
- `model.reference_images.image_3:IMAGE`（1 次）

## 输出

- `VIDEO:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["heygen-video-1", "@Image1 stands at a plain warm grey studio backdrop holding the handbag from @Image2 up beside her c`（1 次）
- `["heygen-video-1", "A woman in her late twenties in a cream knit sweater sits at a sunlit kitchen counter and holds up a`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
