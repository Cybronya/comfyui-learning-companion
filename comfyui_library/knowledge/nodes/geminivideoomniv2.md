# GeminiVideoOmniV2

## 节点类型

`GeminiVideoOmniV2`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `model.images.image_1:IMAGE`（8 次）
- `model.videos.video_1:VIDEO`（8 次）
- `model.videos.video_2:VIDEO`（3 次）
- `model.images.image_2:IMAGE`（3 次）
- `model.images.image_3:IMAGE`（2 次）
- `model.prompt:STRING`（2 次）

## 输出

- `VIDEO:VIDEO`（8 次）
- `STRING:STRING`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Omni Flash", "", "16:9", "auto", 1, 0.95, 42, "randomize", "randomize"]`（2 次）
- `["Omni Flash 1.1", "Change the character in the video to a walking human‑shaped cactus", "720p", "16:9", "edit", 1228915`（1 次）
- `["Omni Flash 1.1", "Continue the scene: cut to a new shot at the edge of town, the two roosters taking a dust bath toget`（1 次）
- `["Omni Flash 1.1", "Use @Image1 as the first frame, keep the car and the blue studio set exactly unchanged in the openin`（1 次）
- `["Omni Flash 1.1", "[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]\nA luxury eyeshadow commercial. The woman i`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
