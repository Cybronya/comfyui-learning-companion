---
key: 图片生成/图生图/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2109808936437243905.json
name: Action Transfer人物替换+人物换装 Qwen+Image+2.1_2109808936437243905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2109808936437243905.json
hash: 36c3ed8e63520924
coverage: 0.842105
learned_at: 2026-10-23 10:50:59
nodes: [QwenImage21Cache, ComfySwitchNode, VAEDecode, KSampler, easy imageConcat, VAELoader, CLIPLoader, UNETLoader, easy imageConcat, EmptyLatentImage, ImageResizeKJv2, ImageResizeKJv2, SaveImage, SaveImage, LoadImage, LoadImage, PrimitiveInt, TextEncodeQwenImage21, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 878472000001135, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2109808936437243905.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2109808936437243905.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `QwenImage21Cache`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `easy imageConcat`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `easy imageConcat`
- `EmptyLatentImage` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `TextEncodeQwenImage21`
- `JjkText`

## 关键参数

- `seed` = `878472000001135`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`QwenImage21Cache`、`VAEDecode`、`KSampler`、`easy imageConcat`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`EmptyLatentImage`、`ImageResizeKJv2`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
