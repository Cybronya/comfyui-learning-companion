---
key: 图片生成/图生图/Flex.2局部二阶段重绘工作流V1_1916364099486154753.json
name: Flex.2局部二阶段重绘工作流V1_1916364099486154753
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flex.2局部二阶段重绘工作流V1_1916364099486154753.json
hash: 5ef4a8d5db6dc42b
coverage: 0.882353
learned_at: 2026-10-23 10:56:03
nodes: [PreviewImage, SAM2ModelLoader (segment anything2), DF_Get_image_size, Flex2Conditioner, CLIPTextEncode, CLIPTextEncode, UNETLoader, Flex2Conditioner, PreviewImage, VAEEncode, ApplyFBCacheOnModel, ImageScaleToTotalPixels, DualCLIPLoader, EmptyLatentImage, PreviewImage, VAELoader, SetLatentNoiseMask, GroundingDinoSAM2Segment (segment anything2), VAEDecode, GroundingDinoSAM2Segment (segment anything2), GroundingDinoModelLoader (segment anything2), SAM2ModelLoader (segment anything2), GroundingDinoModelLoader (segment anything2), PreviewImage, KSampler, EG_ZZ_SSKZ, LoadImage, VAEDecode, SaveImage, KSampler, ImageConcanate, ImageScaleToTotalPixels, DepthAnythingPreprocessor, SaveImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1256, "sampler_name": "deis", "scheduler": "beta", "seed": 726210541184116, "steps": 30, "width": 840}
---

# 图片生成/图生图/Flex.2局部二阶段重绘工作流V1_1916364099486154753.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flex.2局部二阶段重绘工作流V1_1916364099486154753.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `PreviewImage`
- `SAM2ModelLoader (segment anything2)`
- `DF_Get_image_size`
- `Flex2Conditioner`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `Flex2Conditioner`
- `PreviewImage`
- `VAEEncode` ★核心
- `ApplyFBCacheOnModel`
- `ImageScaleToTotalPixels`
- `DualCLIPLoader`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `VAELoader`
- `SetLatentNoiseMask`
- `GroundingDinoSAM2Segment (segment anything2)`
- `VAEDecode` ★核心
- `GroundingDinoSAM2Segment (segment anything2)`
- `GroundingDinoModelLoader (segment anything2)`
- `SAM2ModelLoader (segment anything2)`
- `GroundingDinoModelLoader (segment anything2)`
- `PreviewImage`
- `KSampler` ★核心
- `EG_ZZ_SSKZ`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `DepthAnythingPreprocessor`
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

覆盖率 **88%**（30/34）

**有卡**：`SAM2ModelLoader (segment anything2)`、`DF_Get_image_size`、`Flex2Conditioner`、`CLIPTextEncode`、`UNETLoader`、`VAEEncode`、`ApplyFBCacheOnModel`、`ImageScaleToTotalPixels`、`DualCLIPLoader`、`EmptyLatentImage`、`VAELoader`、`SetLatentNoiseMask`、`GroundingDinoSAM2Segment (segment anything2)`、`VAEDecode`、`GroundingDinoModelLoader (segment anything2)`、`KSampler`、`EG_ZZ_SSKZ`、`LoadImage`、`SaveImage`、`ImageConcanate`、`DepthAnythingPreprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader、DepthAnythingPreprocessor
