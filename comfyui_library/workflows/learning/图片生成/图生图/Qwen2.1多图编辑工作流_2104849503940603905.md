---
key: 图片生成/图生图/Qwen2.1多图编辑工作流_2104849503940603905.json
name: Qwen2.1多图编辑工作流_2104849503940603905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1多图编辑工作流_2104849503940603905.json
hash: 7501294aaa708b53
coverage: 0.730769
learned_at: 2026-10-21 00:43:39
nodes: [UNETLoader, VAEDecode, PreviewImage, SaveImage, Note, CLIPLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, Note, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, TextEncodeQwenImage21, LoadImage, LoraLoaderModelOnly, KSampler, Image Comparer (rgthree), Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 1106923842022909, "steps": 30, "width": 1024}
---

# 图片生成/图生图/Qwen2.1多图编辑工作流_2104849503940603905.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1多图编辑工作流_2104849503940603905.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `Note`

## 关键参数

- `width` = `1024`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `1106923842022909`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`UNETLoader`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`LoadImage`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
