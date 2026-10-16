---
key: 视频生成/图生视频/LTX video 8vram Best Settings_1869653016793227265.json
name: LTX video 8vram Best Settings_1869653016793227265.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1869653016793227265.json
hash: 78088ac83bc56ab8
coverage: 0.894737
learned_at: 2026-10-15 22:29:14
nodes: [KSampler, VHS_VideoCombine, Florence2Run, Florence2ModelLoader, LTXVConditioning, UpscaleModelLoader, ImageUpscaleWithModel, VHS_VideoCombine, VAEDecodeTiled, Note, LTXVModelConfigurator, Display Any (rgthree), LTXVImgToVideo, Fast Groups Bypasser (rgthree), CLIPLoader, LoadImage, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 3.5, "checkpoint": "ltx-video-2b-v0.9.1.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1, "steps": 20}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX video 8vram Best Settings_1869653016793227265.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1869653016793227265.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（19 个）：
- `KSampler` ★核心
- `VHS_VideoCombine`
- `Florence2Run`
- `Florence2ModelLoader`
- `LTXVConditioning`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `Note`
- `LTXVModelConfigurator`
- `Display Any (rgthree)`
- `LTXVImgToVideo`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `1`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `ltx-video-2b-v0.9.1.safetensors`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`KSampler`、`VHS_VideoCombine`、`Florence2Run`、`Florence2ModelLoader`、`LTXVConditioning`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`VAEDecodeTiled`、`LTXVModelConfigurator`、`Display Any (rgthree)`、`LTXVImgToVideo`、`CLIPLoader`、`LoadImage`、`CLIPTextEncode`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、VAEDecodeTiled、ImageUpscaleWithModel、UpscaleModelLoader

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
