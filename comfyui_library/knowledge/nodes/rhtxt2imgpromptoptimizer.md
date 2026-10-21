# RHTxt2ImgPromptOptimizer

## 节点类型

`RHTxt2ImgPromptOptimizer`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `llm_config:SYNVOW_LLM_CONFIG`（1 次）
- `user_prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `layout_type:COMBO`（1 次）
- `text_policy:COMBO`（1 次）
- `optimize_strength:COMBO`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `seed:INT`（1 次）
- `exact_text:STRING`（1 次）

## 输出

- `optimized_prompt:STRING`（1 次）
- `debug_info:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "google/gemini-3.1-pro-preview", "图文混排海报", "自动生成", "增强", "9:16", 1774760343, "randomize", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
