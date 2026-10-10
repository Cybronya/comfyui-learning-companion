---
key: 视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V4文生视频极速版_1973020564535250945.json
name: Wan2.2 Rapid-AIO-Mega V4文生视频极速版_1973020564535250945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V4文生视频极速版_1973020564535250945.json
hash: 9aa939a4e79f10e4
coverage: 0.8125
learned_at: 2026-10-10 23:06:52
nodes: [KSampler, ModelSamplingSD3, CLIPTextEncode, Note, VAEDecode, ApplySageAttention, Note, Note, JWInteger, JWInteger, JWInteger, CLIPTextEncode, WanVaceToVideo, VHS_VideoCombine, VHS_VideoCombine, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v4.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V4文生视频极速版_1973020564535250945.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Rapid-AIO-Mega V4文生视频极速版_1973020564535250945.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（16 个）：
- `KSampler` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `Note`
- `VAEDecode` ★核心
- `ApplySageAttention`
- `Note`
- `Note`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `7567358653673`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v4.safetensors`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`KSampler`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`ApplySageAttention`、`JWInteger`、`WanVaceToVideo`、`VHS_VideoCombine`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ModelSamplingSD3、VHS_VideoCombine、JWInteger、WanVaceToVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
