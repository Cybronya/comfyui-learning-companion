---
key: 图片生成/图生图/QWen2.1图像编辑_2102423497988460545.json
name: QWen2.1图像编辑_2102423497988460545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QWen2.1图像编辑_2102423497988460545.json
hash: 8c112748b3823633
coverage: 0.736842
learned_at: 2026-10-10 20:48:04
nodes: [QwenImage21Cache, MarkdownNote, MarkdownNote, VAEDecode, TextGenerate, PreviewAny, BatchImagesNode, PrimitiveStringMultiline, CR Prompt Text, ComfySwitchNode, PrimitiveInt, EmptyLatentImage, KSampler, ComfySwitchNode, SaveImage, ResolutionSelector, TextEncodeQwenImage21, PrimitiveBoolean, PrimitiveBoolean, CLIPLoader, VAELoader, UNETLoader, UNETLoader, ComfySwitchNode, CLIPLoader, PrimitiveBoolean, CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ComfySwitchNode]
patterns: []
missing: [CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 505584410010387, "steps": 25, "width": 1024}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/QWen2.1图像编辑_2102423497988460545.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QWen2.1图像编辑_2102423497988460545.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `QwenImage21Cache`
- `MarkdownNote`
- `MarkdownNote`
- `VAEDecode` ★核心
- `TextGenerate`
- `PreviewAny`
- `BatchImagesNode`
- `PrimitiveStringMultiline`
- `CR Prompt Text`
- `ComfySwitchNode`
- `PrimitiveInt`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `SaveImage`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `CLIPLoader`
- `PrimitiveBoolean`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ComfySwitchNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `505584410010387`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`QwenImage21Cache`、`VAEDecode`、`TextGenerate`、`BatchImagesNode`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`PrimitiveBoolean`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
