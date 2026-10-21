---
key: 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜与关键帧全流程提示词_2104790428624183297.json
name: FireRed-Image-Edit 1.1-单图一键生成专业影视分镜与关键帧全流程提示词_2104790428624183297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜与关键帧全流程提示词_2104790428624183297.json
hash: b69dc97b2f547a3f
coverage: 0.769231
learned_at: 2026-10-21 00:39:20
nodes: [CLIPLoader, VAELoader, ProcessString, CFGNorm, LoraLoaderModelOnly, LoraLoaderModelOnly, JDCN_StringToList, PreviewImage, ResolutionSelector, PrimitiveStringMultiline, CustomCombo, Int2String, Int2String, Text Find and Replace, llama_cpp_model_loader, llama_cpp_parameters, CR Text Replace, PrimitiveInt, SaveImage, PrimitiveInt, ModelSamplingAuraFlow, UNETLoader, llama_cpp_instruct_adv, TextEncodeQwenImageEditPlusAdvance_lrzjason, KSampler, VAEDecode, PrimitiveNode, CR Text, RH_LLMAPI_NODE, TextEncodeQwenImageEditPlus, easy showAnything, BatchImagesNode, LoadImage, LoadImage, CR Text, CR Text, PrimitiveStringMultiline, ShowText|pysssss, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 764128636816292, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜与关键帧全流程提示词_2104790428624183297.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜与关键帧全流程提示词_2104790428624183297.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `CLIPLoader`
- `VAELoader`
- `ProcessString`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `JDCN_StringToList`
- `PreviewImage`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `CustomCombo`
- `Int2String`
- `Int2String`
- `Text Find and Replace`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `CR Text Replace`
- `PrimitiveInt`
- `SaveImage`
- `PrimitiveInt`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `llama_cpp_instruct_adv`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PrimitiveNode`
- `CR Text`
- `RH_LLMAPI_NODE`
- `TextEncodeQwenImageEditPlus`
- `easy showAnything`
- `BatchImagesNode`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `CR Text`
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `764128636816292`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **77%**（30/39）

**有卡**：`CLIPLoader`、`VAELoader`、`ProcessString`、`CFGNorm`、`LoraLoaderModelOnly`、`JDCN_StringToList`、`ResolutionSelector`、`CustomCombo`、`Int2String`、`Text Find and Replace`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`CR Text Replace`、`SaveImage`、`ModelSamplingAuraFlow`、`UNETLoader`、`llama_cpp_instruct_adv`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`KSampler`、`VAEDecode`、`CR Text`、`RH_LLMAPI_NODE`、`TextEncodeQwenImageEditPlus`、`BatchImagesNode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
