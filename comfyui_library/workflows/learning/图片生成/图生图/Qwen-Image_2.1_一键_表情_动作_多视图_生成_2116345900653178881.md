---
key: 图片生成/图生图/Qwen-Image_2.1_一键_表情_动作_多视图_生成_2116345900653178881.json
name: Qwen-Image_2.1_一键_表情_动作_多视图_生成_2116345900653178881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image_2.1_一键_表情_动作_多视图_生成_2116345900653178881.json
hash: 5324c43f315e81ba
coverage: 0.552239
learned_at: 2026-11-02 19:12:53
nodes: [MarkdownNote, Reroute, Reroute, KSamplerSelect, ImageConcanate, QwenImage21Cache, Reroute, CFGGuider, ManualSigmas, KSamplerSelect, RandomNoise, Seed (rgthree), SamplerCustomAdvanced, ManualSigmas, SamplerCustomAdvanced, EmptyLatentImage, Reroute, Image Comparer (rgthree), Seed (rgthree), ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, Reroute, ResolutionSelector, Fast Groups Muter (rgthree), ImageFromBatch, ImageFromBatch, ImageFromBatch, Reroute, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageConcatMulti, ImageConcatMulti, ImageConcatMulti, ImageScaleToTotalPixels, ImageScaleToTotalPixels, easy imageListToImageBatch, VAEDecode, UNETLoader, CLIPLoader, Reroute, PrimitiveStringMultiline, ResolutionSelector, EmptyLatentImage, ResolutionSelector, Reroute, Reroute, easy promptList, VAELoader, QwenImage21Cache, MarkdownNote, Reroute, Reroute, Reroute, easy promptList, PrimitiveStringMultiline, ImageConcatMulti, Reroute, Reroute, Reroute, Reroute, CR Text Replace, Reroute, Any Switch (rgthree), Reroute, ImageConcanate, ComfySwitchNode, ComfySwitchNode, ImageConcanate, SimpleComparison+, easy promptList, PrimitiveStringMultiline, easy anythingIndexSwitch, SimpleComparison+, Reroute, LoadImage, LoadImage, easy int, RandomNoise, CFGGuider, Reroute, PrimitiveStringMultiline, PrimitiveStringMultiline, TextEncodeQwenImage21, easy int, SaveImage, easy mathInt, Reroute, SimpleComparison+, ResolutionSelector, easy int, easy int, ComfySwitchNode, VAEDecode, Reroute, Reroute, ComfySwitchNode, SaveImage, Fast Groups Bypasser (rgthree), ComfySwitchNode, Reroute, TextEncodeQwenImage21, Reroute, Reroute, Reroute, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, easy promptList, easy promptList, easy promptList, SaveImage, ResolutionSelector, ComfySwitchNode, ComfySwitchNode, Reroute, Reroute, Reroute, Reroute, easy int, SimpleComparison+, Reroute, Reroute, Reroute, PrimitiveStringMultiline, ComfySwitchNode, PrimitiveBoolean, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/Qwen-Image_2.1_一键_表情_动作_多视图_生成_2116345900653178881.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image_2.1_一键_表情_动作_多视图_生成_2116345900653178881.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（134 个）：
- `MarkdownNote`
- `Reroute`
- `Reroute`
- `KSamplerSelect` ★核心
- `ImageConcanate`
- `QwenImage21Cache`
- `Reroute`
- `CFGGuider`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `Seed (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `Reroute`
- `Image Comparer (rgthree)`
- `Seed (rgthree)`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `Reroute`
- `ResolutionSelector`
- `Fast Groups Muter (rgthree)`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `Reroute`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `easy imageListToImageBatch`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `Reroute`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `Reroute`
- `Reroute`
- `easy promptList`
- `VAELoader`
- `QwenImage21Cache`
- `MarkdownNote`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy promptList`
- `PrimitiveStringMultiline`
- `ImageConcatMulti`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CR Text Replace`
- `Reroute`
- `Any Switch (rgthree)`
- `Reroute`
- `ImageConcanate`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ImageConcanate`
- `SimpleComparison+`
- `easy promptList`
- `PrimitiveStringMultiline`
- `easy anythingIndexSwitch`
- `SimpleComparison+`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `easy int`
- `RandomNoise`
- `CFGGuider`
- `Reroute`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `easy int`
- `SaveImage`
- `easy mathInt`
- `Reroute`
- `SimpleComparison+`
- `ResolutionSelector`
- `easy int`
- `easy int`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `ComfySwitchNode`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `ComfySwitchNode`
- `Reroute`
- `TextEncodeQwenImage21`
- `Reroute`
- `Reroute`
- `Reroute`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `SaveImage`
- `ResolutionSelector`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy int`
- `SimpleComparison+`
- `Reroute`
- `Reroute`
- `Reroute`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **55%**（74/134）

**有卡**：`KSamplerSelect`、`ImageConcanate`、`QwenImage21Cache`、`CFGGuider`、`ManualSigmas`、`RandomNoise`、`Seed (rgthree)`、`SamplerCustomAdvanced`、`EmptyLatentImage`、`ImageFromBatch`、`ResolutionSelector`、`ImageConcatMulti`、`ImageScaleToTotalPixels`、`easy imageListToImageBatch`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`easy promptList`、`VAELoader`、`CR Text Replace`、`SimpleComparison+`、`easy anythingIndexSwitch`、`LoadImage`、`easy int`、`TextEncodeQwenImage21`、`SaveImage`、`easy mathInt`、`PrimitiveBoolean`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、QwenImage21Cache
