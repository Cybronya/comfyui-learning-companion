# SplitAndExtractText

## 节点类型

`SplitAndExtractText`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `input_text:STRING`（3 次）
- `delimiter:STRING`（3 次）
- `index:INT`（3 次）
- `order:COMBO`（3 次）
- `include_delimiter:BOOLEAN`（3 次）

## 输出

- `STRING:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "【LTX-2视频提示词】", 1, "顺序", false]`（1 次）
- `["", "【LTX-2视频提示词】", 2, "顺序", false]`（1 次）
- `["", "【画面1首帧图提示词】", 2, "顺序", false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
