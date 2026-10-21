---
key: 图片生成/文生图/wan2.2文生图+高清放大（高质量极简流）_2029319670993522690.json
name: wan2.2文生图+高清放大（高质量极简流）_2029319670993522690
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生图+高清放大（高质量极简流）_2029319670993522690.json
hash: aed47b72f89feef9
coverage: 0.818182
learned_at: 2026-10-19 22:46:14
nodes: [Note, UNETLoader, easy int, easy int, PreviewImage, CLIPLoader, LoraLoader, PathchSageAttentionKJ, EmptyHunyuanLatentVideo, CR Text, CLIPTextEncode, CLIPTextEncode, MarkdownNote, KSampler, Note, VAEDecode, VAELoader, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SaveImage, SeedVR2VideoUpscaler]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "FastWan_T2V_14B_480p_lora_rank_128_bf16.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 822125032699591, "steps": 5, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.2文生图+高清放大（高质量极简流）_2029319670993522690.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2文生图+高清放大（高质量极简流）_2029319670993522690.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `Note`
- `UNETLoader` ★核心
- `easy int`
- `easy int`
- `PreviewImage`
- `CLIPLoader`
- `LoraLoader` ★核心
- `PathchSageAttentionKJ`
- `EmptyHunyuanLatentVideo`
- `CR Text`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `KSampler` ★核心
- `Note`
- `VAEDecode` ★核心
- `VAELoader`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SeedVR2VideoUpscaler`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `FastWan_T2V_14B_480p_lora_rank_128_bf16.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`
- `seed` = `822125032699591`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`UNETLoader`、`easy int`、`CLIPLoader`、`LoraLoader`、`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`CR Text`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`VAELoader`、`SaveImage`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
