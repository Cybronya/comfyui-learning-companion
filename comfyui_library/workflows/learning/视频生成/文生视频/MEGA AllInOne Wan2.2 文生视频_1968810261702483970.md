---
key: 视频生成/文生视频/MEGA AllInOne Wan2.2 文生视频_1968810261702483970.json
name: MEGA AllInOne Wan2.2 文生视频_1968810261702483970.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1968810261702483970.json
hash: 8aaf3c1b2e2ca42d
coverage: 0.933333
learned_at: 2026-10-15 22:43:46
nodes: [KSampler, TrimVideoLatent, WanVaceToVideo, INTConstant, INTConstant, INTConstant, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, ConcatTextOfUtils, PrimitiveStringMultiline, CheckpointLoaderSimple, VAEDecode, VHS_VideoCombine, Wan22PromptSelector]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 192054346835137, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MEGA AllInOne Wan2.2 文生视频_1968810261702483970.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1968810261702483970.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（15 个）：
- `KSampler` ★核心
- `TrimVideoLatent`
- `WanVaceToVideo`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ConcatTextOfUtils`
- `PrimitiveStringMultiline`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `Wan22PromptSelector`

## 关键参数

- `seed` = `192054346835137`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`KSampler`、`TrimVideoLatent`、`WanVaceToVideo`、`INTConstant`、`CLIPTextEncode`、`ModelSamplingSD3`、`ConcatTextOfUtils`、`CheckpointLoaderSimple`、`VAEDecode`、`VHS_VideoCombine`、`Wan22PromptSelector`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、TrimVideoLatent、Wan22PromptSelector、INTConstant、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
