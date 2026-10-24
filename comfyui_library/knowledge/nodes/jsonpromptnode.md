# JsonPromptNode

## 节点类型

`JsonPromptNode`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `custom_text:STRING`（3 次）
- `enable_default_prompt:BOOLEAN`（3 次）
- `refresh_cache:BOOLEAN`（3 次）
- `透视图:COMBO`（3 次）
- `鸟瞰图:COMBO`（3 次）

## 输出

- `final_prompt:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", true, false, "None", "None"]`（2 次）
- `["", true, false, "03_黄昏透视01.json", "None"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
