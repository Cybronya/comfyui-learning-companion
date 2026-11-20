---
key: 图片生成/图生图/Qwen2.1-图生图16参考提速版_2115478113609142274.json
name: Qwen2.1-图生图16参考提速版_2115478113609142274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1-图生图16参考提速版_2115478113609142274.json
hash: c5499f3d6b550e01
coverage: 1
learned_at: 2026-10-30 17:51:05
nodes: [UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, EmptyLatentImage, KSampler, VAEDecode, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1.2, "denoise": 0.97, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 470379795650164, "steps": 25, "width": 1920}
---

# 图片生成/图生图/Qwen2.1-图生图16参考提速版_2115478113609142274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1-图生图16参考提速版_2115478113609142274.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `470379795650164`
- `steps` = `25`
- `cfg` = `1.2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.97`

## 知识

覆盖率 **100%**（26/26）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
