---
key: 图片生成/文生图/001-image_qwen_image2.1-VOSR2-VS-SEEDVR2_2105226191602020353.json
name: 001-image_qwen_image2.1-VOSR2-VS-SEEDVR2_2105226191602020353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/001-image_qwen_image2.1-VOSR2-VS-SEEDVR2_2105226191602020353.json
hash: 6974e5516fda7c61
coverage: 0.586957
learned_at: 2026-10-07 02:04:25
nodes: [SetNode, SetNode, GetNode, easy promptLine, ResolutionSelector, EmptyLatentImage, GetNode, VOSR2ModelLoader, SaveImage, SaveImage, SplitImageWithAlpha, SetNode, GetNode, KSamplerAdvanced, SeedVR2Conditioning, JoinImageWithAlpha, KSampler, SeedVR2Preprocess, UNETLoader, VAELoader, ModelAttentionBackend, TextEncodeQwenImage21, Text Multiline, TextGenerateLTX2Prompt, ResizeImageMaskNode, Text Multiline, CLIPLoader, Fast Groups Bypasser (rgthree), ShowText|pysssss, SaveImage, Image Comparer (rgthree), VAELoader, VAEDecodeTiled, VAEEncodeTiled, VOSR2Upscale, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, SplitImageWithAlpha, GetNode, easy cleanGpuUsed, UNETLoader, SeedVR2PostProcessing, easy cleanGpuUsed, Image Comparer (rgthree), Image Comparer (rgthree)]
patterns: []
missing: [Text Multiline, Text Multiline, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy promptLine]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1344, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 1, "width": 960}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/001-image_qwen_image2.1-VOSR2-VS-SEEDVR2_2105226191602020353.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/001-image_qwen_image2.1-VOSR2-VS-SEEDVR2_2105226191602020353.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `easy promptLine`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `GetNode`
- `VOSR2ModelLoader`
- `SaveImage`
- `SaveImage`
- `SplitImageWithAlpha`
- `SetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `SeedVR2Conditioning`
- `JoinImageWithAlpha`
- `KSampler` ★核心
- `SeedVR2Preprocess`
- `UNETLoader` ★核心
- `VAELoader`
- `ModelAttentionBackend`
- `TextEncodeQwenImage21`
- `Text Multiline`
- `TextGenerateLTX2Prompt`
- `ResizeImageMaskNode`
- `Text Multiline`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `ShowText|pysssss`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAELoader`
- `VAEDecodeTiled` ★核心
- `VAEEncodeTiled` ★核心
- `VOSR2Upscale`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SplitImageWithAlpha`
- `GetNode`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `SeedVR2PostProcessing`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`

## 关键参数

- `width` = `960`
- `height` = `1344`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **59%**（27/46）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`VOSR2ModelLoader`、`SaveImage`、`SplitImageWithAlpha`、`KSamplerAdvanced`、`SeedVR2Conditioning`、`JoinImageWithAlpha`、`KSampler`、`SeedVR2Preprocess`、`UNETLoader`、`VAELoader`、`ModelAttentionBackend`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`ResizeImageMaskNode`、`CLIPLoader`、`VAEDecodeTiled`、`VAEEncodeTiled`、`VOSR2Upscale`、`VAEDecode`、`SeedVR2PostProcessing`

**缺卡**（7）：`Text Multiline`、`Text Multiline`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy promptLine`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
