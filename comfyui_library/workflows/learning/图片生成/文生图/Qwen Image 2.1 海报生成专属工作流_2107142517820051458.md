---
key: 图片生成/文生图/Qwen Image 2.1 海报生成专属工作流_2107142517820051458.json
name: Qwen Image 2.1 海报生成专属工作流_2107142517820051458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 海报生成专属工作流_2107142517820051458.json
hash: 285c7f0fc1e20636
coverage: 0.300971
learned_at: 2026-10-06 21:47:59
nodes: [SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, PathchSageAttentionKJ, QwenImage21Cache, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, ModelAttentionBackend, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ResolutionSelector, CR Prompt Text, ShowText|pysssss, EmptyLatentImage, CR Prompt Text, MarkdownNote, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VRAM_Debug, Any Switch (rgthree), PixaromaGroupSwitch, PixaromaGroupSwitch, QwenPERewriteT8, CR Prompt Text, PixaromaGroupSwitch, Any Switch (rgthree), PreviewAny, CR Text Concatenate, PixaromaResolution, EmptyLatentImage, PathchSageAttentionKJ, QwenImage21Cache, ModelAttentionBackend, TextEncodeQwenImage21, VRAM_Debug, CR Prompt Text, PixaromaLabel, CR Prompt Text, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PixaromaGroupSwitch, LoadImage, CR Text Concatenate, TextEncodeQwenImage21, LoadImage, LoadImage, MarkdownNote, PixaromaLabel, PixaromaLabel, CR Prompt Text, UNETLoader, CLIPLoader, VAELoader, VAELoader, CLIPLoader, UNETLoader, QwenPERewriteT8, KSampler, VAEDecode, SaveImageAdvanced, VAEDecode, KSampler, SaveImageAdvanced, SaveImage, SaveImage]
patterns: []
missing: [CR Text Concatenate, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ModelAttentionBackend, ModelAttentionBackend, PathchSageAttentionKJ, PathchSageAttentionKJ, PixaromaGroupSwitch, PixaromaGroupSwitch, PixaromaGroupSwitch, PixaromaGroupSwitch, PixaromaLabel, PixaromaLabel, PixaromaLabel, QwenPERewriteT8, QwenPERewriteT8, VRAM_Debug, VRAM_Debug, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, PixaromaResolution, PreviewAny, SaveImageAdvanced, SaveImageAdvanced]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666801090491300, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `ModelAttentionBackend` 知识库中没有该节点类型的任何知识, 次要节点 `ModelAttentionBackend` 知识库中没有该节点类型的任何知识, 次要节点 `PathchSageAttentionKJ` 知识库中没有该节点类型的任何知识, 次要节点 `PathchSageAttentionKJ` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaLabel` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaLabel` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaLabel` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `VRAM_Debug` 知识库中没有该节点类型的任何知识, 次要节点 `VRAM_Debug` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `PixaromaResolution` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen Image 2.1 海报生成专属工作流_2107142517820051458.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 海报生成专属工作流_2107142517820051458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（103 个）：
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `ModelAttentionBackend`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResolutionSelector`
- `CR Prompt Text`
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `CR Prompt Text`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VRAM_Debug`
- `Any Switch (rgthree)`
- `PixaromaGroupSwitch`
- `PixaromaGroupSwitch`
- `QwenPERewriteT8`
- `CR Prompt Text`
- `PixaromaGroupSwitch`
- `Any Switch (rgthree)`
- `PreviewAny`
- `CR Text Concatenate`
- `PixaromaResolution`
- `EmptyLatentImage` ★核心
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `TextEncodeQwenImage21`
- `VRAM_Debug`
- `CR Prompt Text`
- `PixaromaLabel`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PixaromaGroupSwitch`
- `LoadImage`
- `CR Text Concatenate`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `PixaromaLabel`
- `PixaromaLabel`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenPERewriteT8`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `666801090491300`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **30%**（31/103）

**有卡**：`QwenImage21Cache`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`SaveImage`

**缺卡**（37）：`CR Text Concatenate`、`CR Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelAttentionBackend`、`ModelAttentionBackend`、`PathchSageAttentionKJ`、`PathchSageAttentionKJ`、`PixaromaGroupSwitch`、`PixaromaGroupSwitch`、`PixaromaGroupSwitch`、`PixaromaGroupSwitch`、`PixaromaLabel`、`PixaromaLabel`、`PixaromaLabel`、`QwenPERewriteT8`、`QwenPERewriteT8`、`VRAM_Debug`、`VRAM_Debug`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`PixaromaResolution`、`PreviewAny`、`SaveImageAdvanced`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `ModelAttentionBackend` 知识库中没有该节点类型的任何知识
- 次要节点 `ModelAttentionBackend` 知识库中没有该节点类型的任何知识
- 次要节点 `PathchSageAttentionKJ` 知识库中没有该节点类型的任何知识
- 次要节点 `PathchSageAttentionKJ` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaLabel` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaLabel` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaLabel` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
- 次要节点 `VRAM_Debug` 知识库中没有该节点类型的任何知识
- 次要节点 `VRAM_Debug` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `PixaromaResolution` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
