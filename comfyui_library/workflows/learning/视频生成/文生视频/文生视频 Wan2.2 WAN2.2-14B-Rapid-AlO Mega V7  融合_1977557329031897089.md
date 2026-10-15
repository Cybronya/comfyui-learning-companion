---
key: 视频生成/文生视频/文生视频 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7  融合_1977557329031897089.json
name: 文生视频 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7  融合_1977557329031897089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7  融合_1977557329031897089.json
hash: 87948586fa950d7d
coverage: 0.888889
learned_at: 2026-10-15 22:48:41
nodes: [Seed Everywhere, VHS_VideoCombine, WanVaceToVideo, CLIPTextEncode, KSampler (Efficient), CLIPTextEncode, CheckpointLoaderSimple, ModelSamplingSD3, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v7.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 193226821865994, "steps": 4}
---

# 视频生成/文生视频/文生视频 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7  融合_1977557329031897089.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/文生视频 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7  融合_1977557329031897089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（9 个）：
- `Seed Everywhere`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `KSampler (Efficient)` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `ModelSamplingSD3`
- `Note`

## 关键参数

- `seed` = `193226821865994`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v7.safetensors`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`Seed Everywhere`、`VHS_VideoCombine`、`WanVaceToVideo`、`CLIPTextEncode`、`KSampler (Efficient)`、`CheckpointLoaderSimple`、`ModelSamplingSD3`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、KSampler (Efficient)、Seed Everywhere、ModelSamplingSD3、VHS_VideoCombine、WanVaceToVideo、KSampler
