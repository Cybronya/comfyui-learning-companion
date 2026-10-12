# HyVideoI2VEncode

## 节点类型

`HyVideoI2VEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 13 个 workflow 中。

## 输入

- `text_encoders:HYVIDTEXTENCODER`（14 次）
- `clip_l:CLIP`（14 次）
- `image:IMAGE`（14 次）
- `hyvid_cfg:HYVID_CFG`（14 次）
- `prompt:STRING`（10 次）
- `model_to_offload:HYVIDEOMODEL`（1 次）

## 输出

- `hyvid_embeds:HYVIDEMBEDS`（14 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["镜头推近，国漫女神眨眼微笑", true, "I2V_video", 4]`（2 次）
- `["", true, "I2V_video", 4, [false, true]]`（2 次）
- `["男子手持闪电链，向前奔跑", true, "I2V_video", 2]`（1 次）
- `["chibi figurine dances", true, "I2V_video"]`（1 次）
- `["1 girl is smiling", true, "I2V_video"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
