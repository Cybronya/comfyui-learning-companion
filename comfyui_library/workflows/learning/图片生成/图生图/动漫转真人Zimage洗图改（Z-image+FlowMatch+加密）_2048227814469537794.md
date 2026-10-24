---
key: 图片生成/图生图/动漫转真人Zimage洗图改（Z-image+FlowMatch+加密）_2048227814469537794.json
name: 动漫转真人Zimage洗图改（Z-image+FlowMatch+加密）_2048227814469537794
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/动漫转真人Zimage洗图改（Z-image+FlowMatch+加密）_2048227814469537794.json
hash: 5c9028823a699a22
coverage: 0.666667
learned_at: 2026-10-23 12:27:50
nodes: [llama_cpp_unload_model, easy cleanGpuUsed, SetNode, CLIPLoader, SetNode, SetNode, VAELoader, SamplerCustom, CLIPLoader, easy cleanGpuUsed, KSamplerSelect, ImpactExecutionOrderController, VAELoader, VAEDecode, GetNode, SetNode, GetNode, ImpactExecutionOrderController, UNETLoader, UNETLoader, CLIPTextEncode, ConditioningZeroOut, VAEEncode, SetNode, FlowMatchEulerDiscreteScheduler (Custom), GetNode, ImpactExecutionOrderController, GetNode, JoinStrings, ConditioningZeroOut, QwenEditOutputExtractor_EditUtils, VAEDecode, SplitSigmasDenoise, CropWithPadInfo_EditUtils, SetNode, GetNode, GetNode, GetNode, GetNode, easy loraStackApply, KSampler, CFGNorm, ModelSamplingAuraFlow, QwenEditTextEncode_EditUtils, GetNode, easy showAnything, llama_cpp_instruct_adv, JjkText, easy loraStack, JjkText, llama_cpp_model_loader, llama_cpp_parameters, LoadImage, CompressImages]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 371114511916710, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/动漫转真人Zimage洗图改（Z-image+FlowMatch+加密）_2048227814469537794.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/动漫转真人Zimage洗图改（Z-image+FlowMatch+加密）_2048227814469537794.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（54 个）：
- `llama_cpp_unload_model`
- `easy cleanGpuUsed`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SamplerCustom` ★核心
- `CLIPLoader`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `ImpactExecutionOrderController`
- `VAELoader`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `ImpactExecutionOrderController`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `SetNode`
- `FlowMatchEulerDiscreteScheduler (Custom)`
- `GetNode`
- `ImpactExecutionOrderController`
- `GetNode`
- `JoinStrings`
- `ConditioningZeroOut`
- `QwenEditOutputExtractor_EditUtils`
- `VAEDecode` ★核心
- `SplitSigmasDenoise`
- `CropWithPadInfo_EditUtils`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy loraStackApply`
- `KSampler` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `QwenEditTextEncode_EditUtils`
- `GetNode`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `JjkText`
- `easy loraStack`
- `JjkText`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `LoadImage`
- `CompressImages`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `371114511916710`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **67%**（36/54）

**有卡**：`llama_cpp_unload_model`、`easy cleanGpuUsed`、`CLIPLoader`、`VAELoader`、`SamplerCustom`、`KSamplerSelect`、`ImpactExecutionOrderController`、`VAEDecode`、`UNETLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEEncode`、`FlowMatchEulerDiscreteScheduler (Custom)`、`JoinStrings`、`QwenEditOutputExtractor_EditUtils`、`SplitSigmasDenoise`、`CropWithPadInfo_EditUtils`、`easy loraStackApply`、`KSampler`、`CFGNorm`、`ModelSamplingAuraFlow`、`QwenEditTextEncode_EditUtils`、`llama_cpp_instruct_adv`、`easy loraStack`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`LoadImage`、`CompressImages`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
