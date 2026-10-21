---
key: 图片生成/文生图/LH-DMT版本-2.生图片类-029.Z-image智能改词文生图-NF_2016493278639693826.json
name: LH-DMT版本-2.生图片类-029.Z-image智能改词文生图-NF_2016493278639693826
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-029.Z-image智能改词文生图-NF_2016493278639693826.json
hash: 3dd869af847561b0
coverage: 0.928571
learned_at: 2026-10-19 22:15:12
nodes: [EmptyLatentImage, CR Prompt List, easy showAnything, KSampler, VAEDecode, ConditioningZeroOut, CLIPTextEncode, CLIPLoader, UNETLoader, SaveImage, ImpactInt, ImpactInt, String Literal, VAELoader]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 581493387965875, "steps": 9, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/LH-DMT版本-2.生图片类-029.Z-image智能改词文生图-NF_2016493278639693826.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LH-DMT版本-2.生图片类-029.Z-image智能改词文生图-NF_2016493278639693826.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `EmptyLatentImage` ★核心
- `CR Prompt List`
- `easy showAnything`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `SaveImage`
- `ImpactInt`
- `ImpactInt`
- `String Literal`
- `VAELoader`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `581493387965875`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`EmptyLatentImage`、`CR Prompt List`、`KSampler`、`VAEDecode`、`ConditioningZeroOut`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`SaveImage`、`ImpactInt`、`String Literal`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
