---
key: 平台全量/kontext_一键移除-2.0_1957771054355771394.json
name: kontext_一键移除-2.0_1957771054355771394
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/kontext_一键移除-2.0_1957771054355771394.json
hash: 6edc3d3ec1b07474
coverage: 0.692308
learned_at: 2026-11-14 01:13:41
nodes: [FluxKontextImageScale, INPAINT_MaskedFill, PreviewImage, Image Comparer (rgthree), FluxGuidance, easy cleanGpuUsed, ConditioningZeroOut, KSampler, LoraLoaderModelOnly, LoadImage, DualCLIPLoader, LoraLoaderModelOnly, ChinesePrompt_Mix, VAEDecode, UNETLoader, VAELoader, Anything Everywhere3, Anything Everywhere, SaveImage, Anything Everywhere, VAEEncode, ReferenceLatent, Anything Everywhere, CLIPTextEncode, Note, Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 994505988945058, "steps": 30}
---

# 平台全量/kontext_一键移除-2.0_1957771054355771394.json

> 来源文件 `comfyui_library/workflows/平台全量/kontext_一键移除-2.0_1957771054355771394.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（26 个）：
- `FluxKontextImageScale`
- `INPAINT_MaskedFill`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `FluxGuidance`
- `easy cleanGpuUsed`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ChinesePrompt_Mix`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `Anything Everywhere3`
- `Anything Everywhere`
- `SaveImage`
- `Anything Everywhere`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `994505988945058`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（18/26）

**有卡**：`FluxKontextImageScale`、`INPAINT_MaskedFill`、`FluxGuidance`、`easy cleanGpuUsed`、`ConditioningZeroOut`、`KSampler`、`LoraLoaderModelOnly`、`LoadImage`、`DualCLIPLoader`、`ChinesePrompt_Mix`、`VAEDecode`、`UNETLoader`、`VAELoader`、`SaveImage`、`VAEEncode`、`ReferenceLatent`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
