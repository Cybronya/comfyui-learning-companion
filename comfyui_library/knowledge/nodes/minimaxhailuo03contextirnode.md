# MinimaxHailuo03ContextIRNode

## 节点类型

`MinimaxHailuo03ContextIRNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `first_frame:IMAGE`（6 次）
- `last_frame:IMAGE`（6 次）
- `model.prompt:STRING`（6 次）
- `model.reference_images.image_1:IMAGE`（6 次）
- `model.reference_videos.video_1:VIDEO`（6 次）
- `model.reference_audios.audio_1:AUDIO`（6 次）
- `model.reference_images.image_2:IMAGE`（2 次）

## 输出

- `STRING:STRING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["MiniMax H3", "", 5, "adaptive"]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
