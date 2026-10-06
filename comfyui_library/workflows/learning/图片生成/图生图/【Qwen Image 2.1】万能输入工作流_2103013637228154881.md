---
key: 图片生成/图生图/【Qwen Image 2.1】万能输入工作流_2103013637228154881.json
name: 【Qwen Image 2.1】万能输入工作流_2103013637228154881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【Qwen Image 2.1】万能输入工作流_2103013637228154881.json
hash: 7bcc4a61eebef96a
coverage: 0.653846
learned_at: 2026-10-06 21:42:56
nodes: [SaveImage, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, Fast Groups Bypasser (rgthree), VAEDecode, KSampler, CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, CR Prompt Text, ResolutionSelector, LoadImage, GetNode, Note, PreviewAny, LoadImage, ComfySwitchNode, CLIPLoader, SetNode, EmptyLatentImage, TextGenerateLTX2Prompt]
patterns: []
missing: [Fast Groups Bypasser (rgthree), CR Prompt Text, PreviewAny, TextGenerateLTX2Prompt]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1015641285360799, "steps": 40, "width": 1024}
discoveries: [次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/【Qwen Image 2.1】万能输入工作流_2103013637228154881.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【Qwen Image 2.1】万能输入工作流_2103013637228154881.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `SaveImage`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `ResolutionSelector`
- `LoadImage`
- `GetNode`
- `Note`
- `PreviewAny`
- `LoadImage`
- `ComfySwitchNode`
- `CLIPLoader`
- `SetNode`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`

## 关键参数

- `seed` = `1015641285360799`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **65%**（17/26）

**有卡**：`SaveImage`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`VAEDecode`、`KSampler`、`CLIPLoader`、`LoadImage`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`

**缺卡**（4）：`Fast Groups Bypasser (rgthree)`、`CR Prompt Text`、`PreviewAny`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `TextGenerateLTX2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
