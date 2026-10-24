---
key: 图片生成/图生图/视频首帧Flex.2深度替换图_1924671178982813697.json
name: 视频首帧Flex.2深度替换图_1924671178982813697
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/视频首帧Flex.2深度替换图_1924671178982813697.json
hash: 3fdde820b0e5a551
coverage: 0.961538
learned_at: 2026-10-23 13:26:09
nodes: [Note Plus (mtb), DepthAnythingPreprocessor, DF_Get_image_size, CLIPTextEncode, UNETLoader, Flex2Conditioner, ApplyFBCacheOnModel, DualCLIPLoader, PreviewImage, VAELoader, ImageScaleToTotalPixels, KSampler, VAEEncode, Flex2Conditioner, ImageScaleToTotalPixels, ImageConcanate, JWImageResizeByLongerSide, VAEDecode, SaveImage, JWImageResizeByLongerSide, ImageConcanate, CLIPTextEncode, EmptyLatentImage, VHS_LoadVideo, ImageFromBatch+, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1256, "sampler_name": "deis", "scheduler": "beta", "seed": 726210541184116, "steps": 30, "width": 840}
---

# 图片生成/图生图/视频首帧Flex.2深度替换图_1924671178982813697.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/视频首帧Flex.2深度替换图_1924671178982813697.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `Note Plus (mtb)`
- `DepthAnythingPreprocessor`
- `DF_Get_image_size`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `Flex2Conditioner`
- `ApplyFBCacheOnModel`
- `DualCLIPLoader`
- `PreviewImage`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `Flex2Conditioner`
- `ImageScaleToTotalPixels`
- `ImageConcanate`
- `JWImageResizeByLongerSide`
- `VAEDecode` ★核心
- `SaveImage`
- `JWImageResizeByLongerSide`
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `VHS_LoadVideo`
- `ImageFromBatch+`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `726210541184116`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `840`
- `height` = `1256`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`Note Plus (mtb)`、`DepthAnythingPreprocessor`、`DF_Get_image_size`、`CLIPTextEncode`、`UNETLoader`、`Flex2Conditioner`、`ApplyFBCacheOnModel`、`DualCLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`KSampler`、`VAEEncode`、`ImageConcanate`、`JWImageResizeByLongerSide`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`VHS_LoadVideo`、`ImageFromBatch+`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、UNETLoader、DepthAnythingPreprocessor、VAEEncode
