# MOSSImagePromptEnhancerT8

## 节点类型

`MOSSImagePromptEnhancerT8`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `reference_images.reference_image_0:IMAGE`（1 次）
- `api_key:STRING`（1 次）
- `provider_config:T8_LLM_PROVIDER_CONFIG`（1 次）
- `prompt:STRING`（1 次）
- `operation:COMBO`（1 次）
- `output_format:COMBO`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `output_language:COMBO`（1 次）
- `api_mode:COMBO`（1 次）

## 输出

- `正向提示词 / positive_prompt:STRING`（1 次）
- `宽 / width:INT`（1 次）
- `高 / height:INT`（1 次）
- `实际格式 / resolved_format:STRING`（1 次）
- `可编辑草稿 / draft_json:STRING`（1 次）
- `诊断报告 / report_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "生成 / Generate", "AUTO / 自动", 1024, 1024, "按需求（默认英文）/ Auto", "贞贞平价小屋（推荐）", "", 0, 1, 16384, "", "gemini-3.5-flash",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
