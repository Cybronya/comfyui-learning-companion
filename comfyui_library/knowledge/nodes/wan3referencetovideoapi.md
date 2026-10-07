# Wan3ReferenceToVideoApi

## 节点类型

`Wan3ReferenceToVideoApi`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model.reference_images.image1:IMAGE`（2 次）
- `model.reference_videos.video1:VIDEO`（2 次）
- `model.reference_audios.audio1:AUDIO`（2 次）
- `model.reference_images.image2:IMAGE`（1 次）
- `model.reference_images.image3:IMAGE`（1 次）

## 输出

- `VIDEO:VIDEO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["wan3.0-video", "Generate a 5-second, 16:9 street dance shoe showcase video: using @Image1 as the shoe reference and @I`（1 次）
- `["wan3.0-video", "Generate a 5-second, 16:9 ultra-widescreen plush universe adventure clip: a spaceship crafted entirely`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
