---
key: 图片生成/文生图/FluxToQwenEdit-NextSceneLora_ 6场景 角色一致性工作流_1979459859504599042.json
name: FluxToQwenEdit-NextSceneLora_ 6场景 角色一致性工作流_1979459859504599042.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FluxToQwenEdit-NextSceneLora_ 6场景 角色一致性工作流_1979459859504599042.json
hash: ade889c8cb2c83f7
coverage: 0.642105
learned_at: 2026-10-07 19:34:51
nodes: [EmptySD3LatentImage, KSampler, ConditioningZeroOut, CLIPTextEncode, CFGNorm, ModelSamplingAuraFlow, KSampler, VAEEncode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, SetNode, SetNode, SetNode, CFGNorm, ModelSamplingAuraFlow, KSampler, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, VAEEncode, CFGNorm, ModelSamplingAuraFlow, KSampler, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, VAEEncode, CFGNorm, ModelSamplingAuraFlow, KSampler, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, VAEEncode, CFGNorm, ModelSamplingAuraFlow, KSampler, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, VAEEncode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), UNETLoader, DualCLIPLoader, LoraLoaderModelOnly, VAELoader, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, Note, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Note, VAEDecode, SetNode, VAEDecode, SetNode, VAEDecode, VAEDecode, VAEDecode, SetNode, SetNode, SaveImage, SaveImage, SaveImage, SaveImage, SaveImage, VAEDecode, easy cleanGpuUsed, SaveImage]
patterns: [image_to_image]
missing: [easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 8650324624072, "steps": 4}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/FluxToQwenEdit-NextSceneLora_ 6场景 角色一致性工作流_1979459859504599042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1979459859504599042.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `SetNode`
- `SetNode`
- `SetNode`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
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
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `VAEDecode` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `8650324624072`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（61/95）

**有卡**：`EmptySD3LatentImage`、`KSampler`、`ConditioningZeroOut`、`CLIPTextEncode`、`CFGNorm`、`ModelSamplingAuraFlow`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`ImageScaleToTotalPixels`、`LoadImage`、`UNETLoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`SaveImage`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

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
