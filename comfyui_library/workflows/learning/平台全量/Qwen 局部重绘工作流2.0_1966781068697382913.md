---
key: 平台全量/Qwen 局部重绘工作流2.0_1966781068697382913.json
name: Qwen 局部重绘工作流2.0_1966781068697382913
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen 局部重绘工作流2.0_1966781068697382913.json
hash: 6ab4b6ec6161ace1
coverage: 1
learned_at: 2026-11-14 00:50:55
nodes: [CLIPLoader, UNETLoader, ModelSamplingAuraFlow, VAEDecode, CFGNorm, KSampler, SaveImage, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Mask Fill Holes, CLIPTextEncode, ControlNetLoader, LoraLoaderModelOnly, VAELoader, ControlNetInpaintingAliMamaApply, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 1035392338201698, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen 局部重绘工作流2.0_1966781068697382913.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen 局部重绘工作流2.0_1966781068697382913.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `CFGNorm`
- `KSampler` ★核心
- `SaveImage`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Mask Fill Holes`
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ControlNetInpaintingAliMamaApply`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1035392338201698`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`CLIPLoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`VAEDecode`、`CFGNorm`、`KSampler`、`SaveImage`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`Mask Fill Holes`、`CLIPTextEncode`、`ControlNetLoader`、`LoraLoaderModelOnly`、`VAELoader`、`ControlNetInpaintingAliMamaApply`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
