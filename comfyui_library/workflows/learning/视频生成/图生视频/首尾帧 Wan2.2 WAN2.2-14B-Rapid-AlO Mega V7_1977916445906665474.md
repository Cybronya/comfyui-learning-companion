---
key: 视频生成/图生视频/首尾帧 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7_1977916445906665474.json
name: 首尾帧 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7_1977916445906665474.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1977916445906665474.json
hash: 5736e87d4165aafb
coverage: 0.928571
learned_at: 2026-10-15 22:32:16
nodes: [Seed Everywhere, CLIPTextEncode, VHS_VideoCombine, KSampler (Efficient), WanVideoVACEStartToEndFrame, CLIPTextEncode, WanVaceToVideo, easy imageScaleDownToSize, easy imageScaleDownToSize, Note, LoadImage, LoadImage, ModelSamplingSD3, CheckpointLoaderSimple]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v7.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 193226821865994, "steps": 4}
---

# 视频生成/图生视频/首尾帧 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7_1977916445906665474.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1977916445906665474.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（14 个）：
- `Seed Everywhere`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `KSampler (Efficient)` ★核心
- `WanVideoVACEStartToEndFrame`
- `CLIPTextEncode` ★核心
- `WanVaceToVideo`
- `easy imageScaleDownToSize`
- `easy imageScaleDownToSize`
- `Note`
- `LoadImage`
- `LoadImage`
- `ModelSamplingSD3`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `193226821865994`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v7.safetensors`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`Seed Everywhere`、`CLIPTextEncode`、`VHS_VideoCombine`、`KSampler (Efficient)`、`WanVideoVACEStartToEndFrame`、`WanVaceToVideo`、`easy imageScaleDownToSize`、`LoadImage`、`ModelSamplingSD3`、`CheckpointLoaderSimple`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、KSampler (Efficient)、Seed Everywhere、easy imageScaleDownToSize、ModelSamplingSD3、VHS_VideoCombine
