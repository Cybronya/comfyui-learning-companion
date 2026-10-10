---
key: QwenImageEdit-Plus有无LORA效果对比测试_1978372865714229249.json
name: QwenImageEdit-Plus有无LORA效果对比测试_1978372865714229249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImageEdit-Plus有无LORA效果对比测试_1978372865714229249.json
hash: 4873a2bdacae0438
coverage: 0.818182
learned_at: 2026-10-10 20:59:07
nodes: [ModelSamplingAuraFlow, CFGNorm, KSampler, SaveImage, SaveImage, ImageStitch, LayerUtility: PurgeVRAM V2, ModelSamplingAuraFlow, CFGNorm, KSampler, SaveImage, SaveImage, ImageStitch, LayerUtility: PurgeVRAM V2, CLIPLoader, GetImageSize, ConditioningZeroOut, EmptySD3LatentImage, VAELoader, PrimitiveInt, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, VAEDecode, VAEDecode, ImageBatch, ImageBatch, easy joinImageBatch, PreviewImage, Text Multiline, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, Text Multiline, easy joinImageBatch]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 476602248560184, "steps": 8}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy joinImageBatch` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# QwenImageEdit-Plus有无LORA效果对比测试_1978372865714229249.json

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

覆盖率 **82%**（27/33）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`KSampler`、`SaveImage`、`ImageStitch`、`CLIPLoader`、`GetImageSize`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`ImageScaleToTotalPixels`、`VAEDecode`、`ImageBatch`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`

**缺卡**（4）：`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`Text Multiline`、`easy joinImageBatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy joinImageBatch` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
