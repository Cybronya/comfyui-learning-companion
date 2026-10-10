# WanVideoSVIProEmbeds

## 节点类型

`WanVideoSVIProEmbeds`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `anchor_samples:LATENT`（4 次）
- `prev_samples:LATENT`（4 次）
- `num_frames:INT`（4 次）
- `motion_latent_count:INT`（4 次）

## 输出

- `image_embeds:WANVIDIMAGE_EMBEDS`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[81, 1]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
