---
key: 图片生成/文生图/FluxToQwenEdit-NextSceneLora_ 6场景 角色一致性工作流_1979459859504599042.json
name: FluxToQwenEdit-NextSceneLora_ 6场景 角色一致性工作流_1979459859504599042
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FluxToQwenEdit-NextSceneLora_ 6场景 角色一致性工作流_1979459859504599042.json
hash: ade889c8cb2c83f7
coverage: 0.642105
learned_at: 2026-10-10 20:58:36
nodes: [EmptySD3LatentImage, KSampler, ConditioningZeroOut, CLIPTextEncode, CFGNorm, ModelSamplingAuraFlow, KSampler, VAEEncode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, SetNode, SetNode, SetNode, CFGNorm, ModelSamplingAuraFlow, KSampler, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, VAEEncode, CFGNorm, ModelSamplingAuraFlow, KSampler, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, VAEEncode, CFGNorm, ModelSamplingAuraFlow, KSampler, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, VAEEncode, CFGNorm, ModelSamplingAuraFlow, KSampler, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, VAEEncode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), UNETLoader, DualCLIPLoader, LoraLoaderModelOnly, VAELoader, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, Note, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Note, VAEDecode, SetNode, VAEDecode, SetNode, VAEDecode, VAEDecode, VAEDecode, SetNode, SetNode, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, VAEDecode, easy cleanGpuUsed, SaveImage]
patterns: [image_to_image]
missing: [easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 8650324624072, "steps": 4}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/FluxToQwenEdit-NextSceneLora_ 6场景 角色一致性工作流_1979459859504599042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FluxToQwenEdit-NextSceneLora_ 6场景 角色一致性工作流_1979459859504599042.json`

## 结构

**节点**（95 个）：
- `EmptySD3LatentImage`
- `KSampler`
- `ConditioningZeroOut`
- `CLIPTextEncode`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler`
- `VAEEncode`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `SetNode`
- `SetNode`
- `SetNode`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `VAEEncode`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `VAEEncode`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `VAEEncode`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `VAEEncode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader`
- `DualCLIPLoader`
- `LoraLoaderModelOnly`
- `VAELoader`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `LoraLoaderModelOnly`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `VAEDecode`
- `SetNode`
- `VAEDecode`
- `SetNode`
- `VAEDecode`
- `VAEDecode`
- `VAEDecode`
- `SetNode`
- `SetNode`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `VAEDecode`
- `easy cleanGpuUsed`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `8650324624072`
- `steps` = `4`

## 知识

覆盖率 **64%**（61/95）

**有卡**：`EmptySD3LatentImage`、`KSampler`、`ConditioningZeroOut`、`CLIPTextEncode`、`CFGNorm`、`ModelSamplingAuraFlow`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`ImageScaleToTotalPixels`、`SetNode`、`GetNode`、`LoadImage`

**缺卡**（1）：`easy cleanGpuUsed`

## 参数体检

发现 5 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
