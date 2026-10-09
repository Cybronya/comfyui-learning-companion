# TextSplitByDelimiterEnhanced

## 节点类型

`TextSplitByDelimiterEnhanced`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `外部文本列表:STRING`（2 次）
- `输入来源:COMBO`（2 次）
- `输入文本:STRING`（2 次）
- `分隔符:STRING`（2 次）
- `使用正则表达式:BOOLEAN`（2 次）
- `输出段落索引:INT`（2 次）
- `输出列表索引:INT`（2 次）
- `总列表段落选择:INT`（2 次）

## 输出

- `总列表:STRING`（2 次）
- `选中列表的完整分割:STRING`（2 次）
- `选中段落:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["文本框", "", "===SPLIT===", false, 1, 1, 0]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
