---
key: 图片生成/图生图/Z-image自动提示词+Union Controlnet 2.0控制+TTP放大_2001462714058895361.json
name: Z-image自动提示词+Union Controlnet 2.0控制+TTP放大_2001462714058895361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image自动提示词+Union Controlnet 2.0控制+TTP放大_2001462714058895361.json
hash: 052f739e8279cdbc
coverage: 0.796296
learned_at: 2026-10-23 11:31:55
nodes: [Note, ModelSamplingAuraFlow, PreviewImage, TTP_Image_Tile_Batch, ImageResize+, ImageCASharpening+, Get Image Size, ImpactMinMax, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SeedVR2, SaveImage, easy showAnything, UNETLoader, Canny, AIO_Preprocessor, AIO_Preprocessor, SaveImage, Text Concatenate, Text Concatenate, EmptySD3LatentImage, GetImageSize, ModelPatchLoader, VAELoader, QwenImageDiffsynthControlnet, PreviewImage, CLIPTextEncode, ConditioningZeroOut, VAEDecode, ImageResize+, MarkdownNote, MarkdownNote, MarkdownNote, CLIPLoader, easy anythingIndexSwitch, Qwen3_VQA, ImageScaleToMaxDimension, easy showAnything, easy anythingIndexSwitch, ImageConcanate, TTP_Image_Assy, Image Comparer (rgthree), SaveImage, ImageCASharpening+, PreviewImage, ImageConcanate, PreviewImage, KSampler, LoraLoaderModelOnly, CR Prompt Text, Int, LoadImage, Int, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 1089823097931882, "steps": 10}
---

# 图片生成/图生图/Z-image自动提示词+Union Controlnet 2.0控制+TTP放大_2001462714058895361.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image自动提示词+Union Controlnet 2.0控制+TTP放大_2001462714058895361.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `Note`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `TTP_Image_Tile_Batch`
- `ImageResize+`
- `ImageCASharpening+`
- `Get Image Size`
- `ImpactMinMax`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `SeedVR2`
- `SaveImage`
- `easy showAnything`
- `UNETLoader` ★核心
- `Canny`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `SaveImage`
- `Text Concatenate`
- `Text Concatenate`
- `EmptySD3LatentImage`
- `GetImageSize`
- `ModelPatchLoader`
- `VAELoader`
- `QwenImageDiffsynthControlnet`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `ImageResize+`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `easy anythingIndexSwitch`
- `Qwen3_VQA`
- `ImageScaleToMaxDimension`
- `easy showAnything`
- `easy anythingIndexSwitch`
- `ImageConcanate`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ImageCASharpening+`
- `PreviewImage`
- `ImageConcanate`
- `PreviewImage`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `Int`
- `LoadImage`
- `Int`
- `CR Prompt Text`

## 关键参数

- `seed` = `1089823097931882`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（43/54）

**有卡**：`ModelSamplingAuraFlow`、`TTP_Image_Tile_Batch`、`ImageResize+`、`ImageCASharpening+`、`Get Image Size`、`ImpactMinMax`、`LayerUtility: PurgeVRAM`、`SeedVR2`、`SaveImage`、`UNETLoader`、`Canny`、`AIO_Preprocessor`、`Text Concatenate`、`EmptySD3LatentImage`、`GetImageSize`、`ModelPatchLoader`、`VAELoader`、`QwenImageDiffsynthControlnet`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEDecode`、`CLIPLoader`、`easy anythingIndexSwitch`、`Qwen3_VQA`、`ImageScaleToMaxDimension`、`ImageConcanate`、`TTP_Image_Assy`、`KSampler`、`LoraLoaderModelOnly`、`CR Prompt Text`、`Int`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
