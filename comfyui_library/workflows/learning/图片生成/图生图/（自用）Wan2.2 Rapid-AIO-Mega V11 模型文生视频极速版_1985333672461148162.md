---
key: 图片生成/图生图/（自用）Wan2.2 Rapid-AIO-Mega V11 模型文生视频极速版_1985333672461148162.json
name: （自用）Wan2.2 Rapid-AIO-Mega V11 模型文生视频极速版_1985333672461148162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（自用）Wan2.2 Rapid-AIO-Mega V11 模型文生视频极速版_1985333672461148162.json
hash: 6fcd88a5d11534a8
coverage: 0.791667
learned_at: 2026-10-23 13:38:23
nodes: [Note, JWInteger, Note, Note, WanVaceToVideo, ModelSamplingSD3, ApplySageAttention, CLIPTextEncode, JWInteger, JWInteger, Note, VAEDecode, KSampler, SaveImage, SaveImage, ImageFromBatch+, TT_img_enc, CR Prompt Text, Note, CLIPTextEncode, TT_img_enc_v2, SaveImage, LoadImage, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v11.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（自用）Wan2.2 Rapid-AIO-Mega V11 模型文生视频极速版_1985333672461148162.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（自用）Wan2.2 Rapid-AIO-Mega V11 模型文生视频极速版_1985333672461148162.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `Note`
- `JWInteger`
- `Note`
- `Note`
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `ApplySageAttention`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `Note`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `ImageFromBatch+`
- `TT_img_enc`
- `CR Prompt Text`
- `Note`
- `CLIPTextEncode` ★核心
- `TT_img_enc_v2`
- `SaveImage`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v11.safetensors`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`JWInteger`、`WanVaceToVideo`、`ModelSamplingSD3`、`ApplySageAttention`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`SaveImage`、`ImageFromBatch+`、`TT_img_enc`、`CR Prompt Text`、`TT_img_enc_v2`、`LoadImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CR Prompt Text、SaveImage、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
