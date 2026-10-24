---
key: 图片生成/图生图/WH-AI-Studio人物风格迁移ipadapter+controlnet_2022481235498508289.json
name: WH-AI-Studio人物风格迁移ipadapter+controlnet_2022481235498508289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WH-AI-Studio人物风格迁移ipadapter+controlnet_2022481235498508289.json
hash: 15ea5bc7ab1cca59
coverage: 0.896552
learned_at: 2026-10-23 11:27:38
nodes: [AlphaChanelAsMask, LoraLoader, IPAdapterAdvanced, CheckpointLoaderSimple, IPAdapterUnifiedLoader, easy imageRemBg, VAEEncodeForInpaint, MiniCPM_VQA_Polished, InvertMask, easy promptConcat, AnyLinePreprocessor, ControlNetLoader, CLIPTextEncode, ControlNetApplyAdvanced, KSampler, PreviewImage, ShowText|pysssss, CLIPTextEncode, MiniCPM_VQA_Polished, RH_Prompter, ShowText|pysssss, SaveImage, SaveImage, VAEDecode, easy imageConcat, LoadImage, LoadImage, easy imageConcat, LoadImage]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2, "checkpoint": "dreamshaperXL_sfwV2TurboDPMSDE.safetensors", "controlnet_strength": 1, "denoise": 0.8, "lora_name": "MJ52.safetensors", "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 291849792120848, "steps": 8, "strength_clip": 1, "strength_model": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/WH-AI-Studio人物风格迁移ipadapter+controlnet_2022481235498508289.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WH-AI-Studio人物风格迁移ipadapter+controlnet_2022481235498508289.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `AlphaChanelAsMask`
- `LoraLoader` ★核心
- `IPAdapterAdvanced`
- `CheckpointLoaderSimple` ★核心
- `IPAdapterUnifiedLoader`
- `easy imageRemBg`
- `VAEEncodeForInpaint` ★核心
- `MiniCPM_VQA_Polished`
- `InvertMask`
- `easy promptConcat`
- `AnyLinePreprocessor`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `MiniCPM_VQA_Polished`
- `RH_Prompter`
- `ShowText|pysssss`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `easy imageConcat`
- `LoadImage`
- `LoadImage`
- `easy imageConcat`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `MJ52.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `dreamshaperXL_sfwV2TurboDPMSDE.safetensors`
- `controlnet_strength` = `1`
- `seed` = `291849792120848`
- `steps` = `8`
- `cfg` = `2`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `0.8`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`AlphaChanelAsMask`、`LoraLoader`、`IPAdapterAdvanced`、`CheckpointLoaderSimple`、`IPAdapterUnifiedLoader`、`easy imageRemBg`、`VAEEncodeForInpaint`、`MiniCPM_VQA_Polished`、`InvertMask`、`easy promptConcat`、`AnyLinePreprocessor`、`ControlNetLoader`、`CLIPTextEncode`、`ControlNetApplyAdvanced`、`KSampler`、`RH_Prompter`、`SaveImage`、`VAEDecode`、`easy imageConcat`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、VAEEncodeForInpaint

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
