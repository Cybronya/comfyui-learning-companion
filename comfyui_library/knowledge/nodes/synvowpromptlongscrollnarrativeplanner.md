# SynVowPromptLongScrollNarrativePlanner

## 节点类型

`SynVowPromptLongScrollNarrativePlanner`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `产品图_1:IMAGE`（2 次）
- `llm_config:SYNVOW_LLM_CONFIG`（2 次）
- `产品图_2:IMAGE`（2 次）
- `产品图_3:IMAGE`（2 次）
- `产品图_4:IMAGE`（2 次）
- `参考图_1:IMAGE`（2 次）
- `参考图_2:IMAGE`（2 次）
- `参考图_3:IMAGE`（2 次）
- `参考图_4:IMAGE`（2 次）
- `模型:COMBO`（2 次）

## 输出

- `叙事结构_JSON:STRING`（2 次）
- `长卷视觉母版说明:STRING`（2 次）
- `叙事结构_Markdown:STRING`（2 次）
- `生成状态:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["google/gemini-3.5-flash", "趣脆巧克力豆曲奇", "曲奇饼干", "", 8, 1000, "fixed", 0.3]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
