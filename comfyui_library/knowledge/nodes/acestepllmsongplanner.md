# AceStepLLMSongPlanner

## 节点类型

`AceStepLLMSongPlanner`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `llama_model:LLAMACPPMODEL`（1 次）
- `source_lyrics:STRING`（1 次）
- `description:STRING`（1 次）
- `duration:FLOAT`（1 次）
- `language:COMBO`（1 次）
- `use_confirmed_prompt:BOOLEAN`（1 次）
- `approved_plan:STRING`（1 次）

## 输出

- `conditioning:CONDITIONING`（1 次）
- `duration:FLOAT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["悲壮轻音乐，萨克斯主奏", 60, "auto", false, "[PARAMS] Key=D minor | BPM=65 | Time=4/4 | Language=zh | Duration=60.0s\n\n[TAGS]\n无`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
