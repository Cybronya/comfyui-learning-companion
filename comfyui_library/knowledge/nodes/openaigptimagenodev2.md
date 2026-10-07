# OpenAIGPTImageNodeV2

## 节点类型

`OpenAIGPTImageNodeV2`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 13 个 workflow 中。

## 输入

- `model.images.image_1:IMAGE`（14 次）
- `model.mask:MASK`（14 次）
- `model.images.image_2:IMAGE`（10 次）
- `model.images.image_3:IMAGE`（2 次）
- `prompt:STRING`（1 次）

## 输出

- `IMAGE:IMAGE`（14 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["dress a professional female model with the provided clothing items. Crucially, preserve ALL original material properti`（2 次）
- `["Keep the background environment, concrete walls, blue sky, sunlight, shadows, camera angle, framing and composition co`（1 次）
- `["1:1 square poster, an extreme close-up, high-contrast shot of a racing car front nose, aerodynamic wing and tire rim, `（1 次）
- `["Keep head, face, body, flowers, sweater, background, lighting unchanged. Only change hairstyle to retro bangs and make`（1 次）
- `["1:1 square editorial fashion poster, futuristic desert motorcycle rally scene. A rugged male biker with long dark hair`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
