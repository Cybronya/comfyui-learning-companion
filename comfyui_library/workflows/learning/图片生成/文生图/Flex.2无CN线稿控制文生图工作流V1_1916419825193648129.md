---
key: 图片生成/文生图/Flex.2无CN线稿控制文生图工作流V1_1916419825193648129.json
name: Flex.2无CN线稿控制文生图工作流V1_1916419825193648129.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flex.2无CN线稿控制文生图工作流V1_1916419825193648129.json
hash: d4be588e415750ee
coverage: 0.884615
learned_at: 2026-10-07 22:07:50
nodes: [DF_Get_image_size, CLIPTextEncode, CLIPTextEncode, UNETLoader, Flex2Conditioner, ApplyFBCacheOnModel, DualCLIPLoader, EmptyLatentImage, VAELoader, GroundingDinoModelLoader (segment anything2), KSampler, VAEEncode, Flex2Conditioner, ImageScaleToTotalPixels, ImageConcanate, VAEDecode, SaveImage, JWImageResizeByLongerSide, ImageConcanate, Note Plus (mtb), PreviewImage, JWImageResizeByLongerSide, ImageScaleToTotalPixels, AnyLineArtPreprocessor_aux, LoadImage, SaveImage]
patterns: [text_to_image, image_to_image]
missing: [GroundingDinoModelLoader (segment anything2), Note Plus (mtb)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1256, "sampler_name": "deis", "scheduler": "beta", "seed": 726210541184116, "steps": 30, "width": 840}
discoveries: [次要节点 `GroundingDinoModelLoader (segment anything2)` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Flex.2无CN线稿控制文生图工作流V1_1916419825193648129.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1916419825193648129.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `DF_Get_image_size`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `Flex2Conditioner`
- `ApplyFBCacheOnModel`
- `DualCLIPLoader`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `GroundingDinoModelLoader (segment anything2)`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `Flex2Conditioner`
- `ImageScaleToTotalPixels`
- `ImageConcanate`
- `VAEDecode` ★核心
- `SaveImage`
- `JWImageResizeByLongerSide`
- `ImageConcanate`
- `Note Plus (mtb)`
- `PreviewImage`
- `JWImageResizeByLongerSide`
- `ImageScaleToTotalPixels`
- `AnyLineArtPreprocessor_aux`
- `LoadImage`
- `SaveImage`

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

**有卡**：`DF_Get_image_size`、`CLIPTextEncode`、`UNETLoader`、`Flex2Conditioner`、`ApplyFBCacheOnModel`、`DualCLIPLoader`、`EmptyLatentImage`、`VAELoader`、`KSampler`、`VAEEncode`、`ImageScaleToTotalPixels`、`ImageConcanate`、`VAEDecode`、`SaveImage`、`JWImageResizeByLongerSide`、`AnyLineArtPreprocessor_aux`、`LoadImage`

**缺卡**（2）：`GroundingDinoModelLoader (segment anything2)`、`Note Plus (mtb)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader、VAEEncode

## 学习发现

- 次要节点 `GroundingDinoModelLoader (segment anything2)` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
