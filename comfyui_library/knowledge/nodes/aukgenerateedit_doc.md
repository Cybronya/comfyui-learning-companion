# AuKGenerateEdit_Doc

## 节点类型

`AuKGenerateEdit_Doc`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `engine:AUK_ENGINE_Doc`（4 次）
- `input_audio:AUDIO`（4 次）
- `llm_config:AUK_LLM_CONFIG_Doc`（4 次）
- `instruction:STRING`（4 次）
- `generation_seconds:FLOAT`（4 次）
- `use_prompt_enhancer:BOOLEAN`（4 次）
- `seed:INT`（4 次）
- `nfe_steps:INT`（4 次）
- `cfg_strength:FLOAT`（4 次）
- `sway_sampling_coef:FLOAT`（4 次）

## 输出

- `generated audio:AUDIO`（4 次）
- `model instruction:STRING`（4 次）
- `Prompt Enhancer info:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Generate speech based on the following description: \"A calm, warm female voice with a clear, moderate pace\". The con`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
