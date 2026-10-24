---
key: 图片生成/图生图/Qwen-Image-Edit-Rapid-AIO-双图编辑_1977937392734720001.json
name: Qwen-Image-Edit-Rapid-AIO-双图编辑_1977937392734720001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-Rapid-AIO-双图编辑_1977937392734720001.json
hash: 9518cf2b4b9f921a
coverage: 0.923077
learned_at: 2026-10-23 11:16:59
nodes: [TextEncodeQwenImageEditPlus, JjkText, KSampler, VAEDecode, SaveImage, CheckpointLoaderSimple, TextEncodeQwenImageEditPlus, LoadImage, LoadImage, ImageScaleDownToSize, EmptyLatentImage, ImageScaleDownToSize, GetImageSize]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-v4.safetensors", "denoise": 1, "height": 512, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 729003653705697, "steps": 4, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-Edit-Rapid-AIO-双图编辑_1977937392734720001.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-Rapid-AIO-双图编辑_1977937392734720001.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `TextEncodeQwenImageEditPlus`
- `JjkText`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `LoadImage`
- `ImageScaleDownToSize`
- `EmptyLatentImage` ★核心
- `ImageScaleDownToSize`
- `GetImageSize`

## 关键参数

- `seed` = `729003653705697`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-v4.safetensors`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`TextEncodeQwenImageEditPlus`、`KSampler`、`VAEDecode`、`SaveImage`、`CheckpointLoaderSimple`、`LoadImage`、`ImageScaleDownToSize`、`EmptyLatentImage`、`GetImageSize`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、EmptyLatentImage、LoadImage、TextEncodeQwenImageEditPlus、GetImageSize、GetImageSize

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
