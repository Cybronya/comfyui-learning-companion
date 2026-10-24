---
key: 图片生成/图生图/Qwen 图生图 三视图 多视图 nunchaku-Qwen-image_2041532075769073665.json
name: Qwen 图生图 三视图 多视图 nunchaku-Qwen-image_2041532075769073665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen 图生图 三视图 多视图 nunchaku-Qwen-image_2041532075769073665.json
hash: 18f776b92eb90b80
coverage: 0.956522
learned_at: 2026-10-23 11:14:34
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy anythingIndexSwitch, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy anythingIndexSwitch, easy imageBatchToImageList, NunchakuQwenImageDiTLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, CFGNorm, ModelSamplingAuraFlow, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEdit, KSampler, MathExpression|pysssss, EmptyLatentImage, Text Load Line From File, ImageScaleToTotalPixels, ImageScaleToTotalPixels, easy forLoopStart, Any Switch (rgthree), VAEDecode, WujiCleaner, easy batchAnything, WujiCleaner, Text Multiline, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, easy imageListToImageBatch, SaveImage, Mute / Bypass Repeater (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Bypasser (rgthree), easy forLoopEnd, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1440, "sampler_name": "euler", "scheduler": "simple", "seed": 509025751835382, "steps": 4, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen 图生图 三视图 多视图 nunchaku-Qwen-image_2041532075769073665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen 图生图 三视图 多视图 nunchaku-Qwen-image_2041532075769073665.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
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
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy anythingIndexSwitch`
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
- `LoadImage`
- `LoadImage`
- `easy anythingIndexSwitch`
- `easy imageBatchToImageList`
- `NunchakuQwenImageDiTLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEdit`
- `KSampler` ★核心
- `MathExpression|pysssss`
- `EmptyLatentImage` ★核心
- `Text Load Line From File`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `easy forLoopStart`
- `Any Switch (rgthree)`
- `VAEDecode` ★核心
- `WujiCleaner`
- `easy batchAnything`
- `WujiCleaner`
- `Text Multiline`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `easy imageListToImageBatch`
- `SaveImage`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `easy forLoopEnd`
- `LoadImage`

## 关键参数

- `seed` = `509025751835382`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `720`
- `height` = `1440`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（66/69）

**有卡**：`LoadImage`、`easy anythingIndexSwitch`、`easy imageBatchToImageList`、`NunchakuQwenImageDiTLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CFGNorm`、`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`TextEncodeQwenImageEdit`、`KSampler`、`MathExpression|pysssss`、`EmptyLatentImage`、`Text Load Line From File`、`ImageScaleToTotalPixels`、`easy forLoopStart`、`VAEDecode`、`WujiCleaner`、`easy batchAnything`、`Text Multiline`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`easy imageListToImageBatch`、`SaveImage`、`Mute / Bypass Repeater (rgthree)`、`Fast Bypasser (rgthree)`、`easy forLoopEnd`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
