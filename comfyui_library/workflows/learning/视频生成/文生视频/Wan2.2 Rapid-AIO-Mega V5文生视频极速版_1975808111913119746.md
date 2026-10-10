---
key: 视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V5文生视频极速版_1975808111913119746.json
name: Wan2.2 Rapid-AIO-Mega V5文生视频极速版_1975808111913119746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V5文生视频极速版_1975808111913119746.json
hash: d4ba525dc110dd2e
coverage: 0.923077
learned_at: 2026-10-10 23:06:53
nodes: [CheckpointLoaderSimple, ApplySageAttention, ModelSamplingSD3, WanVaceToVideo, KSampler, VAEDecode, CLIPTextEncode, JWInteger, JWInteger, Note, CLIPTextEncode, JWInteger, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v5.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V5文生视频极速版_1975808111913119746.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V5文生视频极速版_1975808111913119746.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（13 个）：
- `CheckpointLoaderSimple` ★核心
- `ApplySageAttention`
- `ModelSamplingSD3`
- `WanVaceToVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `Note`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `wan2.2-rapid-mega-aio-v5.safetensors`
- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CheckpointLoaderSimple`、`ApplySageAttention`、`ModelSamplingSD3`、`WanVaceToVideo`、`KSampler`、`VAEDecode`、`CLIPTextEncode`、`JWInteger`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ModelSamplingSD3、VHS_VideoCombine、JWInteger、WanVaceToVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
