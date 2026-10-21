# SynVowPromptTransparentAssetPromptGenerator

## 节点类型

`SynVowPromptTransparentAssetPromptGenerator`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `llm_config:SYNVOW_LLM_CONFIG`（3 次）
- `product_or_reference_image:IMAGE`（3 次）
- `style_reference_image:IMAGE`（3 次）
- `scene_preset:COMBO`（3 次）
- `planner_mode:COMBO`（3 次）
- `asset_count:COMBO`（3 次）
- `custom_prompt:STRING`（3 次）
- `model:COMBO`（3 次）
- `seed:INT`（3 次）

## 输出

- `prompts_list:STRING`（3 次）
- `asset_plan_json:STRING`（3 次）
- `prompts_text:STRING`（3 次）
- `status:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["参考图分层拆图", "自动规划(LLM)", "4", "", "gemini-3.1-pro-preview", 1054871277, "randomize"]`（1 次）
- `["游戏道具素材", "自动规划(LLM)", "8", "", "gemini-3.1-pro-preview", 309225228, "randomize"]`（1 次）
- `["人物/IP贴纸", "自动规划(LLM)", "2", "原创圆形表情贴纸，包含开心、疑问、点赞、比心", "google/gemini-3.1-pro-preview", 1404083569, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
