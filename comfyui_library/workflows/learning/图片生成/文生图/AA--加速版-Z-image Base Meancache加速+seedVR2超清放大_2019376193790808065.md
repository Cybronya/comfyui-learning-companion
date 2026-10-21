---
key: 图片生成/文生图/AA--加速版-Z-image Base Meancache加速+seedVR2超清放大_2019376193790808065.json
name: AA--加速版-Z-image Base Meancache加速+seedVR2超清放大_2019376193790808065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AA--加速版-Z-image Base Meancache加速+seedVR2超清放大_2019376193790808065.json
hash: 9450c0349e460e23
coverage: 0.833333
learned_at: 2026-10-19 22:29:32
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, UNETLoader, ModelSamplingAuraFlow, EmptySD3LatentImage, KSampler, MarkdownNote, SeedVR2LoadDiTModel, VAEDecode, Fast Groups Bypasser (rgthree), INTConstant, Note, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, CLIPTextEncode, SaveImage, MeanCache_ZImage]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 1119853695139807, "steps": 50}
---

# 图片生成/文生图/AA--加速版-Z-image Base Meancache加速+seedVR2超清放大_2019376193790808065.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/AA--加速版-Z-image Base Meancache加速+seedVR2超清放大_2019376193790808065.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `MarkdownNote`
- `SeedVR2LoadDiTModel`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `Note`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `MeanCache_ZImage`

## 关键参数

- `seed` = `1119853695139807`
- `steps` = `50`
- `cfg` = `4`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`KSampler`、`SeedVR2LoadDiTModel`、`VAEDecode`、`INTConstant`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`MeanCache_ZImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel
