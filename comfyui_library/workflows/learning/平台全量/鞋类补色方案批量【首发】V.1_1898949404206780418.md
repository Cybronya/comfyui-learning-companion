---
key: 平台全量/鞋类补色方案批量【首发】V.1_1898949404206780418.json
name: 鞋类补色方案批量【首发】V.1_1898949404206780418
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/鞋类补色方案批量【首发】V.1_1898949404206780418.json
hash: 4ded5261a00f4416
coverage: 0.681159
learned_at: 2026-11-14 02:50:16
nodes: [ControlNetApplySD3, PreviewImage, ControlNetApplySD3, Canny, ControlNetLoader, CLIPTextEncode, CLIPTextEncode, CLIPSetLastLayer, GetNode, DepthAnythingV2Preprocessor, GetNode, GetNode, GetNode, Text Concatenate, SetNode, SetNode, String, LoadImage, SetNode, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, LayerMask: MaskGrow, String, KSampler, Get Image Size, EmptyLatentImage, VAEDecode, Anything Everywhere3, LayerStyle: ColorOverlay V2, GetNode, SetNode, TTP_Image_Tile_Batch, SamplerCustomAdvanced, ImageListToImageBatch, easy imageBatchToImageList, VAEDecodeTiled, RandomNoise, SetNode, SetNode, SetNode, InspyrenetRembg, TTP_Image_Assy, ControlNetLoader, PreviewImage, Int, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), ImageUpscaleWithModel, ImageScaleToTotalPixels, Joy_caption_two_load, Joy_caption_two, TTP_Tile_image_size, CLIPTextEncode, FluxGuidance, BasicGuider, UpscaleModelLoader, GetNode, UNETLoader, VAEEncode, BasicScheduler, KSamplerSelect, GetNode, CheckpointLoaderSimple, Note, PreviewImage, SaveImage, PreviewImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7.49, "checkpoint": "majicmixRealistic_v7.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 934712048287, "steps": 30, "width": 512}
---

# 平台全量/鞋类补色方案批量【首发】V.1_1898949404206780418.json

> 来源文件 `comfyui_library/workflows/平台全量/鞋类补色方案批量【首发】V.1_1898949404206780418.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `ControlNetApplySD3` ★核心
- `PreviewImage`
- `ControlNetApplySD3` ★核心
- `Canny`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPSetLastLayer`
- `GetNode`
- `DepthAnythingV2Preprocessor`
- `GetNode`
- `GetNode`
- `GetNode`
- `Text Concatenate`
- `SetNode`
- `SetNode`
- `String`
- `LoadImage`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LayerMask: MaskGrow`
- `String`
- `KSampler` ★核心
- `Get Image Size`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `Anything Everywhere3`
- `LayerStyle: ColorOverlay V2`
- `GetNode`
- `SetNode`
- `TTP_Image_Tile_Batch`
- `SamplerCustomAdvanced` ★核心
- `ImageListToImageBatch`
- `easy imageBatchToImageList`
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `SetNode`
- `SetNode`
- `SetNode`
- `InspyrenetRembg`
- `TTP_Image_Assy`
- `ControlNetLoader`
- `PreviewImage`
- `Int`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `Joy_caption_two_load`
- `Joy_caption_two`
- `TTP_Tile_image_size`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `BasicGuider`
- `UpscaleModelLoader`
- `GetNode`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `934712048287`
- `steps` = `30`
- `cfg` = `7.49`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `checkpoint` = `majicmixRealistic_v7.safetensors`

## 知识

覆盖率 **68%**（47/69）

**有卡**：`ControlNetApplySD3`、`Canny`、`ControlNetLoader`、`CLIPTextEncode`、`CLIPSetLastLayer`、`DepthAnythingV2Preprocessor`、`Text Concatenate`、`String`、`LoadImage`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`、`LayerMask: MaskGrow`、`KSampler`、`Get Image Size`、`EmptyLatentImage`、`VAEDecode`、`LayerStyle: ColorOverlay V2`、`TTP_Image_Tile_Batch`、`SamplerCustomAdvanced`、`ImageListToImageBatch`、`easy imageBatchToImageList`、`VAEDecodeTiled`、`RandomNoise`、`InspyrenetRembg`、`TTP_Image_Assy`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`Joy_caption_two_load`、`Joy_caption_two`、`TTP_Tile_image_size`、`FluxGuidance`、`BasicGuider`、`UpscaleModelLoader`、`UNETLoader`、`VAEEncode`、`BasicScheduler`、`KSamplerSelect`、`CheckpointLoaderSimple`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、EmptyLatentImage
