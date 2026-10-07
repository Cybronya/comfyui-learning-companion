# KlingOmniProImageToVideoNode

## 节点类型

`KlingOmniProImageToVideoNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `reference_images:IMAGE`（3 次）
- `aspect_ratio:COMBO`（1 次）
- `storyboards.storyboard_1_prompt:STRING`（1 次）
- `storyboards.storyboard_2_prompt:STRING`（1 次）
- `storyboards.storyboard_3_prompt:STRING`（1 次）

## 输出

- `VIDEO:VIDEO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["kling-v3-omni", "Wide shot of a free‑spirited young woman running toward the camera through a sun‑drenched field, whit`（1 次）
- `["kling-video-o1", "An indoor scene at night where the quokka in a white bathrobe sits by a window, looking out at the s`（1 次）
- `["kling-v3-omni", "", "9:16", 12, "720p", "3 storyboards", "", 4, "", 4, "", 4, true, 205346978, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
