---
key: 图片生成/图生图/F.1 KONTEXT DEV 单图版nunchaku极速电商万能改图王_1945395741722386434.json
name: F.1 KONTEXT DEV 单图版nunchaku极速电商万能改图王_1945395741722386434
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1 KONTEXT DEV 单图版nunchaku极速电商万能改图王_1945395741722386434.json
hash: 551e55c5d4b73d0f
coverage: 1
learned_at: 2026-10-23 10:52:34
nodes: [CLIPTextEncode, FluxGuidance, ConditioningZeroOut, ReferenceLatent, FluxKontextImageScale, VAEEncode, NunchakuFluxDiTLoader, VAEDecode, KSampler, SaveImage, EmptySD3LatentImage, LoadImage, RH_Translator, DualCLIPLoader, VAELoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 586968845239429, "steps": 20}
---

# 图片生成/图生图/F.1 KONTEXT DEV 单图版nunchaku极速电商万能改图王_1945395741722386434.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1 KONTEXT DEV 单图版nunchaku极速电商万能改图王_1945395741722386434.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `NunchakuFluxDiTLoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `EmptySD3LatentImage`
- `LoadImage`
- `RH_Translator`
- `DualCLIPLoader`
- `VAELoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `586968845239429`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`ReferenceLatent`、`FluxKontextImageScale`、`VAEEncode`、`NunchakuFluxDiTLoader`、`VAEDecode`、`KSampler`、`SaveImage`、`EmptySD3LatentImage`、`LoadImage`、`RH_Translator`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent
