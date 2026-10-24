---
key: 图片生成/图生图/FireRed-Image-Edit 1.1分镜关键帧生成｜单图直出影视级分镜｜全流程提示词_2112052555575554049.json
name: FireRed-Image-Edit 1.1分镜关键帧生成｜单图直出影视级分镜｜全流程提示词_2112052555575554049
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1分镜关键帧生成｜单图直出影视级分镜｜全流程提示词_2112052555575554049.json
hash: a8a51855e0e1a612
coverage: 0.775281
learned_at: 2026-10-23 10:55:38
nodes: [SaveImage, LoadImage, JjkText, MultiTextConcatenate, MultiTextConcatenate, JjkText, JjkText, ttN concat, JjkText, MultiTextConcatenate, ttN concat, JjkText, TextEncodeQwenImageEditPlusAdvance_lrzjason, ModelSamplingAuraFlow, LoraLoaderModelOnly, GetNode, JDCN_StringToList, TextEncodeQwenImageEditPlus, VAEDecode, SetNode, UNETLoader, KSampler, ProcessString, LoraLoaderModelOnly, CFGNorm, VAELoader, CLIPLoader, Anything Everywhere3, CR Text, SaveImage, GetNode, CustomAddLabel, SaveImage, GetNode, RH_LLMAPI_NODE, SetNode, SetNode, llama_cpp_instruct_adv, easy showAnything, llama_cpp_model_loader, ttN concat, JjkText, llama_cpp_parameters, JjkText, JjkText, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1分镜关键帧生成｜单图直出影视级分镜｜全流程提示词_2112052555575554049.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1分镜关键帧生成｜单图直出影视级分镜｜全流程提示词_2112052555575554049.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（89 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（69/89）

**有卡**：`SaveImage`、`LoadImage`、`MultiTextConcatenate`、`ttN concat`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`JDCN_StringToList`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`UNETLoader`、`KSampler`、`ProcessString`、`CFGNorm`、`VAELoader`、`CLIPLoader`、`CR Text`、`CustomAddLabel`、`RH_LLMAPI_NODE`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
