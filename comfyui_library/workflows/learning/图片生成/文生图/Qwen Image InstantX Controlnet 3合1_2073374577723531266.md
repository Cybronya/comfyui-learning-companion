---
key: 图片生成/文生图/Qwen Image InstantX Controlnet 3合1_2073374577723531266.json
name: Qwen Image InstantX Controlnet 3合1_2073374577723531266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image InstantX Controlnet 3合1_2073374577723531266.json
hash: b5f150b5e68b17ec
coverage: 0.806452
learned_at: 2026-10-20 00:01:36
nodes: [UNETLoader, LoraLoaderModelOnly, ImpactSwitch, ControlNetLoader, SetUnionControlNetType, PreviewImage, PreviewImage, PreviewImage, AIO_Preprocessor, AIO_Preprocessor, Note, ControlNetApplySD3, KSampler, EmptySD3LatentImage, SaveLatent, VAEDecode, SeedVR2BlockSwap, SeedVR2GGUF, EmptyImage, PreviewImage, SaveImage, AIO_Preprocessor, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, VAELoader, ImageConcatMulti, LoadImage, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 0.75, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 397623419622816, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image InstantX Controlnet 3合1_2073374577723531266.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image InstantX Controlnet 3合1_2073374577723531266.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImpactSwitch`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `Note`
- `ControlNetApplySD3` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `SaveLatent`
- `VAEDecode` ★核心
- `SeedVR2BlockSwap`
- `SeedVR2GGUF`
- `EmptyImage`
- `PreviewImage`
- `SaveImage`
- `AIO_Preprocessor`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `VAELoader`
- `ImageConcatMulti`
- `LoadImage`
- `Int`

## 关键参数

- `controlnet_strength` = `0.75`
- `seed` = `397623419622816`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **81%**（25/31）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`ControlNetLoader`、`SetUnionControlNetType`、`AIO_Preprocessor`、`ControlNetApplySD3`、`KSampler`、`EmptySD3LatentImage`、`SaveLatent`、`VAEDecode`、`SeedVR2BlockSwap`、`SeedVR2GGUF`、`EmptyImage`、`SaveImage`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`VAELoader`、`ImageConcatMulti`、`LoadImage`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
