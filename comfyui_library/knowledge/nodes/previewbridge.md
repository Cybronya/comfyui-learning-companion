# PreviewBridge

## 节点类型

`PreviewBridge`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `images:IMAGE`（3 次）
- `image:STRING`（3 次）
- `block:BOOLEAN`（3 次）
- `restore_mask:COMBO`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）
- `MASK:MASK`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["$319-0", {"filename": "clipspace-paint-7358498.png", "subfolder": "clipspace", "type": "input"}, "never"]`（2 次）
- `["$-1-0", {"filename": "clipspace-paint-7358498.png", "subfolder": "clipspace", "type": "input"}, "never"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
