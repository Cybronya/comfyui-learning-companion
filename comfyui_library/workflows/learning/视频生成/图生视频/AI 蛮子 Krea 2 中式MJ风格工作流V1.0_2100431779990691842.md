---
key: 视频生成/图生视频/AI 蛮子 Krea 2 中式MJ风格工作流V1.0_2100431779990691842.json
name: AI 蛮子 Krea 2 中式MJ风格工作流V1.0_2100431779990691842
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI 蛮子 Krea 2 中式MJ风格工作流V1.0_2100431779990691842.json
hash: d5043dcb86f2d763
coverage: 0.581197
learned_at: 2026-10-17 01:58:53
nodes: [SetNode, ImageResizeKJv2, ImageResizeKJv2, 孤海注释, 孤海注释, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, MiniMaxH3ImageToVideo, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, GetNode, MathExpression|pysssss, ConditioningZeroOut, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, SetNode, GetNode, GetNode, GetNode, SaveVideo, ResolutionSelector, GetNode, 孤海注释, CreateVideo, MarkdownNote, VRAM_Debug, 孤海注释, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ConditioningZeroOut, CLIPTextEncode, ConditioningKrea2Rebalance, EmptyLatentImage, Image Comparer (rgthree), VRAM_Debug, CLIPTextEncode, VRAM_Debug, easy sam3ImageSegmentation, ConditioningAverage, CLIPTextEncode, VRAM_Debug, CR Upscale Image, ResizeMask, Florence2Run, Florence2ModelLoader, GetImageSize+, ImageScaleToTotalPixels, CR Upscale Image, VAEDecode, UNETLoader, LoraLoaderModelOnly, SetNode, LoraLoaderModelOnly, PreviewImage, CLIPLoader, VAELoader, LoraLoaderModelOnly, KSampler, SaveImage, 忽略多组孤海, SetNode, ComfyMathExpression, PrimitiveFloat, 孤海注释, 孤海注释, 孤海注释, SetNode, GetNode, 忽略多组孤海, GetNode, PrimitiveStringMultiline, Int, CLIPLoader, VAELoader, VAELoader, UNETLoader, LoadImage, PreviewImage, GenerateNoise, easy sam3ModelLoader, ImageScaleToTotalPixels, GetImageSize+, ImageScaleToTotalPixels, CLIPTextEncode, LGNoiseInjectionLatent, VAELoader, CheckpointLoaderSimple, ImageCompositeMasked, MaskPreview+, UltimateSDUpscaleNoUpscale, KSamplerSelect, BasicScheduler, SelfLiftH3Sampler, VAEDecode, 孤海注释, LoadImage, MiniMaxChunkFeedForward, SetNode, ModelPreviewOverrideKJ, MiniMaxH3SigmaShift]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors", "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "simple", "seed": 939104416406542, "steps": 8, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/AI 蛮子 Krea 2 中式MJ风格工作流V1.0_2100431779990691842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AI 蛮子 Krea 2 中式MJ风格工作流V1.0_2100431779990691842.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（117 个）：
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `孤海注释`
- `孤海注释`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `MiniMaxH3ImageToVideo`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `MathExpression|pysssss`
- `ConditioningZeroOut`
- `SetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SaveVideo`
- `ResolutionSelector`
- `GetNode`
- `孤海注释`
- `CreateVideo`
- `MarkdownNote`
- `VRAM_Debug`
- `孤海注释`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ConditioningKrea2Rebalance`
- `EmptyLatentImage` ★核心
- `Image Comparer (rgthree)`
- `VRAM_Debug`
- `CLIPTextEncode` ★核心
- `VRAM_Debug`
- `easy sam3ImageSegmentation`
- `ConditioningAverage`
- `CLIPTextEncode` ★核心
- `VRAM_Debug`
- `CR Upscale Image`
- `ResizeMask`
- `Florence2Run`
- `Florence2ModelLoader`
- `GetImageSize+`
- `ImageScaleToTotalPixels`
- `CR Upscale Image`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImage`
- `忽略多组孤海`
- `SetNode`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `SetNode`
- `GetNode`
- `忽略多组孤海`
- `GetNode`
- `PrimitiveStringMultiline`
- `Int`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `PreviewImage`
- `GenerateNoise`
- `easy sam3ModelLoader`
- `ImageScaleToTotalPixels`
- `GetImageSize+`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `LGNoiseInjectionLatent`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `ImageCompositeMasked`
- `MaskPreview+`
- `UltimateSDUpscaleNoUpscale`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SelfLiftH3Sampler` ★核心
- `VAEDecode` ★核心
- `孤海注释`
- `LoadImage`
- `MiniMaxChunkFeedForward`
- `SetNode`
- `ModelPreviewOverrideKJ`
- `MiniMaxH3SigmaShift`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`
- `seed` = `939104416406542`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `redcraftRedzimageUpdatedDEC03_redzimage15AIO.safetensors`

## 知识

覆盖率 **58%**（68/117）

**有卡**：`ImageResizeKJv2`、`MiniMaxH3ImageToVideo`、`VAEDecodeAudio`、`MathExpression|pysssss`、`ConditioningZeroOut`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxLowVRAMAttention`、`SaveVideo`、`ResolutionSelector`、`CreateVideo`、`VRAM_Debug`、`CLIPTextEncode`、`ConditioningKrea2Rebalance`、`EmptyLatentImage`、`easy sam3ImageSegmentation`、`ConditioningAverage`、`CR Upscale Image`、`ResizeMask`、`Florence2Run`、`Florence2ModelLoader`、`GetImageSize+`、`ImageScaleToTotalPixels`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`KSampler`、`SaveImage`、`忽略多组孤海`、`ComfyMathExpression`、`Int`、`LoadImage`、`GenerateNoise`、`easy sam3ModelLoader`、`LGNoiseInjectionLatent`、`CheckpointLoaderSimple`、`ImageCompositeMasked`、`MaskPreview+`、`UltimateSDUpscaleNoUpscale`、`KSamplerSelect`、`BasicScheduler`、`SelfLiftH3Sampler`、`MiniMaxChunkFeedForward`、`ModelPreviewOverrideKJ`、`MiniMaxH3SigmaShift`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
