---
key: 图片生成/图生图/Kontext姿势参考-Flux-UnionPro-CN2_1961975841964146689.json
name: Kontext姿势参考-Flux-UnionPro-CN2_1961975841964146689
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kontext姿势参考-Flux-UnionPro-CN2_1961975841964146689.json
hash: 51d1de9ada971981
coverage: 0.848485
learned_at: 2026-10-23 11:07:14
nodes: [DualCLIPLoader, SaveImage, MarkdownNote, LoraLoaderModelOnly, CLIPTextEncode, VAEDecode, UNETLoader, VAEEncode, ReferenceLatent, KSampler, TeaCache, VAELoader, Note, ImageStitch, SaveImage, PreviewImage, ControlNetLoader, FluxGuidance, ConditioningZeroOut, LoadImage, ImageStitch, ShowText|pysssss, Text Concatenate, RH_Captioner, Text Multiline, ControlNetApplyAdvanced, easy imageRemBg, LoadImage, ImageScaleDownToSize, PreviewImage, ImageScaleDownToSize, FluxKontextImageScale, AIO_Preprocessor]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 986093768163848, "steps": 20}
---

# 图片生成/图生图/Kontext姿势参考-Flux-UnionPro-CN2_1961975841964146689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kontext姿势参考-Flux-UnionPro-CN2_1961975841964146689.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `DualCLIPLoader`
- `SaveImage`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `KSampler` ★核心
- `TeaCache`
- `VAELoader`
- `Note`
- `ImageStitch`
- `SaveImage`
- `PreviewImage`
- `ControlNetLoader`
- `FluxGuidance`
- `ConditioningZeroOut`
- `LoadImage`
- `ImageStitch`
- `ShowText|pysssss`
- `Text Concatenate`
- `RH_Captioner`
- `Text Multiline`
- `ControlNetApplyAdvanced` ★核心
- `easy imageRemBg`
- `LoadImage`
- `ImageScaleDownToSize`
- `PreviewImage`
- `ImageScaleDownToSize`
- `FluxKontextImageScale`
- `AIO_Preprocessor`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `986093768163848`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1.0000000000000002`

## 知识

覆盖率 **85%**（28/33）

**有卡**：`DualCLIPLoader`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEDecode`、`UNETLoader`、`VAEEncode`、`ReferenceLatent`、`KSampler`、`TeaCache`、`VAELoader`、`ImageStitch`、`ControlNetLoader`、`FluxGuidance`、`ConditioningZeroOut`、`LoadImage`、`Text Concatenate`、`RH_Captioner`、`Text Multiline`、`ControlNetApplyAdvanced`、`easy imageRemBg`、`ImageScaleDownToSize`、`FluxKontextImageScale`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
