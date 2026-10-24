# ZML_TextFormatter

## 节点类型

`ZML_TextFormatter`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `文本:STRING`（4 次）
- `权重转换:COMBO`（4 次）
- `文本格式化:COMBO`（4 次）
- `格式化标点符号:BOOLEAN`（4 次）
- `合并相同提示词:BOOLEAN`（4 次）
- `合并白名单:STRING`（4 次）

## 输出

- `文本:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "禁用", "下划线转空格", true, true, ""]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
