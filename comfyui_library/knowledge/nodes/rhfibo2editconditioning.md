# RHFibo2EditConditioning

## 节点类型

`RHFibo2EditConditioning`

## 分类

Conditioning

## 作用

条件处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 9 个 workflow 中。

## 输入

- `clip:CLIP`（9 次）
- `vae:VAE`（9 次）
- `images.image_0:IMAGE`（9 次）
- `images.image_1:IMAGE`（9 次）
- `mask:MASK`（9 次）
- `prompt:STRING`（9 次）
- `width:INT`（9 次）
- `height:INT`（9 次）
- `render_text_images:BOOLEAN`（9 次）
- `images.image_2:IMAGE`（4 次）

## 输出

- `条件:CONDITIONING`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["参考<Image-1>的人物，参考<Image-2>的背景，把<Image-1>中的人物和<Image-2>融合，保持<Image-1>人物服装发型人脸不变，光影融合自然", 1024, 1024, true]`（4 次）
- `["把主体衣服改成红色，保持构图和背景不变。", 1024, 1024, true]`（4 次）
- `["", 1024, 1024, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
