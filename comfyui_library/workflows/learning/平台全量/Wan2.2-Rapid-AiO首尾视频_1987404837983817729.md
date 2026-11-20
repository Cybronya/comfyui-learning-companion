---
key: 平台全量/Wan2.2-Rapid-AiO首尾视频_1987404837983817729.json
name: Wan2.2-Rapid-AiO首尾视频_1987404837983817729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Rapid-AiO首尾视频_1987404837983817729.json
hash: dadc453e739e7750
coverage: 1
learned_at: 2026-11-14 01:05:59
nodes: [SimpleMath+, ModelSamplingSD3, VAEDecode, KSampler, CheckpointLoaderSimple, CLIPTextEncode, ApplySageAttention, CLIPTextEncode, WanVideoVACEStartToEndFrame, LoadImage, LoadImage, INTConstant, WanVaceToVideo, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v11.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 867071626809982, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2-Rapid-AiO首尾视频_1987404837983817729.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Rapid-AiO首尾视频_1987404837983817729.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（14 个）：
- `SimpleMath+`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `ApplySageAttention`
- `CLIPTextEncode` ★核心
- `WanVideoVACEStartToEndFrame`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `WanVaceToVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `867071626809982`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v11.safetensors`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`SimpleMath+`、`ModelSamplingSD3`、`VAEDecode`、`KSampler`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`ApplySageAttention`、`WanVideoVACEStartToEndFrame`、`LoadImage`、`INTConstant`、`WanVaceToVideo`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ApplySageAttention、INTConstant、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
