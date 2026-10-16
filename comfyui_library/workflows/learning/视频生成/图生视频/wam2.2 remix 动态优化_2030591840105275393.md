---
key: 视频生成/图生视频/wam2.2 remix 动态优化_2030591840105275393.json
name: wam2.2 remix 动态优化_2030591840105275393.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2030591840105275393.json
hash: 61efd4b1c566a037
coverage: 1
learned_at: 2026-10-15 22:35:27
nodes: [CLIPTextEncode, KSamplerAdvanced, Seed (rgthree), KSamplerAdvanced, INTConstant, VAEDecode, WanFunInpaintToVideo, ImageLoader, INTConstant, LoraLoaderModelOnly, LoraLoaderModelOnly, INTConstant, ImageResizeKJv2, ImageResizeKJv2, LoraLoaderModelOnly, INTConstant, INTConstant, LoraLoaderModelOnly, VAELoader, ImageLoader, CLIPLoader, CLIPTextEncode, VHS_VideoCombine, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wam2.2 remix 动态优化_2030591840105275393.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030591840105275393.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `Seed (rgthree)`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `VAEDecode` ★核心
- `WanFunInpaintToVideo`
- `ImageLoader`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ImageLoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`CLIPTextEncode`、`KSamplerAdvanced`、`Seed (rgthree)`、`INTConstant`、`VAEDecode`、`WanFunInpaintToVideo`、`ImageLoader`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`VAELoader`、`CLIPLoader`、`VHS_VideoCombine`、`ModelSamplingSD3`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)
