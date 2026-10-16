---
key: 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V6图生视频极速版_1975830994022436866.json
name: （自用）Wan2.2 Rapid-AIO-Mega V6图生视频极速版_1975830994022436866.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1975830994022436866.json
hash: c31bf47769497e3c
coverage: 0.857143
learned_at: 2026-10-15 22:32:09
nodes: [ModelSamplingSD3, CLIPTextEncode, WanVaceToVideo, Note, WanVideoVACEStartToEndFrame, ApplySageAttention, Note, Note, CLIPTextEncode, LoadImage, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VAEDecode, TT_img_enc, SaveImage, CheckpointLoaderSimple, KSampler, CR Prompt Text, LoadImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v6.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 739755501032891, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/（自用）Wan2.2 Rapid-AIO-Mega V6图生视频极速版_1975830994022436866.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1975830994022436866.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `Note`
- `WanVideoVACEStartToEndFrame`
- `ApplySageAttention`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `VAEDecode` ★核心
- `TT_img_enc`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `CR Prompt Text`
- `LoadImage`
- `SaveImage`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v6.safetensors`
- `seed` = `739755501032891`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`ApplySageAttention`、`LoadImage`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`TT_img_enc`、`SaveImage`、`CheckpointLoaderSimple`、`KSampler`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CR Prompt Text、SaveImage、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
