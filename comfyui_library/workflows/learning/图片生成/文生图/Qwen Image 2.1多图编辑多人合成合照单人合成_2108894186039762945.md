---
key: 图片生成/文生图/Qwen Image 2.1多图编辑多人合成合照单人合成_2108894186039762945.json
name: Qwen Image 2.1多图编辑多人合成合照单人合成_2108894186039762945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1多图编辑多人合成合照单人合成_2108894186039762945.json
hash: f77950fc1994b23e
coverage: 0.833333
learned_at: 2026-10-21 02:54:12
nodes: [CLIPLoader, CLIPLoader, BatchImagesNode, EmptyLatentImage, ComfySwitchNode, VAEDecode, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, VAELoader, ResolutionSelector, QwenImage21Cache, KSampler, SaveImage, easy imageConcat, easy imageConcat, easy imageConcat, JjkText, LoadImage, SaveImage, 孤海注释, 孤海注释, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 152271907447062, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1多图编辑多人合成合照单人合成_2108894186039762945.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1多图编辑多人合成合照单人合成_2108894186039762945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `CLIPLoader`
- `BatchImagesNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `VAELoader`
- `ResolutionSelector`
- `QwenImage21Cache`
- `KSampler` ★核心
- `SaveImage`
- `easy imageConcat`
- `easy imageConcat`
- `easy imageConcat`
- `JjkText`
- `LoadImage`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `152271907447062`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`EmptyLatentImage`、`VAEDecode`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`QwenImage21Cache`、`KSampler`、`SaveImage`、`easy imageConcat`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
