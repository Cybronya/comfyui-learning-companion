# BerniniContextEmbeds

## 节点类型

`BerniniContextEmbeds`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:WANVAE`（1 次）
- `source_video:IMAGE`（1 次）
- `reference_video:IMAGE`（1 次）
- `reference_image_0:IMAGE`（1 次）
- `reference_image_1:IMAGE`（1 次）
- `reference_image_2:IMAGE`（1 次）
- `reference_image_3:IMAGE`（1 次）
- `reference_image_4:IMAGE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）
- `task_mode:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[832, 480, 121, 848, false, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
