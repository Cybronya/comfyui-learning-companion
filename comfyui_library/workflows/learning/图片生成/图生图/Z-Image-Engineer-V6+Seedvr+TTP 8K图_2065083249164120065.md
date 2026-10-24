---
key: 图片生成/图生图/Z-Image-Engineer-V6+Seedvr+TTP 8K图_2065083249164120065.json
name: Z-Image-Engineer-V6+Seedvr+TTP 8K图_2065083249164120065
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image-Engineer-V6+Seedvr+TTP 8K图_2065083249164120065.json
hash: e80cbb5b233443f4
coverage: 0.729167
learned_at: 2026-10-23 11:29:35
nodes: [ImageResize+, ConditioningZeroOut, TTP_Image_Tile_Batch, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2GGUF, TTP_Image_Assy, Note, Note, AspectRatio, PreviewImage, PreviewImage, CLIPTextEncode, LayerUtility: PurgeVRAM, PreviewImage, easy int, UNETLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, CR Text, Note, LoadImage, KSampler, Note, Note, CR Text, CLIPLoader, CR Prompt Text, PreviewImage, ImageCASharpening+, LayerUtility: PurgeVRAM, PreviewImage, SaveImage, VAELoader, EmptyLatentImage, CR Text Replace, RH_LLMAPI_NODE, Text Concatenate, ProcessString, QwenImageEngineer, JDCN_StringToList, DeepTranslatorTextNode, easy showAnything, MarkdownNote, CR Prompt Text, CLIPLoaderGGUF, VAEDecode, SaveImage, easy showAnything]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 880943124471723, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-Image-Engineer-V6+Seedvr+TTP 8K图_2065083249164120065.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image-Engineer-V6+Seedvr+TTP 8K图_2065083249164120065.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `ImageResize+`
- `ConditioningZeroOut`
- `TTP_Image_Tile_Batch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2GGUF`
- `TTP_Image_Assy`
- `Note`
- `Note`
- `AspectRatio`
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `easy int`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CR Text`
- `Note`
- `LoadImage`
- `KSampler` ★核心
- `Note`
- `Note`
- `CR Text`
- `CLIPLoader`
- `CR Prompt Text`
- `PreviewImage`
- `ImageCASharpening+`
- `LayerUtility: PurgeVRAM`
- `PreviewImage`
- `SaveImage`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CR Text Replace`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `ProcessString`
- `QwenImageEngineer`
- `JDCN_StringToList`
- `DeepTranslatorTextNode`
- `easy showAnything`
- `MarkdownNote`
- `CR Prompt Text`
- `CLIPLoaderGGUF`
- `VAEDecode` ★核心
- `SaveImage`
- `easy showAnything`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `880943124471723`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（35/48）

**有卡**：`ImageResize+`、`ConditioningZeroOut`、`TTP_Image_Tile_Batch`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2GGUF`、`TTP_Image_Assy`、`AspectRatio`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM`、`easy int`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`CR Text`、`LoadImage`、`KSampler`、`CLIPLoader`、`CR Prompt Text`、`ImageCASharpening+`、`SaveImage`、`VAELoader`、`EmptyLatentImage`、`CR Text Replace`、`RH_LLMAPI_NODE`、`Text Concatenate`、`ProcessString`、`QwenImageEngineer`、`JDCN_StringToList`、`DeepTranslatorTextNode`、`CLIPLoaderGGUF`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
