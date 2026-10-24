---
key: 图片生成/图生图/Qwen-image角色IP多视图极速2.0版（男女二合一，默认女）_2027563789377347586.json
name: Qwen-image角色IP多视图极速2.0版（男女二合一，默认女）_2027563789377347586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image角色IP多视图极速2.0版（男女二合一，默认女）_2027563789377347586.json
hash: 39cfaa65dfda56a3
coverage: 0.942857
learned_at: 2026-10-23 11:18:43
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy anythingIndexSwitch, NunchakuQwenImageDiTLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, CFGNorm, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, Text Multiline, easy forLoopStart, MathExpression|pysssss, KSampler, Text Load Line From File, ImageScaleToTotalPixels, TextEncodeQwenImageEdit, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), SaveImage, easy forLoopEnd, EmptyLatentImage, Any Switch (rgthree), ImageScaleToTotalPixels, Mute / Bypass Repeater (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy anythingIndexSwitch, PreviewImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, easy imageBatchToImageList, easy imageListToImageBatch, easy batchAnything, VAEDecode, WujiCleaner, WujiCleaner, LoadImage, Fast Groups Bypasser (rgthree), LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1440, "sampler_name": "euler", "scheduler": "simple", "seed": 307570505699436, "steps": 4, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image角色IP多视图极速2.0版（男女二合一，默认女）_2027563789377347586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image角色IP多视图极速2.0版（男女二合一，默认女）_2027563789377347586.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
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
- `NunchakuQwenImageDiTLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `Text Multiline`
- `easy forLoopStart`
- `MathExpression|pysssss`
- `KSampler` ★核心
- `Text Load Line From File`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEdit`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `easy forLoopEnd`
- `EmptyLatentImage` ★核心
- `Any Switch (rgthree)`
- `ImageScaleToTotalPixels`
- `Mute / Bypass Repeater (rgthree)`
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
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy batchAnything`
- `VAEDecode` ★核心
- `WujiCleaner`
- `WujiCleaner`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`

## 关键参数

- `seed` = `307570505699436`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `720`
- `height` = `1440`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（66/70）

**有卡**：`LoadImage`、`easy anythingIndexSwitch`、`NunchakuQwenImageDiTLoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`CFGNorm`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`Text Multiline`、`easy forLoopStart`、`MathExpression|pysssss`、`KSampler`、`Text Load Line From File`、`ImageScaleToTotalPixels`、`TextEncodeQwenImageEdit`、`Fast Bypasser (rgthree)`、`SaveImage`、`easy forLoopEnd`、`EmptyLatentImage`、`Mute / Bypass Repeater (rgthree)`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`easy imageBatchToImageList`、`easy imageListToImageBatch`、`easy batchAnything`、`VAEDecode`、`WujiCleaner`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
