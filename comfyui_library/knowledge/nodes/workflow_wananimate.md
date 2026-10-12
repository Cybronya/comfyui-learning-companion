# workflow>wanAnimate 采样

## 节点类型

`workflow>wanAnimate 采样`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `t5:WANTEXTENCODER`（16 次）
- `model:WANVIDEOMODEL`（16 次）
- `image_embeds:WANVIDIMAGE_EMBEDS`（16 次）
- `vae:WANVAE`（16 次）
- `positive_prompt:STRING`（16 次）
- `negative_prompt:STRING`（16 次）
- `force_offload:BOOLEAN`（16 次）
- `use_disk_cache:BOOLEAN`（16 次）
- `device:COMBO`（16 次）
- `steps:INT`（16 次）

## 输出

- `图像:IMAGE`（16 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["帮我把视频中的人物替换成图片中的人物", "色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的`（14 次）
- `["帮我把视频中的人物替换成图片中的人物", "色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，画得不好的手部，画得不好的脸部，畸形的，毁容的`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
