---
key: 平台全量/智能精准风格迁移 Style Transfer to Main Subject_1840347073982976001.json
name: 智能精准风格迁移 Style Transfer to Main Subject_1840347073982976001
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/智能精准风格迁移 Style Transfer to Main Subject_1840347073982976001.json
hash: 0b449ca7f5c7f4b5
coverage: 0.851852
learned_at: 2026-11-14 02:13:42
nodes: [IPAdapterUnifiedLoader, CheckpointLoaderSimple, LoraLoader, EmptyLatentImage, VAEEncodeForInpaint, ControlNetApplyAdvanced, IPAdapterAdvanced, PreviewImage, AnyLinePreprocessor, InvertMask, easy imageRemBg, AlphaChanelAsMask, ControlNetLoader, SaveImage, VAEDecode, PreviewImage, CLIPTextEncode, CLIPTextEncode, MiniCPM_VQA_Polished, MiniCPM_VQA_Polished, easy promptConcat, ShowText|pysssss, RH_Prompter, ShowText|pysssss, LoadImage, LoadImage, KSampler]
patterns: [text_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 2, "checkpoint": "dreamshaperXL_sfwV2TurboDPMSDE.safetensors", "controlnet_strength": 1, "denoise": 0.8, "height": 1352, "lora_name": "MJ52.safetensors", "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 644714670836608, "steps": 8, "strength_clip": 1, "strength_model": 1, "width": 856}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/智能精准风格迁移 Style Transfer to Main Subject_1840347073982976001.json

> 来源文件 `comfyui_library/workflows/平台全量/智能精准风格迁移 Style Transfer to Main Subject_1840347073982976001.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `IPAdapterUnifiedLoader`
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `EmptyLatentImage` ★核心
- `VAEEncodeForInpaint` ★核心
- `ControlNetApplyAdvanced` ★核心
- `IPAdapterAdvanced`
- `PreviewImage`
- `AnyLinePreprocessor`
- `InvertMask`
- `easy imageRemBg`
- `AlphaChanelAsMask`
- `ControlNetLoader`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MiniCPM_VQA_Polished`
- `MiniCPM_VQA_Polished`
- `easy promptConcat`
- `ShowText|pysssss`
- `RH_Prompter`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `checkpoint` = `dreamshaperXL_sfwV2TurboDPMSDE.safetensors`
- `lora_name` = `MJ52.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `width` = `856`
- `height` = `1352`
- `batch_size` = `1`
- `controlnet_strength` = `1`
- `seed` = `644714670836608`
- `steps` = `8`
- `cfg` = `2`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `0.8`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`IPAdapterUnifiedLoader`、`CheckpointLoaderSimple`、`LoraLoader`、`EmptyLatentImage`、`VAEEncodeForInpaint`、`ControlNetApplyAdvanced`、`IPAdapterAdvanced`、`AnyLinePreprocessor`、`InvertMask`、`easy imageRemBg`、`AlphaChanelAsMask`、`ControlNetLoader`、`SaveImage`、`VAEDecode`、`CLIPTextEncode`、`MiniCPM_VQA_Polished`、`easy promptConcat`、`RH_Prompter`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
