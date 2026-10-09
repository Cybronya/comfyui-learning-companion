# iToolsPromptStyler

## 节点类型

`iToolsPromptStyler`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text_positive:STRING`（1 次）
- `text_negative:STRING`（1 次）
- `style_file:COMBO`（1 次）
- `template_name:COMBO`（1 次）

## 输出

- `positive_prompt:STRING`（1 次）
- `negative_prompt:STRING`（1 次）
- `used_template:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "basic.yaml", "Comic Book"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
