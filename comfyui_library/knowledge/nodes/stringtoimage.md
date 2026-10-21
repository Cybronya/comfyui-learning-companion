# StringToImage

## 节点类型

`StringToImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `colour:COLOR`（1 次）
- `background:COLOR`（1 次）

## 输出

- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Hello world!", 768, 1024, "white", "black"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
