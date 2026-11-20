---
key: 平台全量/Flux Kontext Dev真人转动漫Limbus风格_1945286636521365506.json
name: Flux Kontext Dev真人转动漫Limbus风格_1945286636521365506
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Kontext Dev真人转动漫Limbus风格_1945286636521365506.json
hash: 109009e5e9b32097
coverage: 0.909091
learned_at: 2026-11-14 00:27:53
nodes: [ConditioningZeroOut, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, CLIPTextEncode, VAEDecode, SaveImage, ImageConcanate, LoadImage, ImageStitch, CR Prompt Text, PreviewImage, UnetLoaderGGUF, KSampler, SaveImage, LoraLoaderModelOnly, MagCache, DualCLIPLoader, VAELoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 393939897285114, "steps": 20}
---

# 平台全量/Flux Kontext Dev真人转动漫Limbus风格_1945286636521365506.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Kontext Dev真人转动漫Limbus风格_1945286636521365506.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `ConditioningZeroOut`
- `LoadImageOutput`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `MarkdownNote`
- `FluxGuidance`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageConcanate`
- `LoadImage`
- `ImageStitch`
- `CR Prompt Text`
- `PreviewImage`
- `UnetLoaderGGUF` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `MagCache`
- `DualCLIPLoader`
- `VAELoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `393939897285114`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`CLIPTextEncode`、`VAEDecode`、`SaveImage`、`ImageConcanate`、`LoadImage`、`ImageStitch`、`CR Prompt Text`、`UnetLoaderGGUF`、`KSampler`、`LoraLoaderModelOnly`、`MagCache`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage
