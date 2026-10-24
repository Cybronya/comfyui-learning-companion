# DapaoPromptBrakeNode

## 节点类型

`DapaoPromptBrakeNode`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `text:STRING`（8 次）
- `⏱️ 超时时间(秒):INT`（8 次）

## 输出

- `📝 最终提示词:STRING`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[null, "", null, 60]`（8 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
