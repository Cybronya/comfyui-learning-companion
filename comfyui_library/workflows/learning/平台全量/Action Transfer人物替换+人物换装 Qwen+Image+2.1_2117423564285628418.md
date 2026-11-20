---
key: 平台全量/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2117423564285628418.json
name: Action Transfer人物替换+人物换装 Qwen+Image+2.1_2117423564285628418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2117423564285628418.json
hash: 5efea4e0440e90e8
coverage: 0.842105
learned_at: 2026-11-14 00:17:28
nodes: [QwenImage21Cache, ComfySwitchNode, VAEDecode, KSampler, easy imageConcat, VAELoader, CLIPLoader, UNETLoader, easy imageConcat, EmptyLatentImage, ImageResizeKJv2, ImageResizeKJv2, SaveImage, SaveImage, LoadImage, LoadImage, PrimitiveInt, TextEncodeQwenImage21, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 20643992801966, "steps": 25, "width": 1024}
---

# 平台全量/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2117423564285628418.json

> 来源文件 `comfyui_library/workflows/平台全量/Action Transfer人物替换+人物换装 Qwen+Image+2.1_2117423564285628418.json`

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

- `seed` = `20643992801966`
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

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
