---
key: 图片生成/文生图/Flex.2无CN深度控制文生图工作流V1_1916415071411703809.json
name: Flex.2无CN深度控制文生图工作流V1_1916415071411703809.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flex.2无CN深度控制文生图工作流V1_1916415071411703809.json
hash: 9e6257fbe54cc838
coverage: 0.884615
learned_at: 2026-10-07 22:07:49
nodes: [Note Plus (mtb), DepthAnythingPreprocessor, DF_Get_image_size, CLIPTextEncode, CLIPTextEncode, UNETLoader, Flex2Conditioner, ApplyFBCacheOnModel, DualCLIPLoader, EmptyLatentImage, PreviewImage, VAELoader, GroundingDinoModelLoader (segment anything2), ImageScaleToTotalPixels, KSampler, VAEEncode, Flex2Conditioner, LoadImage, ImageScaleToTotalPixels, ImageConcanate, JWImageResizeByLongerSide, VAEDecode, SaveImage, SaveImage, JWImageResizeByLongerSide, ImageConcanate]
patterns: [text_to_image, image_to_image]
missing: [GroundingDinoModelLoader (segment anything2), Note Plus (mtb)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1256, "sampler_name": "deis", "scheduler": "beta", "seed": 726210541184116, "steps": 30, "width": 840}
discoveries: [次要节点 `GroundingDinoModelLoader (segment anything2)` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Flex.2无CN深度控制文生图工作流V1_1916415071411703809.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1916415071411703809.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `Note Plus (mtb)`
- `DepthAnythingPreprocessor`
- `DF_Get_image_size`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `Flex2Conditioner`
- `ApplyFBCacheOnModel`
- `DualCLIPLoader`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `VAELoader`
- `GroundingDinoModelLoader (segment anything2)`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `Flex2Conditioner`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageConcanate`
- `JWImageResizeByLongerSide`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `JWImageResizeByLongerSide`
- `ImageConcanate`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `840`
- `height` = `1256`
- `batch_size` = `1`
- `seed` = `726210541184116`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`DepthAnythingPreprocessor`、`DF_Get_image_size`、`CLIPTextEncode`、`UNETLoader`、`Flex2Conditioner`、`ApplyFBCacheOnModel`、`DualCLIPLoader`、`EmptyLatentImage`、`VAELoader`、`ImageScaleToTotalPixels`、`KSampler`、`VAEEncode`、`LoadImage`、`ImageConcanate`、`JWImageResizeByLongerSide`、`VAEDecode`、`SaveImage`

**缺卡**（2）：`GroundingDinoModelLoader (segment anything2)`、`Note Plus (mtb)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader、DepthAnythingPreprocessor

## 学习发现

- 次要节点 `GroundingDinoModelLoader (segment anything2)` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
