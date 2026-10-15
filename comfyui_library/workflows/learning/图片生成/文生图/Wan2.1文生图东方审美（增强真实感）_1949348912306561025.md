---
key: 图片生成/文生图/Wan2.1文生图东方审美（增强真实感）_1949348912306561025.json
name: Wan2.1文生图东方审美（增强真实感）_1949348912306561025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.1文生图东方审美（增强真实感）_1949348912306561025.json
hash: 2f67e55f787f3c48
coverage: 0.809524
learned_at: 2026-10-15 22:27:34
nodes: [VAELoader, LoadImage, LoadImage, EmptyHunyuanLatentVideo, LayerColor: Brightness & Contrast, CLIPTextEncode, FilmGrain, KSampler, LoraLoader, SaveImage, PrimitiveInt, PrimitiveInt, PreviewImage, VAEDecode, LoraLoader, LoraLoader, CR Text, CLIPLoader, UNETLoader, CLIPTextEncode, PreviewImage]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 483990837151334, "steps": 8, "strength_clip": 0.45000000000000007, "strength_model": 0.45000000000000007}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Wan2.1文生图东方审美（增强真实感）_1949348912306561025.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.1文生图东方审美（增强真实感）_1949348912306561025.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `EmptyHunyuanLatentVideo`
- `LayerColor: Brightness & Contrast`
- `CLIPTextEncode` ★核心
- `FilmGrain`
- `KSampler` ★核心
- `LoraLoader` ★核心
- `SaveImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PreviewImage`
- `VAEDecode` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `CR Text`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`

**识别到的模式**：lora

## 关键参数

- `seed` = `483990837151334`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `lora_name` = `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors`
- `strength_model` = `0.45000000000000007`
- `strength_clip` = `0.45000000000000007`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`VAELoader`、`LoadImage`、`EmptyHunyuanLatentVideo`、`LayerColor: Brightness & Contrast`、`CLIPTextEncode`、`FilmGrain`、`KSampler`、`LoraLoader`、`SaveImage`、`VAEDecode`、`CR Text`、`CLIPLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、EmptyHunyuanLatentVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
