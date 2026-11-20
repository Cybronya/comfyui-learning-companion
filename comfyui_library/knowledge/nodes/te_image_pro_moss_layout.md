# TE_image_pro_moss_layout

## 节点类型

`TE_image_pro_moss_layout`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `prompt:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `完整版式提示词:STRING`（1 次）
- `元素列表:STRING`（1 次）
- `版式预览图:IMAGE`（1 次）
- `描述:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["CLIP", "街上一个女人", "竖版海报", 1024, 1536, 6016, 233698290936851, "randomize", "中文", "qwen3.8\\Qwen3.8-27B-Uncensored-0bserv`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
