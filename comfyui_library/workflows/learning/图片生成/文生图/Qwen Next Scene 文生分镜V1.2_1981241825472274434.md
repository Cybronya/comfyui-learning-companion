---
key: 图片生成/文生图/Qwen Next Scene 文生分镜V1.2_1981241825472274434.json
name: Qwen Next Scene 文生分镜V1.2_1981241825472274434.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Next Scene 文生分镜V1.2_1981241825472274434.json
hash: c10e1aeaea22d862
coverage: 0.820513
learned_at: 2026-10-09 19:56:21
nodes: [KSampler, VAEEncode, easy promptLine, VAEDecode, easy showAnything, UNETLoader, ProcessString, TextEncodeQwenImageEditPlus, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, CLIPTextEncode, ConditioningZeroOut, Anything Everywhere3, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, LayerUtility: ImageScaleByAspectRatio V2, MinNode, FluxResolutionNode, RH_Translator, InversionDemoLazySwitch, RH_Translator, InversionDemoLazySwitch, RH_Translator, InversionDemoLazySwitch, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, VAEDecode, SaveImage, JjkText, VAEDecode, JjkText, EmptySD3LatentImage, JjkText, SaveImage, PrimitiveBoolean, LoadImage]
patterns: [image_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy promptLine]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 792342327315534, "steps": 4}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Next Scene 文生分镜V1.2_1981241825472274434.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1981241825472274434.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `KSampler` ★核心
- `VAEEncode` ★核心
- `easy promptLine`
- `VAEDecode` ★核心
- `easy showAnything`
- `UNETLoader` ★核心
- `ProcessString`
- `TextEncodeQwenImageEditPlus`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MinNode`
- `FluxResolutionNode`
- `RH_Translator`
- `InversionDemoLazySwitch`
- `RH_Translator`
- `InversionDemoLazySwitch`
- `RH_Translator`
- `InversionDemoLazySwitch`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `JjkText`
- `VAEDecode` ★核心
- `JjkText`
- `EmptySD3LatentImage`
- `JjkText`
- `SaveImage`
- `PrimitiveBoolean`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `792342327315534`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`KSampler`、`VAEEncode`、`VAEDecode`、`UNETLoader`、`ProcessString`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`MinNode`、`FluxResolutionNode`、`RH_Translator`、`InversionDemoLazySwitch`、`SaveImage`、`EmptySD3LatentImage`、`PrimitiveBoolean`、`LoadImage`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`easy promptLine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
