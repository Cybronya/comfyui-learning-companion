---
key: 图片生成/文生图/QwenImageEdit-Plus有无LORA效果对比测试_1978372865714229249.json
name: QwenImageEdit-Plus有无LORA效果对比测试_1978372865714229249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImageEdit-Plus有无LORA效果对比测试_1978372865714229249.json
hash: 4873a2bdacae0438
coverage: 0.939394
learned_at: 2026-10-15 22:27:25
nodes: [ModelSamplingAuraFlow, CFGNorm, KSampler, SaveImage, SaveImage, ImageStitch, LayerUtility: PurgeVRAM V2, ModelSamplingAuraFlow, CFGNorm, KSampler, SaveImage, SaveImage, ImageStitch, LayerUtility: PurgeVRAM V2, CLIPLoader, GetImageSize, ConditioningZeroOut, EmptySD3LatentImage, VAELoader, PrimitiveInt, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, VAEDecode, VAEDecode, ImageBatch, ImageBatch, easy joinImageBatch, PreviewImage, Text Multiline, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 476602248560184, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/QwenImageEdit-Plus有无LORA效果对比测试_1978372865714229249.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QwenImageEdit-Plus有无LORA效果对比测试_1978372865714229249.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `ImageStitch`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `ImageStitch`
- `LayerUtility: PurgeVRAM V2`
- `CLIPLoader`
- `GetImageSize`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `VAELoader`
- `PrimitiveInt`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageBatch`
- `ImageBatch`
- `easy joinImageBatch`
- `PreviewImage`
- `Text Multiline`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

## 关键参数

- `seed` = `476602248560184`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`KSampler`、`SaveImage`、`ImageStitch`、`LayerUtility: PurgeVRAM V2`、`CLIPLoader`、`GetImageSize`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`ImageScaleToTotalPixels`、`VAEDecode`、`ImageBatch`、`easy joinImageBatch`、`Text Multiline`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
