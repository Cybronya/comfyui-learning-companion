---
key: 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2102556544050225153.json
name: 多图编辑 Multi-Image Editing Qwen+Image+2.1_2102556544050225153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2102556544050225153.json
hash: e9502e7511ff7e49
coverage: 0.772727
learned_at: 2026-10-10 20:48:16
nodes: [CLIPLoader, CLIPLoader, BatchImagesNode, EmptyLatentImage, ComfySwitchNode, VAEDecode, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, VAELoader, QwenImage21Cache, KSampler, easy imageConcat, easy imageConcat, easy imageConcat, LoadImage, LoadImage, LoadImage, JjkText, ResolutionSelector, SaveImage, SaveImage]
patterns: []
missing: [easy imageConcat, easy imageConcat, easy imageConcat]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 975422592640714, "steps": 50, "width": 1024}
discoveries: [次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2102556544050225153.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多图编辑 Multi-Image Editing Qwen+Image+2.1_2102556544050225153.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
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
- `QwenImage21Cache`
- `KSampler` ★核心
- `easy imageConcat`
- `easy imageConcat`
- `easy imageConcat`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `ResolutionSelector`
- `SaveImage`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `975422592640714`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（17/22）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`EmptyLatentImage`、`VAEDecode`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`KSampler`、`LoadImage`、`ResolutionSelector`、`SaveImage`

**缺卡**（3）：`easy imageConcat`、`easy imageConcat`、`easy imageConcat`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识
