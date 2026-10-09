---
key: 图片生成/文生图/最新 WAN2.2 融合模型 文生图洗图_1958004480736473089.json
name: 最新 WAN2.2 融合模型 文生图洗图_1958004480736473089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/最新 WAN2.2 融合模型 文生图洗图_1958004480736473089.json
hash: f961ed05a71a5c4b
coverage: 0.545455
learned_at: 2026-10-07 23:31:19
nodes: [PreviewImage, ModelSamplingSD3, Seed Everywhere, CLIPTextEncode, EmptySD3LatentImage, CheckpointLoaderSimple, CLIPTextEncode, Prompts Everywhere, KSampler (Efficient), SaveImage, Note]
patterns: []
missing: [KSampler (Efficient), Prompts Everywhere, Seed Everywhere]
parameters: {"cfg": 1, "checkpoint": "wan2.2-t2v-rapid-aio-v8.1.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 193226821865994, "steps": 8}
discoveries: [核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Prompts Everywhere` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/最新 WAN2.2 融合模型 文生图洗图_1958004480736473089.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1958004480736473089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（11 个）：
- `PreviewImage`
- `ModelSamplingSD3`
- `Seed Everywhere`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `Prompts Everywhere`
- `KSampler (Efficient)` ★核心
- `SaveImage`
- `Note`

## 关键参数

- `checkpoint` = `wan2.2-t2v-rapid-aio-v8.1.safetensors`
- `seed` = `193226821865994`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **55%**（6/11）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`EmptySD3LatentImage`、`CheckpointLoaderSimple`、`SaveImage`

**缺卡**（3）：`KSampler (Efficient)`、`Prompts Everywhere`、`Seed Everywhere`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、SaveImage、EmptySD3LatentImage、ModelSamplingSD3、KSampler、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 核心节点 `KSampler (Efficient)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Prompts Everywhere` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
