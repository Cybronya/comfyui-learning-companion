---
key: 图片生成/图生图/qwen-edit-图片精修-深度优化版4.0_2013194815093084162.json
name: qwen-edit-图片精修-深度优化版4.0_2013194815093084162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-edit-图片精修-深度优化版4.0_2013194815093084162.json
hash: 6f19ab6b7da70b3f
coverage: 0.771429
learned_at: 2026-10-23 11:42:36
nodes: [GetNode, GetNode, CR Text, CR Text, CR Text, ConditioningZeroOut, ModelSamplingAuraFlow, GetNode, VAEDecode, SaveImage, SetNode, SetNode, SetNode, SaveImage, Image Comparer (rgthree), GetNode, KSampler, CFGNorm, Seed (rgthree), QwenEditConfigPreparer, TextEncodeQwenImageEditPlusCustom_lrzjason, LoadImage, easy imageScaleDownToSize, CR Text, easy anythingIndexSwitch, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy int, MuyeTextEditOutput, LoraLoaderModelOnly, CR Index]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 748263678094236, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen-edit-图片精修-深度优化版4.0_2013194815093084162.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-edit-图片精修-深度优化版4.0_2013194815093084162.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `GetNode`
- `GetNode`
- `CR Text`
- `CR Text`
- `CR Text`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `GetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `GetNode`
- `KSampler` ★核心
- `CFGNorm`
- `Seed (rgthree)`
- `QwenEditConfigPreparer`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `LoadImage`
- `easy imageScaleDownToSize`
- `CR Text`
- `easy anythingIndexSwitch`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `easy int`
- `MuyeTextEditOutput`
- `LoraLoaderModelOnly` ★核心
- `CR Index`

## 关键参数

- `seed` = `748263678094236`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`CR Text`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`VAEDecode`、`SaveImage`、`KSampler`、`CFGNorm`、`Seed (rgthree)`、`QwenEditConfigPreparer`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`LoadImage`、`easy imageScaleDownToSize`、`easy anythingIndexSwitch`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`easy int`、`MuyeTextEditOutput`、`CR Index`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、SaveImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
