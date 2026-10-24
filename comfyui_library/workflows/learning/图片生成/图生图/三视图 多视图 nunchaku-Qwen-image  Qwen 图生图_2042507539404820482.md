---
key: 图片生成/图生图/三视图 多视图 nunchaku-Qwen-image  Qwen 图生图_2042507539404820482.json
name: 三视图 多视图 nunchaku-Qwen-image  Qwen 图生图_2042507539404820482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/三视图 多视图 nunchaku-Qwen-image  Qwen 图生图_2042507539404820482.json
hash: 13d624e0ed6104f0
coverage: 0.956522
learned_at: 2026-10-23 12:02:03
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy anythingIndexSwitch, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy anythingIndexSwitch, LoadImage, NunchakuQwenImageDiTLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, CFGNorm, Text Load Line From File, ImageScaleToTotalPixels, MathExpression|pysssss, ImageScaleToTotalPixels, Any Switch (rgthree), Mute / Bypass Repeater (rgthree), TextEncodeQwenImageEdit, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), KSampler, WujiCleaner, VAEDecode, WujiCleaner, easy forLoopEnd, easy batchAnything, TextEncodeQwenImageEditPlus, Text Multiline, easy forLoopStart, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy imageBatchToImageList, easy imageListToImageBatch, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPLoader, VAELoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1440, "sampler_name": "euler", "scheduler": "simple", "seed": 571355153073598, "steps": 4, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/三视图 多视图 nunchaku-Qwen-image  Qwen 图生图_2042507539404820482.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/三视图 多视图 nunchaku-Qwen-image  Qwen 图生图_2042507539404820482.json`

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
- `LoadImage`
- `NunchakuQwenImageDiTLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `Text Load Line From File`
- `ImageScaleToTotalPixels`
- `MathExpression|pysssss`
- `ImageScaleToTotalPixels`
- `Any Switch (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `TextEncodeQwenImageEdit`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `WujiCleaner`
- `VAEDecode` ★核心
- `WujiCleaner`
- `easy forLoopEnd`
- `easy batchAnything`
- `TextEncodeQwenImageEditPlus`
- `Text Multiline`
- `easy forLoopStart`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`

## 关键参数

- `seed` = `571355153073598`
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

**有卡**：`LoadImage`、`easy anythingIndexSwitch`、`NunchakuQwenImageDiTLoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`CFGNorm`、`Text Load Line From File`、`ImageScaleToTotalPixels`、`MathExpression|pysssss`、`Mute / Bypass Repeater (rgthree)`、`TextEncodeQwenImageEdit`、`Fast Bypasser (rgthree)`、`KSampler`、`WujiCleaner`、`VAEDecode`、`easy forLoopEnd`、`easy batchAnything`、`TextEncodeQwenImageEditPlus`、`Text Multiline`、`easy forLoopStart`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
