---
key: 图片生成/图生图/FireRed-Image-Edit + OpenClaw：打造高考倒计时大屏，每天自动生成不重样！_2025468706289094658.json
name: FireRed-Image-Edit + OpenClaw：打造高考倒计时大屏，每天自动生成不重样！_2025468706289094658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit + OpenClaw：打造高考倒计时大屏，每天自动生成不重样！_2025468706289094658.json
hash: e66be639052301e1
coverage: 0.826087
learned_at: 2026-10-23 10:55:30
nodes: [Note, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, VAEDecode, SaveImage, UNETLoader, LoraLoaderModelOnly, Reroute, Reroute, CLIPLoader, VAELoader, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, KSampler, EmptySD3LatentImage, Seed (rgthree), CFGNorm, TextEncodeQwenImageEditPlus, Note, LoadImage, LoadImage, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 602596886192896, "steps": 12}
---

# 图片生成/图生图/FireRed-Image-Edit + OpenClaw：打造高考倒计时大屏，每天自动生成不重样！_2025468706289094658.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit + OpenClaw：打造高考倒计时大屏，每天自动生成不重样！_2025468706289094658.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `Note`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `Seed (rgthree)`
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `Note`
- `LoadImage`
- `LoadImage`
- `Label (rgthree)`
- `Label (rgthree)`

## 关键参数

- `seed` = `602596886192896`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`FluxKontextMultiReferenceLatentMethod`、`VAEDecode`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`KSampler`、`EmptySD3LatentImage`、`Seed (rgthree)`、`CFGNorm`、`LoadImage`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
