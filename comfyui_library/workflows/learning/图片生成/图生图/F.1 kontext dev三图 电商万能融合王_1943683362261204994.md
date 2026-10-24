---
key: 图片生成/图生图/F.1 kontext dev三图 电商万能融合王_1943683362261204994.json
name: F.1 kontext dev三图 电商万能融合王_1943683362261204994
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1 kontext dev三图 电商万能融合王_1943683362261204994.json
hash: 1e03a2c1e51cd3b1
coverage: 1
learned_at: 2026-10-23 10:52:35
nodes: [ConditioningZeroOut, FluxGuidance, ReferenceLatent, VAEEncode, VAEDecode, FluxKontextImageScale, ImageStitch, ImageStitch, KSampler, DualCLIPLoader, VAELoader, LoadImage, LoadImage, LoadImage, CLIPTextEncode, RH_Translator, EmptySD3LatentImage, UNETLoader, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 821110919427711, "steps": 20}
---

# 图片生成/图生图/F.1 kontext dev三图 电商万能融合王_1943683362261204994.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1 kontext dev三图 电商万能融合王_1943683362261204994.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ConditioningZeroOut`
- `FluxGuidance`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `ImageStitch`
- `ImageStitch`
- `KSampler` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `821110919427711`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`ConditioningZeroOut`、`FluxGuidance`、`ReferenceLatent`、`VAEEncode`、`VAEDecode`、`FluxKontextImageScale`、`ImageStitch`、`KSampler`、`DualCLIPLoader`、`VAELoader`、`LoadImage`、`CLIPTextEncode`、`RH_Translator`、`EmptySD3LatentImage`、`UNETLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
