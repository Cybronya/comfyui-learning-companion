---
key: 图片生成/文生图/FLUX.1基础工作流_2054393266530988034.json
name: FLUX.1基础工作流_2054393266530988034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.1基础工作流_2054393266530988034.json
hash: 0356f22822d791e5
coverage: 0.939394
learned_at: 2026-10-21 02:51:48
nodes: [SamplerCustomAdvanced, BasicGuider, BasicGuider, SamplerCustomAdvanced, BasicGuider, KSamplerSelect, easy cleanGpuUsed, CLIPTextEncode, easy cleanGpuUsed, RandomNoise, PreviewImage, KSamplerSelect, BasicScheduler, EmptyLatentImage, ControlNetApplySD3, RandomNoise, KSamplerSelect, RandomNoise, DualCLIPLoader, ControlNetApplyAdvanced, BasicScheduler, LoraLoader, ModelSamplingFlux, UNETLoader, DualCLIPLoader, BasicScheduler, ModelSamplingFlux, easy cleanGpuUsed, UNETLoader, SamplerCustomAdvanced, VAEEncodeForInpaint, VAEEncode, SetShakkerLabsUnionControlNetType, LoadImage, TTPlanet_TileSimple_Preprocessor, LoraLoader, CLIPTextEncodeFlux, LoraLoader, CLIPTextEncodeFlux, PreviewImage, SetShakkerLabsUnionControlNetType, OpenposePreprocessor, LoraLoader, CLIPTextEncodeFlux, LoadImage, Note, LoraLoader, ModelSamplingFlux, easy positive, easy positive, UNETLoader, DualCLIPLoader, VAELoader, VAELoader, VAELoader, easy positive, ControlNetLoader, ControlNetLoader, VAEDecode, SaveImage, VAEDecode, SaveImage, VAEDecode, SaveImage, Fast Groups Muter (rgthree), EmptyLatentImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "controlnet_strength": 0.6, "height": 1280, "lora_name": "CQ_character_styleF1.safetensors", "strength_clip": 0, "strength_model": 1, "width": 768}
---

# 图片生成/文生图/FLUX.1基础工作流_2054393266530988034.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.1基础工作流_2054393266530988034.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（66 个）：
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `RandomNoise`
- `PreviewImage`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `EmptyLatentImage` ★核心
- `ControlNetApplySD3` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `DualCLIPLoader`
- `ControlNetApplyAdvanced` ★核心
- `BasicScheduler`
- `LoraLoader` ★核心
- `ModelSamplingFlux`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `BasicScheduler`
- `ModelSamplingFlux`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEEncodeForInpaint` ★核心
- `VAEEncode` ★核心
- `SetShakkerLabsUnionControlNetType`
- `LoadImage`
- `TTPlanet_TileSimple_Preprocessor`
- `LoraLoader` ★核心
- `CLIPTextEncodeFlux` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncodeFlux` ★核心
- `PreviewImage`
- `SetShakkerLabsUnionControlNetType`
- `OpenposePreprocessor`
- `LoraLoader` ★核心
- `CLIPTextEncodeFlux` ★核心
- `LoadImage`
- `Note`
- `LoraLoader` ★核心
- `ModelSamplingFlux`
- `easy positive`
- `easy positive`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAELoader`
- `VAELoader`
- `easy positive`
- `ControlNetLoader`
- `ControlNetLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Fast Groups Muter (rgthree)`
- `EmptyLatentImage` ★核心

**识别到的模式**：lora

## 关键参数

- `width` = `768`
- `height` = `1280`
- `batch_size` = `1`
- `controlnet_strength` = `0.6`
- `lora_name` = `CQ_character_styleF1.safetensors`
- `strength_model` = `1`
- `strength_clip` = `0`

## 知识

覆盖率 **94%**（62/66）

**有卡**：`SamplerCustomAdvanced`、`BasicGuider`、`KSamplerSelect`、`easy cleanGpuUsed`、`CLIPTextEncode`、`RandomNoise`、`BasicScheduler`、`EmptyLatentImage`、`ControlNetApplySD3`、`DualCLIPLoader`、`ControlNetApplyAdvanced`、`LoraLoader`、`ModelSamplingFlux`、`UNETLoader`、`VAEEncodeForInpaint`、`VAEEncode`、`SetShakkerLabsUnionControlNetType`、`LoadImage`、`TTPlanet_TileSimple_Preprocessor`、`CLIPTextEncodeFlux`、`OpenposePreprocessor`、`easy positive`、`VAELoader`、`ControlNetLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
