# AILab_QwenVL_PromptEnhancer

## 节点类型

`AILab_QwenVL_PromptEnhancer`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_name:COMBO`（1 次）
- `quantization:COMBO`（1 次）
- `attention_mode:COMBO`（1 次）
- `use_torch_compile:BOOLEAN`（1 次）
- `device:COMBO`（1 次）
- `prompt_text:STRING`（1 次）
- `enhancement_style:COMBO`（1 次）
- `custom_system_prompt:STRING`（1 次）
- `max_tokens:INT`（1 次）
- `temperature:FLOAT`（1 次）

## 输出

- `ENHANCED_OUTPUT:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen3-4B-Instruct-2507", "None (FP16)", "auto", false, "auto", "", "📝 Refine", "# MiniMax H3 提示词优化规则（给大模型用）\n\n你是 Mini`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
