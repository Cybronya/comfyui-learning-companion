---
key: 图片生成/图生图/qwen-image2.1故事分镜_参考图生成_九六四宫格三模式_2102369371170623489.json
name: qwen-image2.1故事分镜_参考图生成_九六四宫格三模式_2102369371170623489.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image2.1故事分镜_参考图生成_九六四宫格三模式_2102369371170623489.json
hash: f5955dc47ae13067
coverage: 0.395349
learned_at: 2026-10-09 22:27:12
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, TextEncodeQwenImage21, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, EmptyLatentImage, easy seed, GetNode, UNETLoader, QwenImage21Cache, CLIPLoader, VAELoader, SetNode, SetNode, SetNode, SaveImage, MarkdownNote, StringConcatenate, PrimitiveBoolean, ComfySwitchNode, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, KSampler, VAEDecode, GetNode, GetNode, ComfySwitchNode, RHLLMChatNode, PreviewAny, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, PrimitiveBoolean]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy seed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 875063224334553, "steps": 25, "width": 2048}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/qwen-image2.1故事分镜_参考图生成_九六四宫格三模式_2102369371170623489.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102369371170623489.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `PrimitiveInt`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `easy seed`
- `GetNode`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SaveImage`
- `MarkdownNote`
- `StringConcatenate`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `RHLLMChatNode`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveBoolean`

## 关键参数

- `width` = `2048`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `875063224334553`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **40%**（17/43）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`SaveImage`、`StringConcatenate`、`PrimitiveBoolean`、`KSampler`、`VAEDecode`、`RHLLMChatNode`、`LoadImage`

**缺卡**（4）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
