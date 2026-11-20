# Yuan_MiniMaxH3RefEmbeds

## 节点类型

`Yuan_MiniMaxH3RefEmbeds`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `vae:VAE`（1 次）
- `audio_vae:VAE`（1 次）
- `ref_images:IMAGE`（1 次）
- `ref_video_1:IMAGE`（1 次）
- `ref_video_2:IMAGE`（1 次）
- `ref_video_audio_1:AUDIO`（1 次）
- `ref_video_audio_2:AUDIO`（1 次）
- `ref_audio_1:AUDIO`（1 次）
- `ref_image_size:COMBO`（1 次）
- `match_width:INT`（1 次）

## 输出

- `参考嵌入:MINIMAXH3_REFS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["匹配", 1344, 768, "磁盘", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
