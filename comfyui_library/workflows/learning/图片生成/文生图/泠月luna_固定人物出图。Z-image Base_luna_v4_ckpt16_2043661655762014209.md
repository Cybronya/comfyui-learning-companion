---
key: 图片生成/文生图/泠月luna_固定人物出图。Z-image Base_luna_v4_ckpt16_2043661655762014209.json
name: 泠月luna_固定人物出图。Z-image Base_luna_v4_ckpt16_2043661655762014209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/泠月luna_固定人物出图。Z-image Base_luna_v4_ckpt16_2043661655762014209.json
hash: fcf551fc68b5c327
coverage: 0.941176
learned_at: 2026-10-21 03:01:43
nodes: [CLIPTextEncode, CLIPTextEncode, VAEDecode, ModelSamplingAuraFlow, CR Text Concatenate, VAELoader, Reroute, KSampler, CLIPLoader, CR SDXL Aspect Ratio, workflow>lora pipe, UNETLoader, SaveImage, Text Multiline, TTResolutionSelector, CR Text, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 664340492983443, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/泠月luna_固定人物出图。Z-image Base_luna_v4_ckpt16_2043661655762014209.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/泠月luna_固定人物出图。Z-image Base_luna_v4_ckpt16_2043661655762014209.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `CR Text Concatenate`
- `VAELoader`
- `Reroute`
- `KSampler` ★核心
- `CLIPLoader`
- `CR SDXL Aspect Ratio`
- `workflow>lora pipe`
- `UNETLoader` ★核心
- `SaveImage`
- `Text Multiline`
- `TTResolutionSelector`
- `CR Text`
- `CR Text`

## 关键参数

- `seed` = `664340492983443`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`ModelSamplingAuraFlow`、`CR Text Concatenate`、`VAELoader`、`KSampler`、`CLIPLoader`、`CR SDXL Aspect Ratio`、`workflow>lora pipe`、`UNETLoader`、`SaveImage`、`Text Multiline`、`TTResolutionSelector`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、workflow>lora pipe、CR SDXL Aspect Ratio

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
