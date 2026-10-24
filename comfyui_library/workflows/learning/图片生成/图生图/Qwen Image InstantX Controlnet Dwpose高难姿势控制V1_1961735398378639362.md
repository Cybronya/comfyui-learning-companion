---
key: 图片生成/图生图/Qwen Image InstantX Controlnet Dwpose高难姿势控制V1_1961735398378639362.json
name: Qwen Image InstantX Controlnet Dwpose高难姿势控制V1_1961735398378639362
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image InstantX Controlnet Dwpose高难姿势控制V1_1961735398378639362.json
hash: 0137421fa604c718
coverage: 0.823529
learned_at: 2026-10-23 11:13:21
nodes: [CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, CLIPTextEncode, PreviewImage, SetUnionControlNetType, EmptySD3LatentImage, CFGNorm, ControlNetLoader, PreviewImage, DWPreprocessor, ImageConcanate, SaveImage, ImageConcanate, PreviewImage, SaveLatent, SeedVR2BlockSwap, RH_Captioner, easy showAnything, ControlNetApplySD3, SeedVR2GGUF, SaveImage, SaveImage, VAEDecode, PreviewImage, KSampler, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage, CLIPTextEncode, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 1060091465162839, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image InstantX Controlnet Dwpose高难姿势控制V1_1961735398378639362.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image InstantX Controlnet Dwpose高难姿势控制V1_1961735398378639362.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `SetUnionControlNetType`
- `EmptySD3LatentImage`
- `CFGNorm`
- `ControlNetLoader`
- `PreviewImage`
- `DWPreprocessor`
- `ImageConcanate`
- `SaveImage`
- `ImageConcanate`
- `PreviewImage`
- `SaveLatent`
- `SeedVR2BlockSwap`
- `RH_Captioner`
- `easy showAnything`
- `ControlNetApplySD3` ★核心
- `SeedVR2GGUF`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `seed` = `1060091465162839`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`SetUnionControlNetType`、`EmptySD3LatentImage`、`CFGNorm`、`ControlNetLoader`、`DWPreprocessor`、`ImageConcanate`、`SaveImage`、`SaveLatent`、`SeedVR2BlockSwap`、`RH_Captioner`、`ControlNetApplySD3`、`SeedVR2GGUF`、`VAEDecode`、`KSampler`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
