# WanVideoPhantomEmbeds

## 节点类型

`WanVideoPhantomEmbeds`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `phantom_latent_1:LATENT`（1 次）
- `phantom_latent_2:LATENT`（1 次）
- `phantom_latent_3:LATENT`（1 次）
- `phantom_latent_4:LATENT`（1 次）
- `vace_embeds:WANVIDIMAGE_EMBEDS`（1 次）
- `num_frames:INT`（1 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[81, 5, 0, 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
