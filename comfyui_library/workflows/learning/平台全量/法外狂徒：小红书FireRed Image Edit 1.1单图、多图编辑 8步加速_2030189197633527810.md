---
key: 平台全量/法外狂徒：小红书FireRed Image Edit 1.1单图、多图编辑 8步加速_2030189197633527810.json
name: 法外狂徒：小红书FireRed Image Edit 1.1单图、多图编辑 8步加速_2030189197633527810
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/法外狂徒：小红书FireRed Image Edit 1.1单图、多图编辑 8步加速_2030189197633527810.json
hash: c7b8d6ce452e1488
coverage: 0.694444
learned_at: 2026-11-14 02:19:33
nodes: [SaveImage, Anything Everywhere3, VAELoader, ModelSamplingAuraFlow, CFGNorm, TextEncodeQwenImageEditPlus, VAEEncode, ModelSamplingAuraFlow, CFGNorm, VAEEncode, SetNode, CLIPLoader, GetNode, GetNode, GetNode, FluxKontextImageScale, MarkdownNote, ImageResize+, TTP_Tile_image_size, ImageResize+, GetImageSize+, TTP_Image_Tile_Batch, ImageScaleBy, RunningHub Deepcleaner, ImageCASharpening+, TTP_Image_Assy, KOOK_SaveJPGImage, GetImageSize+, ImageScaleBy, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, ImagePass, SeedVR2VideoUpscaler, SetNode, SetNode, RunningHub Deepcleaner, Any Switch (rgthree), Reroute, GetNode, GetNode, SetNode, KSampler, Fast Groups Bypasser (rgthree), VAEDecode, SaveImage, VAEDecode, KSampler, FluxKontextImageScale, LoadImage, FluxKontextImageScale, SetNode, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, TextEncodeQwenImageEditPlus, UNETLoader, LoadImage, PreviewImage, LoadImage, LoadImage, PreviewImage, LoadImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 256142338546589, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/法外狂徒：小红书FireRed Image Edit 1.1单图、多图编辑 8步加速_2030189197633527810.json

> 来源文件 `comfyui_library/workflows/平台全量/法外狂徒：小红书FireRed Image Edit 1.1单图、多图编辑 8步加速_2030189197633527810.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `SaveImage`
- `Anything Everywhere3`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEEncode` ★核心
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `FluxKontextImageScale`
- `MarkdownNote`
- `ImageResize+`
- `TTP_Tile_image_size`
- `ImageResize+`
- `GetImageSize+`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `RunningHub Deepcleaner`
- `ImageCASharpening+`
- `TTP_Image_Assy`
- `KOOK_SaveJPGImage`
- `GetImageSize+`
- `ImageScaleBy`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `ImagePass`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SetNode`
- `RunningHub Deepcleaner`
- `Any Switch (rgthree)`
- `Reroute`
- `GetNode`
- `GetNode`
- `SetNode`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `FluxKontextImageScale`
- `LoadImage`
- `FluxKontextImageScale`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `LoadImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `256142338546589`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（50/72）

**有卡**：`SaveImage`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`CLIPLoader`、`FluxKontextImageScale`、`ImageResize+`、`TTP_Tile_image_size`、`GetImageSize+`、`TTP_Image_Tile_Batch`、`ImageScaleBy`、`RunningHub Deepcleaner`、`ImageCASharpening+`、`TTP_Image_Assy`、`KOOK_SaveJPGImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ImagePass`、`SeedVR2VideoUpscaler`、`KSampler`、`VAEDecode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LayerUtility: ImageScaleByAspectRatio V2、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
