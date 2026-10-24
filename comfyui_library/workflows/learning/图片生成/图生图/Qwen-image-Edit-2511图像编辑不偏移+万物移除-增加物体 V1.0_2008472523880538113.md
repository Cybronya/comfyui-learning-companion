---
key: 图片生成/图生图/Qwen-image-Edit-2511图像编辑不偏移+万物移除-增加物体 V1.0_2008472523880538113.json
name: Qwen-image-Edit-2511图像编辑不偏移+万物移除-增加物体 V1.0_2008472523880538113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image-Edit-2511图像编辑不偏移+万物移除-增加物体 V1.0_2008472523880538113.json
hash: 290af554c7870876
coverage: 0.826087
learned_at: 2026-10-23 11:18:03
nodes: [QwenEditAdaptiveLongestEdge, ConditioningZeroOut, VAEDecode, Note Plus (mtb), VAELoader, CLIPLoader, CropWithPadInfo, Note, SaveImage, QwenEditConfigPreparer, TextEncodeQwenImageEditPlusCustom_lrzjason, Label (rgthree), Note, Label (rgthree), Image Comparer (rgthree), Note, KSampler, QwenEditOutputExtractor, EasyCache, LoadImage, CR Text, Power Lora Loader (rgthree), UNETLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1003438867881779, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image-Edit-2511图像编辑不偏移+万物移除-增加物体 V1.0_2008472523880538113.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image-Edit-2511图像编辑不偏移+万物移除-增加物体 V1.0_2008472523880538113.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `QwenEditAdaptiveLongestEdge`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `Note Plus (mtb)`
- `VAELoader`
- `CLIPLoader`
- `CropWithPadInfo`
- `Note`
- `SaveImage`
- `QwenEditConfigPreparer`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `Label (rgthree)`
- `Note`
- `Label (rgthree)`
- `Image Comparer (rgthree)`
- `Note`
- `KSampler` ★核心
- `QwenEditOutputExtractor`
- `EasyCache`
- `LoadImage`
- `CR Text`
- `Power Lora Loader (rgthree)`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `1003438867881779`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`QwenEditAdaptiveLongestEdge`、`ConditioningZeroOut`、`VAEDecode`、`Note Plus (mtb)`、`VAELoader`、`CLIPLoader`、`CropWithPadInfo`、`SaveImage`、`QwenEditConfigPreparer`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`Label (rgthree)`、`KSampler`、`QwenEditOutputExtractor`、`EasyCache`、`LoadImage`、`CR Text`、`Power Lora Loader (rgthree)`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、SaveImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
