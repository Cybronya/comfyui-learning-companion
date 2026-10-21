# SynVowTransparentAssetPromptGenerator

## 节点类型

`SynVowTransparentAssetPromptGenerator`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `llm_config:SYNVOW_LLM_CONFIG`（2 次）
- `product_or_reference_image:IMAGE`（2 次）
- `style_reference_image:IMAGE`（2 次）
- `scene_preset:COMBO`（2 次）
- `planner_mode:COMBO`（2 次）
- `asset_count:COMBO`（2 次）
- `layer_count:COMBO`（2 次）
- `custom_prompt:STRING`（2 次）
- `model:COMBO`（2 次）
- `seed:INT`（2 次）

## 输出

- `prompts_list:STRING`（2 次）
- `asset_plan_json:STRING`（2 次）
- `prompts_text:STRING`（2 次）
- `status:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["参考图分层拆图", "自动规划(LLM)", "2", "4", "", "google/gemini-3.6-flash", 412600701, "randomize", "国内站 (.cn)"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
