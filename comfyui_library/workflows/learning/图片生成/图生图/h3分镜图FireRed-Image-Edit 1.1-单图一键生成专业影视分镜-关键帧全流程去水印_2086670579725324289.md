---
key: 图片生成/图生图/h3分镜图FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程去水印_2086670579725324289.json
name: h3分镜图FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程去水印_2086670579725324289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/h3分镜图FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程去水印_2086670579725324289.json
hash: 27806353095333bd
coverage: 0.541667
learned_at: 2026-10-10 20:48:11
nodes: [SaveImage, LoadImage, JjkText, MultiTextConcatenate, MultiTextConcatenate, JjkText, JjkText, ttN concat, JjkText, MultiTextConcatenate, ttN concat, JjkText, TextEncodeQwenImageEditPlusAdvance_lrzjason, ModelSamplingAuraFlow, LoraLoaderModelOnly, GetNode, JDCN_StringToList, TextEncodeQwenImageEditPlus, UNETLoader, KSampler, ProcessString, LoraLoaderModelOnly, CFGNorm, VAELoader, CLIPLoader, Anything Everywhere3, GetNode, RH_LLMAPI_NODE, Note, Note, SetNode, SetNode, llama_cpp_instruct_adv, easy showAnything, llama_cpp_model_loader, ttN concat, llama_cpp_parameters, JjkText, JjkText, CR Text, LoadImage, JjkText, GetNode, SaveImage, CustomAddLabel, SaveImage, SetNode, VAEDecode]
patterns: []
missing: [CR Text, ttN concat, ttN concat, ttN concat]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 163934655761955, "steps": 6}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识, 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识, 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/h3分镜图FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程去水印_2086670579725324289.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/h3分镜图FireRed-Image-Edit 1.1-单图一键生成专业影视分镜-关键帧全流程去水印_2086670579725324289.json`

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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ProcessString`
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `VAELoader`
- `CLIPLoader`
- `Anything Everywhere3`
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
- `llama_cpp_parameters`
- `JjkText`
- `JjkText`
- `CR Text`
- `LoadImage`
- `JjkText`
- `GetNode`
- `SaveImage`
- `CustomAddLabel`
- `SaveImage`
- `SetNode`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `163934655761955`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **54%**（26/48）

**有卡**：`SaveImage`、`LoadImage`、`MultiTextConcatenate`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`JDCN_StringToList`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`KSampler`、`ProcessString`、`CFGNorm`、`VAELoader`、`CLIPLoader`、`RH_LLMAPI_NODE`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`CustomAddLabel`、`VAEDecode`

**缺卡**（4）：`CR Text`、`ttN concat`、`ttN concat`、`ttN concat`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
