---
key: 图片生成/图生图/F.1 Kontext dev 官方两图版 万物编辑 图片融合 换衣换背景_1943235556400914434.json
name: F.1 Kontext dev 官方两图版 万物编辑 图片融合 换衣换背景_1943235556400914434
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1 Kontext dev 官方两图版 万物编辑 图片融合 换衣换背景_1943235556400914434.json
hash: e8ade561d8de8c24
coverage: 0.944444
learned_at: 2026-10-23 10:52:34
nodes: [ConditioningZeroOut, FluxGuidance, ReferenceLatent, VAELoader, CLIPTextEncode, SaveImage, FluxKontextImageScale, MarkdownNote, KSampler, VAEEncode, VAEDecode, ImageStitch, RH_Translator, LoadImage, LoadImage, EmptySD3LatentImage, UNETLoader, DualCLIPLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 788758095125282, "steps": 20}
---

# 图片生成/图生图/F.1 Kontext dev 官方两图版 万物编辑 图片融合 换衣换背景_1943235556400914434.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1 Kontext dev 官方两图版 万物编辑 图片融合 换衣换背景_1943235556400914434.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ConditioningZeroOut`
- `FluxGuidance`
- `ReferenceLatent`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `FluxKontextImageScale`
- `MarkdownNote`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ImageStitch`
- `RH_Translator`
- `LoadImage`
- `LoadImage`
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `788758095125282`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`ConditioningZeroOut`、`FluxGuidance`、`ReferenceLatent`、`VAELoader`、`CLIPTextEncode`、`SaveImage`、`FluxKontextImageScale`、`KSampler`、`VAEEncode`、`VAEDecode`、`ImageStitch`、`RH_Translator`、`LoadImage`、`EmptySD3LatentImage`、`UNETLoader`、`DualCLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
