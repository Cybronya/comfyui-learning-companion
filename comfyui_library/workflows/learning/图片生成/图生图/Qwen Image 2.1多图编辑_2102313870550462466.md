---
key: 图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json
name: Qwen Image 2.1多图编辑_2102313870550462466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json
hash: c3e9256ab9708164
coverage: 0.777778
learned_at: 2026-10-06 21:41:19
nodes: [CLIPLoader, CLIPLoader, BatchImagesNode, EmptyLatentImage, ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, VAELoader, LoadImage, LoadImage, JjkText, LoadImage, ResolutionSelector, SaveImage]
patterns: []
missing: [BatchImagesNode, TextGenerateLTX2Prompt]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 696486761369314, "steps": 50, "width": 1024}
discoveries: [次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑_2102313870550462466.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `CLIPLoader`
- `BatchImagesNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `696486761369314`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`CLIPLoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`UNETLoader`、`VAELoader`、`LoadImage`、`ResolutionSelector`、`SaveImage`

**缺卡**（2）：`BatchImagesNode`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
