# BatchPromptSchedule

## 节点类型

`BatchPromptSchedule`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `text:STRING`（1 次）
- `pre_text:STRING`（1 次）
- `app_text:STRING`（1 次）

## 输出

- `POS:CONDITIONING`（1 次）
- `NEG:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["\"0\" :\"4-year-old,litte baby，kawaii,short hair \",\n\"1\" :\"14-year-old,cute kid,short hair \",\n\"2\" :\"24-year-o`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
