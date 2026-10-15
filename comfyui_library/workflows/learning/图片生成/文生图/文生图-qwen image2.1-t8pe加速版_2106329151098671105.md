---
key: 图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json
name: 文生图-qwen image2.1-t8pe加速版_2106329151098671105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json
hash: 52e6c8fa71100aa5
coverage: 0.653846
learned_at: 2026-10-10 20:59:47
nodes: [QwenImage21Cache, CLIPLoader, EmptyLatentImage, ComfySwitchNode, VAELoader, KSampler, easy cleanGpuUsed, VAEDecode, ResolutionSelector, UNETLoader, MarkdownNote, Note, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, PreviewImage, Image Comparer (rgthree), INTConstant, SaveImage, SeedVR2LoadDiTModel, SaveImage, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, easy showAnything, QwenPERewriteT8, CR Prompt Text]
patterns: []
missing: [easy cleanGpuUsed, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 480862308269817, "steps": 40, "width": 1024}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json`

## 结构

**节点**（26 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `EmptyLatentImage`
- `ComfySwitchNode`
- `VAELoader`
- `KSampler`
- `easy cleanGpuUsed`
- `VAEDecode`
- `ResolutionSelector`
- `UNETLoader`
- `MarkdownNote`
- `Note`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `INTConstant`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `QwenPERewriteT8`
- `CR Prompt Text`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `480862308269817`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **65%**（17/26）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`EmptyLatentImage`、`ComfySwitchNode`、`VAELoader`、`KSampler`、`easy cleanGpuUsed`、`VAEDecode`、`ResolutionSelector`、`UNETLoader`、`MarkdownNote`、`Note`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixels`、`PreviewImage`、`Image Comparer (rgthree)`

**缺卡**（2）：`easy cleanGpuUsed`、`CR Prompt Text`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
