---
key: 平台全量/Flux.1 Kontext 一键商品生背景 V1.0_1968962581920694274.json
name: Flux.1 Kontext 一键商品生背景 V1.0_1968962581920694274
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.1 Kontext 一键商品生背景 V1.0_1968962581920694274.json
hash: 0ecbc339c378a2f2
coverage: 0.941176
learned_at: 2026-11-14 00:28:44
nodes: [VAEDecode, FluxGuidance, FluxKontextImageScale, VAEEncode, ConditioningZeroOut, ReferenceLatent, ImageConcanate, PreviewImage, LoraLoaderModelOnly, VAELoader, SaveImage, LoadImage, DualCLIPLoader, KSampler, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 16194587616877, "steps": 30}
---

# 平台全量/Flux.1 Kontext 一键商品生背景 V1.0_1968962581920694274.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.1 Kontext 一键商品生背景 V1.0_1968962581920694274.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `VAEDecode` ★核心
- `FluxGuidance`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ImageConcanate`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `SaveImage`
- `LoadImage`
- `DualCLIPLoader`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `16194587616877`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`VAEDecode`、`FluxGuidance`、`FluxKontextImageScale`、`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`ImageConcanate`、`LoraLoaderModelOnly`、`VAELoader`、`SaveImage`、`LoadImage`、`DualCLIPLoader`、`KSampler`、`UNETLoader`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
