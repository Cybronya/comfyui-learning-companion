---
key: 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2111795349353488385.json
name: FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2111795349353488385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2111795349353488385.json
hash: 166b97a0268b8550
coverage: 0.625
learned_at: 2026-10-23 10:55:35
nodes: [SaveImage, LoadImage, JjkText, MultiTextConcatenate, MultiTextConcatenate, JjkText, JjkText, ttN concat, JjkText, MultiTextConcatenate, ttN concat, JjkText, TextEncodeQwenImageEditPlusAdvance_lrzjason, ModelSamplingAuraFlow, LoraLoaderModelOnly, GetNode, JDCN_StringToList, TextEncodeQwenImageEditPlus, VAEDecode, SetNode, UNETLoader, KSampler, ProcessString, LoraLoaderModelOnly, CFGNorm, VAELoader, CLIPLoader, Anything Everywhere3, CR Text, SaveImage, GetNode, CustomAddLabel, SaveImage, GetNode, RH_LLMAPI_NODE, Note, Note, SetNode, SetNode, llama_cpp_instruct_adv, easy showAnything, llama_cpp_model_loader, ttN concat, JjkText, llama_cpp_parameters, JjkText, JjkText, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 1074746429910716, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2111795349353488385.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程提示词_2111795349353488385.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

**节点**（48 个）：
- `SaveImage`
- `LoadImage`
- `JjkText`
- `MultiTextConcatenate`
- `MultiTextConcatenate`
- `JjkText`
- `JjkText`
- `ttN concat`
- `JjkText`
- `MultiTextConcatenate`
- `ttN concat`
- `JjkText`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `JDCN_StringToList`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `SetNode`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ProcessString`
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `VAELoader`
- `CLIPLoader`
- `Anything Everywhere3`
- `CR Text`
- `SaveImage`
- `GetNode`
- `CustomAddLabel`
- `SaveImage`
- `GetNode`
- `RH_LLMAPI_NODE`
- `Note`
- `Note`
- `SetNode`
- `SetNode`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `llama_cpp_model_loader`
- `ttN concat`
- `JjkText`
- `llama_cpp_parameters`
- `JjkText`
- `JjkText`
- `LoadImage`

## 关键参数

- `seed` = `1074746429910716`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **62%**（30/48）

**有卡**：`SaveImage`、`LoadImage`、`MultiTextConcatenate`、`ttN concat`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`JDCN_StringToList`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`UNETLoader`、`KSampler`、`ProcessString`、`CFGNorm`、`VAELoader`、`CLIPLoader`、`CR Text`、`CustomAddLabel`、`RH_LLMAPI_NODE`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
