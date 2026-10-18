---
key: 视频生成/图生视频/一键运行：最新 WAN2.2 融合模型 图生视频_1958713035496046593.json
name: 一键运行：最新 WAN2.2 融合模型 图生视频_1958713035496046593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/一键运行：最新 WAN2.2 融合模型 图生视频_1958713035496046593.json
hash: 5f1aa9a7481ebdf5
coverage: 0.909091
learned_at: 2026-10-15 22:31:22
nodes: [KSampler (Efficient), Seed Everywhere, CLIPVisionEncode, CLIPVisionLoader, LoadImage, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, CheckpointLoaderSimple, VHS_VideoCombine, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-nsfw-v8.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 984000706479306, "steps": 8}
---

# 视频生成/图生视频/一键运行：最新 WAN2.2 融合模型 图生视频_1958713035496046593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958713035496046593.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（11 个）：
- `KSampler (Efficient)` ★核心
- `Seed Everywhere`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `Note`

## 关键参数

- `seed` = `984000706479306`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-nsfw-v8.safetensors`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`KSampler (Efficient)`、`Seed Everywhere`、`CLIPVisionEncode`、`CLIPVisionLoader`、`LoadImage`、`CLIPTextEncode`、`WanImageToVideo`、`CheckpointLoaderSimple`、`VHS_VideoCombine`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、KSampler (Efficient)、Seed Everywhere、CLIPVisionEncode、CLIPVisionLoader、VHS_VideoCombine
