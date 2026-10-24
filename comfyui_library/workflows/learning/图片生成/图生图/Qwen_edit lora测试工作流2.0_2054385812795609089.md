---
key: 图片生成/图生图/Qwen_edit lora测试工作流2.0_2054385812795609089.json
name: Qwen_edit lora测试工作流2.0_2054385812795609089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_edit lora测试工作流2.0_2054385812795609089.json
hash: 372b8349f83947c9
coverage: 0.591398
learned_at: 2026-10-23 11:21:22
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, ImageListToBatch+, VAEDecode, JoinStrings, VAEDecode, CR Float To String, Anything Everywhere, String, ConditioningZeroOut, ImpactMakeImageList, Create Grid Image from Batch, Anything Everywhere, Anything Everywhere, CLIPLoader, VAELoader, SetNode, Note, easy rangeFloat, Note, TextEncodeQwenImageEditPlusAdvance_lrzjason, GetNode, GetNode, GetNode, Lora Loader, ConditioningZeroOut, KSampler, KSampler, AddLabel, AddLabel, GetNode, GetNode, TextEncodeQwenImageEditPlusAdvance_lrzjason, ModelSamplingAuraFlow, CFGNorm, GetNode, JoinStrings, VAEDecode, TextEncodeQwenImageEditPlusAdvance_lrzjason, GetNode, GetNode, GetNode, ConditioningZeroOut, KSampler, ModelSamplingAuraFlow, CFGNorm, GetNode, JoinStrings, VAEDecode, TextEncodeQwenImageEditPlusAdvance_lrzjason, GetNode, GetNode, GetNode, ConditioningZeroOut, KSampler, ModelSamplingAuraFlow, CFGNorm, GetNode, JoinStrings, VAEDecode, TextEncodeQwenImageEditPlusAdvance_lrzjason, GetNode, GetNode, GetNode, ConditioningZeroOut, KSampler, ModelSamplingAuraFlow, CFGNorm, Note, Note, Note, Note, Note, Note, Note, Note, Lora Loader, Lora Loader, Lora Loader, Text _O, LoadImage, LoraLoaderModelOnly, UNETLoader, AddLabel, AddLabel, AddLabel, Fast Groups Bypasser (rgthree), ImpactInt, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 416724775987621, "steps": 30}
---

# 图片生成/图生图/Qwen_edit lora测试工作流2.0_2054385812795609089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_edit lora测试工作流2.0_2054385812795609089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageListToBatch+`
- `VAEDecode` ★核心
- `JoinStrings`
- `VAEDecode` ★核心
- `CR Float To String`
- `Anything Everywhere`
- `String`
- `ConditioningZeroOut`
- `ImpactMakeImageList`
- `Create Grid Image from Batch`
- `Anything Everywhere`
- `Anything Everywhere`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `Note`
- `easy rangeFloat`
- `Note`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `GetNode`
- `GetNode`
- `GetNode`
- `Lora Loader`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `KSampler` ★核心
- `AddLabel`
- `AddLabel`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `GetNode`
- `JoinStrings`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `GetNode`
- `JoinStrings`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `GetNode`
- `JoinStrings`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Lora Loader`
- `Lora Loader`
- `Lora Loader`
- `Text _O`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `Fast Groups Bypasser (rgthree)`
- `ImpactInt`
- `SaveImage`

## 关键参数

- `seed` = `416724775987621`
- `steps` = `30`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **59%**（55/93）

**有卡**：`ImageListToBatch+`、`VAEDecode`、`JoinStrings`、`CR Float To String`、`String`、`ConditioningZeroOut`、`ImpactMakeImageList`、`Create Grid Image from Batch`、`CLIPLoader`、`VAELoader`、`easy rangeFloat`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`Lora Loader`、`KSampler`、`AddLabel`、`ModelSamplingAuraFlow`、`CFGNorm`、`Text _O`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`、`ImpactInt`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
