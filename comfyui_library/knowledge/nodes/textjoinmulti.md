# TextJoinMulti

## 节点类型

`TextJoinMulti`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `text1:STRING`（4 次）
- `text2:STRING`（4 次）
- `text3:STRING`（4 次）
- `text4:STRING`（4 次）
- `text5:STRING`（4 次）
- `separator:STRING`（4 次）
- `input:STRING`（4 次）

## 输出

- `string:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["editpicforgood,Only modify the requested content, and try to keep the rest of the image unchanged as much as possible,`（2 次）
- `["editpicforpartV1,Only modify the requested content, and try to keep the rest of the image unchanged as much as possibl`（1 次）
- `["editpicforgood,", "", "", "", "", "\\n", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
