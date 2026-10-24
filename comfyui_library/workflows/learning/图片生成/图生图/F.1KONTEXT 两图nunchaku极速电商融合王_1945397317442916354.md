---
key: 图片生成/图生图/F.1KONTEXT 两图nunchaku极速电商融合王_1945397317442916354.json
name: F.1KONTEXT 两图nunchaku极速电商融合王_1945397317442916354
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1KONTEXT 两图nunchaku极速电商融合王_1945397317442916354.json
hash: 14f798f0adfe278c
coverage: 0.944444
learned_at: 2026-10-23 10:52:37
nodes: [ConditioningZeroOut, FluxGuidance, ReferenceLatent, CLIPTextEncode, SaveImage, FluxKontextImageScale, KSampler, VAEEncode, VAEDecode, ImageStitch, MarkdownNote, LoadImage, EmptySD3LatentImage, NunchakuFluxDiTLoader, LoadImage, RH_Translator, DualCLIPLoader, VAELoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 92077066544767, "steps": 20}
---

# 图片生成/图生图/F.1KONTEXT 两图nunchaku极速电商融合王_1945397317442916354.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1KONTEXT 两图nunchaku极速电商融合王_1945397317442916354.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ConditioningZeroOut`
- `FluxGuidance`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `FluxKontextImageScale`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ImageStitch`
- `MarkdownNote`
- `LoadImage`
- `EmptySD3LatentImage`
- `NunchakuFluxDiTLoader`
- `LoadImage`
- `RH_Translator`
- `DualCLIPLoader`
- `VAELoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `92077066544767`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`ConditioningZeroOut`、`FluxGuidance`、`ReferenceLatent`、`CLIPTextEncode`、`SaveImage`、`FluxKontextImageScale`、`KSampler`、`VAEEncode`、`VAEDecode`、`ImageStitch`、`LoadImage`、`EmptySD3LatentImage`、`NunchakuFluxDiTLoader`、`RH_Translator`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent
