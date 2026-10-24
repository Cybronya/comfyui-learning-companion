---
key: 图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V3版 多功能模型_1976168551994261506.json
name: Qwen-Image-Edit-Rapid-Aio V3版 多功能模型_1976168551994261506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V3版 多功能模型_1976168551994261506.json
hash: d482d1f64689a6d9
coverage: 1
learned_at: 2026-10-23 11:17:00
nodes: [TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, CR Text, CheckpointLoaderSimple, SaveImage, LoadImage, CR Text Concatenate, VAEDecode, easy imageSize, CR SDXL Aspect Ratio, LoadImage, LoadImage, CR Text, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-v3.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 618510021216680, "steps": 10}
---

# 图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V3版 多功能模型_1976168551994261506.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-Rapid-Aio V3版 多功能模型_1976168551994261506.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `CR Text`
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `LoadImage`
- `CR Text Concatenate`
- `VAEDecode` ★核心
- `easy imageSize`
- `CR SDXL Aspect Ratio`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `KSampler` ★核心

## 关键参数

- `checkpoint` = `Qwen-Rapid-AIO-v3.safetensors`
- `seed` = `618510021216680`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`TextEncodeQwenImageEditPlus`、`CR Text`、`CheckpointLoaderSimple`、`SaveImage`、`LoadImage`、`CR Text Concatenate`、`VAEDecode`、`easy imageSize`、`CR SDXL Aspect Ratio`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、LoadImage、TextEncodeQwenImageEditPlus、CR SDXL Aspect Ratio、easy imageSize、SaveImage
