---
key: 视频生成/文生视频/文生视频 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7  融合_1977557329031897089.json
name: 文生视频 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7  融合_1977557329031897089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/文生视频 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7  融合_1977557329031897089.json
hash: 87948586fa950d7d
coverage: 0.666667
learned_at: 2026-10-10 23:13:05
nodes: [Seed Everywhere, VHS_VideoCombine, WanVaceToVideo, CLIPTextEncode, KSampler (Efficient), CLIPTextEncode, CheckpointLoaderSimple, ModelSamplingSD3, Note]
patterns: []
missing: [KSampler (Efficient), Seed Everywhere]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v7.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 193226821865994, "steps": 4}
discoveries: [核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **67%**（6/9）

**有卡**：`VHS_VideoCombine`、`WanVaceToVideo`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`ModelSamplingSD3`

**缺卡**（2）：`KSampler (Efficient)`、`Seed Everywhere`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、ModelSamplingSD3、VHS_VideoCombine、WanVaceToVideo、KSampler、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
