# TextGenerateLTX2Prompt

## 节点类型

`TextGenerateLTX2Prompt`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 17 个 workflow 中。

## 输入

- `clip:CLIP`（23 次）
- `image:IMAGE`（23 次）
- `video:IMAGE`（23 次）
- `audio:AUDIO`（23 次）
- `prompt:STRING`（23 次）
- `max_length:INT`（23 次）
- `sampling_mode:COMFY_DYNAMICCOMBO_V3`（23 次）
- `sampling_mode.temperature:FLOAT`（23 次）
- `sampling_mode.top_k:INT`（23 次）
- `sampling_mode.top_p:FLOAT`（23 次）

## 输出

- `generated_text:STRING`（23 次）
- `thinking:STRING`（20 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 512, "on", 0.7, 64, 0.95, 0.05, 1.05, 999, 0, false, false, "auto"]`（6 次）
- `["参照图片风格构图以及色彩生成一张巨大的中式古代宫殿的图片", 512, "on", 0.7, 64, 0.95, 0.05, 1.05, 666, 0, false, false, "auto"]`（4 次）
- `["aijuxi", 512, "on", 0.7, 64, 0.95, 0.05, 1.05, 666, 0, false, false, "auto"]`（3 次）
- `["让图1的人物穿上图2的整套搭配，包括耳环，衣服，裤子，包，墨镜，项链，靴子。", 512, "on", 0.7, 64, 0.95, 0.04000000000000001, 1.05, 666, 0, false, false, "a`（2 次）
- `["", 1024, "on", 0.7, 64, 0.95, 0.05, 1.05, 0, 0, false, false, "auto"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
