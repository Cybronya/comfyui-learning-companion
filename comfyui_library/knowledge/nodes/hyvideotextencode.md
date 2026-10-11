# HyVideoTextEncode

## 节点类型

`HyVideoTextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text_encoders:HYVIDTEXTENCODER`（1 次）
- `custom_prompt_template:PROMPT_TEMPLATE`（1 次）
- `clip_l:CLIP`（1 次）
- `hyvid_cfg:HYVID_CFG`（1 次）
- `model_to_offload:HYVIDEOMODEL`（1 次）
- `prompt:STRING`（1 次）
- `force_offload:BOOLEAN`（1 次）
- `prompt_template:COMBO`（1 次）

## 输出

- `hyvid_embeds:HYVIDEMBEDS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["女孩微笑着，慢慢戴上了眼镜", true, "video"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
