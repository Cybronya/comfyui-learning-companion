# T5GEMMATextEncoder

## 节点类型

`T5GEMMATextEncoder`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `llm_model:LLM_MODEL`（2 次）
- `llm_tokenizer:LLM_TOKENIZER`（2 次）
- `text:STRING`（2 次）
- `max_length:INT`（2 次）
- `device:COMBO`（2 次）
- `dtype:COMBO`（2 次）

## 输出

- `hidden_states:LLM_HIDDEN_STATES`（2 次）
- `attention_mask:LLM_ATTENTION_MASK`（2 次）
- `info:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["lowres, bad anatomy,  text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, no`（1 次）
- `["1girl, solo, long_hair, looking_at_viewer, blush, blue_eyes, skirt, blonde_hair, hat, holding, ribbon, twintails, unde`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
