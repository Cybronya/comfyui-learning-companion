---
key: 图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json
name: 文生图-qwen image2.1-t8pe加速版_2106329151098671105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json
hash: 52e6c8fa71100aa5
coverage: 0.423077
learned_at: 2026-10-06 21:52:27
nodes: [QwenImage21Cache, CLIPLoader, EmptyLatentImage, ComfySwitchNode, VAELoader, KSampler, easy cleanGpuUsed, VAEDecode, ResolutionSelector, UNETLoader, MarkdownNote, Note, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, PreviewImage, Image Comparer (rgthree), INTConstant, SaveImage, SeedVR2LoadDiTModel, SaveImage, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, easy showAnything, QwenPERewriteT8, CR Prompt Text]
patterns: []
missing: [Fast Groups Bypasser (rgthree), INTConstant, ImageScaleToTotalPixels, QwenPERewriteT8, easy cleanGpuUsed, CR Prompt Text, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 480862308269817, "steps": 40, "width": 1024}
discoveries: [次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `INTConstant` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAELoader`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
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

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `480862308269817`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **42%**（11/26）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`KSampler`、`VAEDecode`、`ResolutionSelector`、`UNETLoader`、`SaveImage`、`TextEncodeQwenImage21`

**缺卡**（9）：`Fast Groups Bypasser (rgthree)`、`INTConstant`、`ImageScaleToTotalPixels`、`QwenPERewriteT8`、`easy cleanGpuUsed`、`CR Prompt Text`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache

## 学习发现

- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `INTConstant` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明
