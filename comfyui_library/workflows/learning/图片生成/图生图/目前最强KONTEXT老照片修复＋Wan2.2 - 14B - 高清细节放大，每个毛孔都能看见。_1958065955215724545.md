---
key: 图片生成/图生图/目前最强KONTEXT老照片修复＋Wan2.2 - 14B - 高清细节放大，每个毛孔都能看见。_1958065955215724545.json
name: 目前最强KONTEXT老照片修复＋Wan2.2 - 14B - 高清细节放大，每个毛孔都能看见。_1958065955215724545
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/目前最强KONTEXT老照片修复＋Wan2.2 - 14B - 高清细节放大，每个毛孔都能看见。_1958065955215724545.json
hash: af87485778862175
coverage: 0.953488
learned_at: 2026-10-23 13:18:21
nodes: [easy cleanGpuUsed, ImageScaleToTotalPixels, TTP_Tile_image_size, TTP_Image_Tile_Batch, ImageStitch, VAEEncode, KSampler, VAELoader, FluxKontextImageScale, UNETLoader, DualCLIPLoader, ConditioningZeroOut, Text Multiline, CLIPTextEncode, FluxGuidance, ImageConcatMulti, VAEDecode, LoraLoaderModelOnly, SaveImage, VAEEncode, VAEDecode, ReferenceLatent, ShowText|pysssss, TTP_Image_Assy, easy imageBatchToImageList, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, KSampler, ImageListToImageBatch, easy imageToBase64, YANC.ConcatStrings, ShellAgentPluginOutputText, UNETLoader, LoraLoaderModelOnly, ConstrainImage|pysssss, SaveImage, ImageUpscaleWithModel, UpscaleModelLoader, VAELoader, CLIPLoader, Image Comparer (rgthree), LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 223181603622468, "steps": 10}
---

# 图片生成/图生图/目前最强KONTEXT老照片修复＋Wan2.2 - 14B - 高清细节放大，每个毛孔都能看见。_1958065955215724545.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/目前最强KONTEXT老照片修复＋Wan2.2 - 14B - 高清细节放大，每个毛孔都能看见。_1958065955215724545.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `easy cleanGpuUsed`
- `ImageScaleToTotalPixels`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `ImageStitch`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `FluxKontextImageScale`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `Text Multiline`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `easy imageBatchToImageList`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ImageListToImageBatch`
- `easy imageToBase64`
- `YANC.ConcatStrings`
- `ShellAgentPluginOutputText`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConstrainImage|pysssss`
- `SaveImage`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `VAELoader`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `223181603622468`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **95%**（41/43）

**有卡**：`easy cleanGpuUsed`、`ImageScaleToTotalPixels`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageStitch`、`VAEEncode`、`KSampler`、`VAELoader`、`FluxKontextImageScale`、`UNETLoader`、`DualCLIPLoader`、`ConditioningZeroOut`、`Text Multiline`、`CLIPTextEncode`、`FluxGuidance`、`ImageConcatMulti`、`VAEDecode`、`LoraLoaderModelOnly`、`SaveImage`、`ReferenceLatent`、`TTP_Image_Assy`、`easy imageBatchToImageList`、`ModelSamplingSD3`、`ImageListToImageBatch`、`easy imageToBase64`、`YANC.ConcatStrings`、`ShellAgentPluginOutputText`、`ConstrainImage|pysssss`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`CLIPLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
