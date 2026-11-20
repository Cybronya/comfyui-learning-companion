---
key: 平台全量/角色合影工作流 ByRui. Group Photos of Characters_1869016946027958274.json
name: 角色合影工作流 ByRui. Group Photos of Characters_1869016946027958274
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/角色合影工作流 ByRui. Group Photos of Characters_1869016946027958274.json
hash: 92c633f3fe2048b0
coverage: 0.851064
learned_at: 2026-11-14 02:43:33
nodes: [ImageConcatMulti, ResizeImageMixlab, ResizeImageMixlab, ImageConcatMulti, ImageConcatMulti, ImageToMask, CLIPTextEncode, KSampler, FluxGuidance, Text Load Line From File, ResizeImageMixlab, DF_Integer, DualCLIPLoader, UNETLoader, DF_Image_scale_to_side, LoraLoaderModelOnly, Text _O, Text _O, ShowText|pysssss, easy promptReplace, RH_Captioner, ShowText|pysssss, Reroute, VAEDecode, SetLatentNoiseMask, VAELoader, VAEEncode, CLIPTextEncode, PreviewImage, LayerUtility: ColorImage V2, LoadImage, LayerMask: MaskPreview, PreviewImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Get Image Size, AddLabel, AddLabel, PreviewImage, PreviewImage, LoadImage, SeargePromptText, SaveImage, ImageCrop, DF_Image_scale_to_side, DF_Image_scale_to_side, LayerUtility: ColorImage V2]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 370616069439037, "steps": 20}
---

# 平台全量/角色合影工作流 ByRui. Group Photos of Characters_1869016946027958274.json

> 来源文件 `comfyui_library/workflows/平台全量/角色合影工作流 ByRui. Group Photos of Characters_1869016946027958274.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `ImageConcatMulti`
- `ResizeImageMixlab`
- `ResizeImageMixlab`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageToMask`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `FluxGuidance`
- `Text Load Line From File`
- `ResizeImageMixlab`
- `DF_Integer`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `DF_Image_scale_to_side`
- `LoraLoaderModelOnly` ★核心
- `Text _O`
- `Text _O`
- `ShowText|pysssss`
- `easy promptReplace`
- `RH_Captioner`
- `ShowText|pysssss`
- `Reroute`
- `VAEDecode` ★核心
- `SetLatentNoiseMask`
- `VAELoader`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `LayerUtility: ColorImage V2`
- `LoadImage`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `Get Image Size`
- `AddLabel`
- `AddLabel`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `SeargePromptText`
- `SaveImage`
- `ImageCrop`
- `DF_Image_scale_to_side`
- `DF_Image_scale_to_side`
- `LayerUtility: ColorImage V2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `370616069439037`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **85%**（40/47）

**有卡**：`ImageConcatMulti`、`ResizeImageMixlab`、`ImageToMask`、`CLIPTextEncode`、`KSampler`、`FluxGuidance`、`Text Load Line From File`、`DF_Integer`、`DualCLIPLoader`、`UNETLoader`、`DF_Image_scale_to_side`、`LoraLoaderModelOnly`、`Text _O`、`easy promptReplace`、`RH_Captioner`、`VAEDecode`、`SetLatentNoiseMask`、`VAELoader`、`VAEEncode`、`LayerUtility: ColorImage V2`、`LoadImage`、`LayerMask: MaskPreview`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`Get Image Size`、`AddLabel`、`SeargePromptText`、`SaveImage`、`ImageCrop`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
