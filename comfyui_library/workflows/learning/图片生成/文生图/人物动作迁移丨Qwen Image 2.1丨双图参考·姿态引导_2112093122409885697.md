---
key: 图片生成/文生图/人物动作迁移丨Qwen Image 2.1丨双图参考·姿态引导_2112093122409885697.json
name: 人物动作迁移丨Qwen Image 2.1丨双图参考·姿态引导_2112093122409885697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/人物动作迁移丨Qwen Image 2.1丨双图参考·姿态引导_2112093122409885697.json
hash: 4b147000a8ac695b
coverage: 0.909091
learned_at: 2026-10-21 02:58:37
nodes: [UNETLoader, CLIPLoader, VAELoader, LoadImage, JjkText, LoadImage, PrimitiveInt, LoraLoaderModelOnly, ImageResizeKJv2, ImageResizeKJv2, EmptyLatentImage, DWPreprocessor, ImageStitch, ImageScale, ImageScale, TextEncodeQwenImage21, SaveImage, KSampler, VAEDecode, SaveImage, ImageStitch, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 960, "sampler_name": "euler", "scheduler": "simple", "seed": 752678491174185, "steps": 30, "width": 1280}
---

# 图片生成/文生图/人物动作迁移丨Qwen Image 2.1丨双图参考·姿态引导_2112093122409885697.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/人物动作迁移丨Qwen Image 2.1丨双图参考·姿态引导_2112093122409885697.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `JjkText`
- `LoadImage`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `EmptyLatentImage` ★核心
- `DWPreprocessor`
- `ImageStitch`
- `ImageScale`
- `ImageScale`
- `TextEncodeQwenImage21`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageStitch`
- `SaveImage`

## 关键参数

- `width` = `1280`
- `height` = `960`
- `batch_size` = `1`
- `seed` = `752678491174185`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`EmptyLatentImage`、`DWPreprocessor`、`ImageStitch`、`ImageScale`、`TextEncodeQwenImage21`、`SaveImage`、`KSampler`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
