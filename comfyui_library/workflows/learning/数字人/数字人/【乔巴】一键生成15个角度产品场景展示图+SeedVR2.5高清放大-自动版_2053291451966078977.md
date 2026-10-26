---
key: 数字人/数字人/【乔巴】一键生成15个角度产品场景展示图+SeedVR2.5高清放大-自动版_2053291451966078977.json
name: 【乔巴】一键生成15个角度产品场景展示图+SeedVR2.5高清放大-自动版_2053291451966078977
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/【乔巴】一键生成15个角度产品场景展示图+SeedVR2.5高清放大-自动版_2053291451966078977.json
hash: abda3b22b7eef867
coverage: 0.853659
learned_at: 2026-10-26 01:59:48
nodes: [CLIPLoader, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageResize+, DF_Integer, SimpleMath+, TTP_Image_Tile_Batch, easy cleanGpuUsed, Get Image Size, ImpactMinMax, TTP_Image_Assy, ImageCASharpening+, ImageResize+, DF_Integer, easy promptLine, VAEEncode, easy clearCacheAll, VAEDecode, ImageCASharpening+, TextEncodeQwenImageEditPlus, ImpactImageBatchToImageList, KSampler, ProcessString, easy showAnything, easy showAnything, RH_LLMAPI_NODE, Fast Groups Bypasser (rgthree), SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, SeedVR2LoadDiTModel, MarkdownNote, SaveImage, TextEncodeQwenImageEditPlus, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, LoadImage, Image Comparer (rgthree), PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "simple", "seed": 184295352615438, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/【乔巴】一键生成15个角度产品场景展示图+SeedVR2.5高清放大-自动版_2053291451966078977.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/【乔巴】一键生成15个角度产品场景展示图+SeedVR2.5高清放大-自动版_2053291451966078977.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `CLIPLoader`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageResize+`
- `DF_Integer`
- `SimpleMath+`
- `TTP_Image_Tile_Batch`
- `easy cleanGpuUsed`
- `Get Image Size`
- `ImpactMinMax`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `ImageResize+`
- `DF_Integer`
- `easy promptLine`
- `VAEEncode` ★核心
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `ImageCASharpening+`
- `TextEncodeQwenImageEditPlus`
- `ImpactImageBatchToImageList`
- `KSampler` ★核心
- `ProcessString`
- `easy showAnything`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `SeedVR2LoadDiTModel`
- `MarkdownNote`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `LoadImage`
- `Image Comparer (rgthree)`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `184295352615438`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`CLIPLoader`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageResize+`、`DF_Integer`、`SimpleMath+`、`TTP_Image_Tile_Batch`、`easy cleanGpuUsed`、`Get Image Size`、`ImpactMinMax`、`TTP_Image_Assy`、`ImageCASharpening+`、`easy promptLine`、`VAEEncode`、`easy clearCacheAll`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`ImpactImageBatchToImageList`、`KSampler`、`ProcessString`、`RH_LLMAPI_NODE`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`SeedVR2LoadDiTModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
