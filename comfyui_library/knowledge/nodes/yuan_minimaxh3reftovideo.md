# Yuan_MiniMaxH3RefToVideo

## 节点类型

`Yuan_MiniMaxH3RefToVideo`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `refs:MINIMAXH3_REFS`（1 次）
- `prompt:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `length:INT`（1 次）

## 输出

- `正向:CONDITIONING`（1 次）
- `潜空间:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 1344, 768, 124]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
