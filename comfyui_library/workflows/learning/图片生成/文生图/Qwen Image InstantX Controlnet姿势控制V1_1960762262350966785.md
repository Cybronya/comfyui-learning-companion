---
key: Qwen Image InstantX Controlnet姿势控制V1_1960762262350966785.json
name: Qwen Image InstantX Controlnet姿势控制V1_1960762262350966785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image InstantX Controlnet姿势控制V1_1960762262350966785.json
hash: eeacf50e80df7eef
coverage: 0.888889
learned_at: 2026-10-10 20:58:55
nodes: [CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, VAEDecode, ImageConcanate, CLIPTextEncode, PreviewImage, SetUnionControlNetType, PreviewImage, OpenposePreprocessor, SeedVR2GGUF, EmptySD3LatentImage, CFGNorm, SaveImage, LoraLoaderModelOnly, KSampler, CLIPTextEncode, PreviewImage, ControlNetLoader, SeedVR2BlockSwap, ControlNetApplySD3, LoadImage, SaveLatent, SaveImage, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 397623419622816, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen Image InstantX Controlnet姿势控制V1_1960762262350966785.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image InstantX Controlnet姿势控制V1_1960762262350966785.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `SetUnionControlNetType`
- `PreviewImage`
- `OpenposePreprocessor`
- `SeedVR2GGUF`
- `EmptySD3LatentImage`
- `CFGNorm`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ControlNetLoader`
- `SeedVR2BlockSwap`
- `ControlNetApplySD3` ★核心
- `LoadImage`
- `SaveLatent`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `397623419622816`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`
- `controlnet_strength` = `1.0000000000000002`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`VAEDecode`、`ImageConcanate`、`CLIPTextEncode`、`SetUnionControlNetType`、`OpenposePreprocessor`、`SeedVR2GGUF`、`EmptySD3LatentImage`、`CFGNorm`、`SaveImage`、`KSampler`、`ControlNetLoader`、`SeedVR2BlockSwap`、`ControlNetApplySD3`、`LoadImage`、`SaveLatent`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
