---
key: 图片生成/图生图/Z-image自动提示词多条件Union Controlnet 2.0控制+分块放大V1_2000560398984151041.json
name: Z-image自动提示词多条件Union Controlnet 2.0控制+分块放大V1_2000560398984151041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image自动提示词多条件Union Controlnet 2.0控制+分块放大V1_2000560398984151041.json
hash: a5ed67b274379269
coverage: 0.816327
learned_at: 2026-10-23 11:31:55
nodes: [VAELoader, EmptySD3LatentImage, Note, CLIPTextEncode, GetImageSize, CLIPLoader, ModelSamplingAuraFlow, Canny, AIO_Preprocessor, QwenImageDiffsynthControlnet, PreviewImage, AIO_Preprocessor, UNETLoader, easy showAnything, SeedVR2, LayerUtility: PurgeVRAM, SaveImage, ImageCASharpening+, SaveImage, LoadImage, ImageScaleToMaxDimension, ConditioningZeroOut, KSampler, PreviewImage, TTP_Image_Tile_Batch, ImageResize+, ImageCASharpening+, Get Image Size, ImpactMinMax, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, LoraLoaderModelOnly, TTP_Image_Assy, Qwen3_VQA, CR Prompt Text, Note, Note, easy showAnything, CR Prompt Text, Text Concatenate, Text Concatenate, easy anythingIndexSwitch, ModelPatchLoader, easy anythingIndexSwitch, SaveImage, VAEDecode, Image Comparer (rgthree), Image Comparer (rgthree), ImageResize+]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 1045532739891710, "steps": 10}
---

# 图片生成/图生图/Z-image自动提示词多条件Union Controlnet 2.0控制+分块放大V1_2000560398984151041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image自动提示词多条件Union Controlnet 2.0控制+分块放大V1_2000560398984151041.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `VAELoader`
- `EmptySD3LatentImage`
- `Note`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `Canny`
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `PreviewImage`
- `AIO_Preprocessor`
- `UNETLoader` ★核心
- `easy showAnything`
- `SeedVR2`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `ImageCASharpening+`
- `SaveImage`
- `LoadImage`
- `ImageScaleToMaxDimension`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `PreviewImage`
- `TTP_Image_Tile_Batch`
- `ImageResize+`
- `ImageCASharpening+`
- `Get Image Size`
- `ImpactMinMax`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TTP_Image_Assy`
- `Qwen3_VQA`
- `CR Prompt Text`
- `Note`
- `Note`
- `easy showAnything`
- `CR Prompt Text`
- `Text Concatenate`
- `Text Concatenate`
- `easy anythingIndexSwitch`
- `ModelPatchLoader`
- `easy anythingIndexSwitch`
- `SaveImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `ImageResize+`

## 关键参数

- `seed` = `1045532739891710`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（40/49）

**有卡**：`VAELoader`、`EmptySD3LatentImage`、`CLIPTextEncode`、`GetImageSize`、`CLIPLoader`、`ModelSamplingAuraFlow`、`Canny`、`AIO_Preprocessor`、`QwenImageDiffsynthControlnet`、`UNETLoader`、`SeedVR2`、`LayerUtility: PurgeVRAM`、`SaveImage`、`ImageCASharpening+`、`LoadImage`、`ImageScaleToMaxDimension`、`ConditioningZeroOut`、`KSampler`、`TTP_Image_Tile_Batch`、`ImageResize+`、`Get Image Size`、`ImpactMinMax`、`LoraLoaderModelOnly`、`TTP_Image_Assy`、`Qwen3_VQA`、`CR Prompt Text`、`Text Concatenate`、`easy anythingIndexSwitch`、`ModelPatchLoader`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
