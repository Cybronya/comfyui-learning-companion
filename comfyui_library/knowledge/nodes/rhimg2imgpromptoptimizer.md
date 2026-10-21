# RHImg2ImgPromptOptimizer

## 节点类型

`RHImg2ImgPromptOptimizer`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `reference_image:IMAGE`（3 次）
- `llm_config:SYNVOW_LLM_CONFIG`（3 次）
- `subject_image:IMAGE`（3 次）
- `user_prompt:STRING`（3 次）
- `model:COMBO`（3 次）
- `reference_mode:COMBO`（3 次）
- `target_aspect_ratio:COMBO`（3 次）
- `seed:INT`（3 次）

## 输出

- `optimized_prompt:STRING`（3 次）
- `reference_summary:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "google/gemini-3.1-pro-preview", "综合参考", "16:9", 660171651, "randomize"]`（1 次）
- `["", "google/gemini-3.1-pro-preview", "综合参考", "16:9", 1002310025, "randomize"]`（1 次）
- `["", "google/gemini-3.1-pro-preview", "自动判断", "auto", 1633657653, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
