---
key: 平台全量/老照片修复+InvSRS_Kontext-DEV开源ComfyUI官方版_1941670941787320322.json
name: 老照片修复+InvSRS_Kontext-DEV开源ComfyUI官方版_1941670941787320322
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/老照片修复+InvSRS_Kontext-DEV开源ComfyUI官方版_1941670941787320322.json
hash: 48f70682a3df0834
coverage: 0.888889
learned_at: 2026-11-14 02:30:01
nodes: [DualCLIPLoader, LoaderGGUF, LoadImage, VAELoader, ConditioningZeroOut, CLIPTextEncode, UNETLoader, LoadImage, ImageStitch, ShowText|pysssss, GoogleTranslateTextNode, FluxKontextImageScale, VAEEncode, PreviewImage, ImageConcatMulti, KSampler, SaveImage, SaveImage, SaveImage, LoadInvSRModels, Image Comparer (rgthree), InvSRSampler, VAEDecode, ReferenceLatent, FluxGuidance, easy cleanGpuUsed, Text Multiline]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 407125596029471, "steps": 20}
---

# 平台全量/老照片修复+InvSRS_Kontext-DEV开源ComfyUI官方版_1941670941787320322.json

> 来源文件 `comfyui_library/workflows/平台全量/老照片修复+InvSRS_Kontext-DEV开源ComfyUI官方版_1941670941787320322.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `DualCLIPLoader`
- `LoaderGGUF`
- `LoadImage`
- `VAELoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `ImageStitch`
- `ShowText|pysssss`
- `GoogleTranslateTextNode`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `PreviewImage`
- `ImageConcatMulti`
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LoadInvSRModels`
- `Image Comparer (rgthree)`
- `InvSRSampler` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `easy cleanGpuUsed`
- `Text Multiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `407125596029471`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`DualCLIPLoader`、`LoaderGGUF`、`LoadImage`、`VAELoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`UNETLoader`、`ImageStitch`、`GoogleTranslateTextNode`、`FluxKontextImageScale`、`VAEEncode`、`ImageConcatMulti`、`KSampler`、`SaveImage`、`LoadInvSRModels`、`InvSRSampler`、`VAEDecode`、`ReferenceLatent`、`FluxGuidance`、`easy cleanGpuUsed`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
