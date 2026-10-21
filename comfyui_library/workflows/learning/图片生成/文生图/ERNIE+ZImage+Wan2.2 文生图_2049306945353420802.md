---
key: 图片生成/文生图/ERNIE+ZImage+Wan2.2 文生图_2049306945353420802.json
name: ERNIE+ZImage+Wan2.2 文生图_2049306945353420802
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ERNIE+ZImage+Wan2.2 文生图_2049306945353420802.json
hash: b8a7d9bf12fd083a
coverage: 0.813333
learned_at: 2026-10-21 02:51:31
nodes: [CLIPLoader, CLIPTextEncode, CLIPTextEncode, KSampler, Note, INTConstant, CLIPLoader, CLIPTextEncode, CLIPTextEncode, UNETLoader, VAEEncode, INTConstant, Note, INTConstant, Note, INTConstant, INTConstant, INTConstant, Note, Note, Note, VAELoader, CR Text, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, ModelSamplingSD3, VAELoader, VAEDecode, RH_LLMAPI_Pro_Node, RH_LLMAPI_NODE, easy showAnything, InversionDemoLazyIndexSwitch, CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSamplerAdvanced, VAEEncode, VAEDecode, KSamplerAdvanced, VAEDecode, PreviewImage, PreviewImage, ImageScaleBy, ConstrainImage|pysssss, TTP_Tile_image_size, ImageResize+, Get Image Size, TTP_Image_Tile_Batch, Image Comparer (rgthree), TTP_Image_Assy, ImageScaleBy, Note, easy imageSize, Get Image Size, easy imageSize, easy imageSize, Note, easy imageSize, ImageResize+, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, EmptyLatentImage, LayerColor: Brightness & Contrast, Fast Groups Bypasser (rgthree), SaveImage, Note, INTConstant, SaveImage, CR Text]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 2, "cfg": 8, "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 960}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/ERNIE+ZImage+Wan2.2 文生图_2049306945353420802.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ERNIE+ZImage+Wan2.2 文生图_2049306945353420802.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `Note`
- `INTConstant`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `INTConstant`
- `Note`
- `INTConstant`
- `Note`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Note`
- `Note`
- `Note`
- `VAELoader`
- `CR Text`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `VAEDecode` ★核心
- `RH_LLMAPI_Pro_Node`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `InversionDemoLazyIndexSwitch`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `PreviewImage`
- `ImageScaleBy`
- `ConstrainImage|pysssss`
- `TTP_Tile_image_size`
- `ImageResize+`
- `Get Image Size`
- `TTP_Image_Tile_Batch`
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `ImageScaleBy`
- `Note`
- `easy imageSize`
- `Get Image Size`
- `easy imageSize`
- `easy imageSize`
- `Note`
- `easy imageSize`
- `ImageResize+`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `EmptyLatentImage` ★核心
- `LayerColor: Brightness & Contrast`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `Note`
- `INTConstant`
- `SaveImage`
- `CR Text`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `960`
- `height` = `1536`
- `batch_size` = `2`

## 知识

覆盖率 **81%**（61/75）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`KSampler`、`INTConstant`、`UNETLoader`、`VAEEncode`、`VAELoader`、`CR Text`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAEDecode`、`RH_LLMAPI_Pro_Node`、`RH_LLMAPI_NODE`、`InversionDemoLazyIndexSwitch`、`KSamplerAdvanced`、`ImageScaleBy`、`ConstrainImage|pysssss`、`TTP_Tile_image_size`、`ImageResize+`、`Get Image Size`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`easy imageSize`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`EmptyLatentImage`、`LayerColor: Brightness & Contrast`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
