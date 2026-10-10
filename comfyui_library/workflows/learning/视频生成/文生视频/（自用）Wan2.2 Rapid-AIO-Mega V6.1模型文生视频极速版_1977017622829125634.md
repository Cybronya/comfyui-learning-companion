---
key: 视频生成/文生视频/（自用）Wan2.2 Rapid-AIO-Mega V6.1模型文生视频极速版_1977017622829125634.json
name: （自用）Wan2.2 Rapid-AIO-Mega V6.1模型文生视频极速版_1977017622829125634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 Rapid-AIO-Mega V6.1模型文生视频极速版_1977017622829125634.json
hash: ee9f7e8a57647e5f
coverage: 0.75
learned_at: 2026-10-10 23:14:43
nodes: [Note, JWInteger, KSampler, CheckpointLoaderSimple, Note, Note, WanVaceToVideo, ModelSamplingSD3, ApplySageAttention, CLIPTextEncode, JWInteger, JWInteger, Note, TT_img_enc, SaveImage, VAEDecode, ImageFromBatch+, LoadImage, SaveImage, CLIPTextEncode]
patterns: []
missing: [ImageFromBatch+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v6.1.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 7567358653673, "steps": 4}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/（自用）Wan2.2 Rapid-AIO-Mega V6.1模型文生视频极速版_1977017622829125634.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/（自用）Wan2.2 Rapid-AIO-Mega V6.1模型文生视频极速版_1977017622829125634.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `Note`
- `JWInteger`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `Note`
- `Note`
- `WanVaceToVideo`
- `ModelSamplingSD3`
- `ApplySageAttention`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `Note`
- `TT_img_enc`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `LoadImage`
- `SaveImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v6.1.safetensors`

## 知识

覆盖率 **75%**（15/20）

**有卡**：`JWInteger`、`KSampler`、`CheckpointLoaderSimple`、`WanVaceToVideo`、`ModelSamplingSD3`、`ApplySageAttention`、`CLIPTextEncode`、`TT_img_enc`、`SaveImage`、`VAEDecode`、`LoadImage`

**缺卡**（1）：`ImageFromBatch+`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveImage、ModelSamplingSD3、JWInteger

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
