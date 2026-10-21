---
key: 图片生成/图生图/F.1 kontext老照片划痕清理终极版_2066168189830131713.json
name: F.1 kontext老照片划痕清理终极版_2066168189830131713
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1 kontext老照片划痕清理终极版_2066168189830131713.json
hash: 1dee09e935f2304b
coverage: 0.92
learned_at: 2026-10-21 00:38:55
nodes: [VAEDecode, DualCLIPLoader, Image Comparer (rgthree), LoadImage, VAELoader, VAEEncode, ConditioningZeroOut, DeepTranslatorTextNode, StringConcatenate, ControlNetApplyAdvanced, DepthAnythingV2Preprocessor, FluxGuidance, KSampler, TextInput_, 孤海-浮点滑条, UNETLoader, SaveImage, LoraLoaderModelOnly, easy imageScaleToNormPixels, CLIPTextEncode, PreviewImage, ControlNetLoader, ReferenceLatent, DF_Float, ImageScaleToTotalPixels]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta", "seed": 1019798594616913, "steps": 20}
---

# 图片生成/图生图/F.1 kontext老照片划痕清理终极版_2066168189830131713.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1 kontext老照片划痕清理终极版_2066168189830131713.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `LoadImage`
- `VAELoader`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `StringConcatenate`
- `ControlNetApplyAdvanced` ★核心
- `DepthAnythingV2Preprocessor`
- `FluxGuidance`
- `KSampler` ★核心
- `TextInput_`
- `孤海-浮点滑条`
- `UNETLoader` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `easy imageScaleToNormPixels`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ControlNetLoader`
- `ReferenceLatent`
- `DF_Float`
- `ImageScaleToTotalPixels`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `1019798594616913`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`VAEDecode`、`DualCLIPLoader`、`LoadImage`、`VAELoader`、`VAEEncode`、`ConditioningZeroOut`、`DeepTranslatorTextNode`、`StringConcatenate`、`ControlNetApplyAdvanced`、`DepthAnythingV2Preprocessor`、`FluxGuidance`、`KSampler`、`TextInput_`、`孤海-浮点滑条`、`UNETLoader`、`SaveImage`、`LoraLoaderModelOnly`、`easy imageScaleToNormPixels`、`CLIPTextEncode`、`ControlNetLoader`、`ReferenceLatent`、`DF_Float`、`ImageScaleToTotalPixels`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
