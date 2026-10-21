# FeishuTextEditorNode

## 节点类型

`FeishuTextEditorNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `输入文本:STRING`（5 次）
- `删除前面条件:STRING`（5 次）
- `删除后面条件:STRING`（5 次）
- `保留关键词:BOOLEAN`（5 次）

## 输出

- `输出文本:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "***(", ")***&", false]`（3 次）
- `["", "[", "]", false]`（1 次）
- `["", "&文本***(", ")***&", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
