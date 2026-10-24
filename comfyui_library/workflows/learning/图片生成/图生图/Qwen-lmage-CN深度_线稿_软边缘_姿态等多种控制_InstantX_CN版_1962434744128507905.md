---
key: 图片生成/图生图/Qwen-lmage-CN深度_线稿_软边缘_姿态等多种控制_InstantX_CN版_1962434744128507905.json
name: Qwen-lmage-CN深度_线稿_软边缘_姿态等多种控制_InstantX_CN版_1962434744128507905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-lmage-CN深度_线稿_软边缘_姿态等多种控制_InstantX_CN版_1962434744128507905.json
hash: 428e7c52f1d947a8
coverage: 0.625
learned_at: 2026-10-23 11:18:52
nodes: [ControlNetApplyAdvanced, PreviewImage, ControlNetApplyAdvanced, Anything Everywhere, PreviewImage, DWPreprocessor, Anything Everywhere, LoraLoaderModelOnly, AIO_Preprocessor, Image Comparer (rgthree), CLIPTextEncode, MarkdownNote, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, EmptySD3LatentImage, ModelSamplingAuraFlow, ControlNetApplyAdvanced, AIO_Preprocessor, CLIPTextEncode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), UNETLoader, CLIPLoader, VAELoader, MarkdownNote, LoadImage, ControlNetLoader, VAEDecode, KSampler, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 2.5, "controlnet_strength": 0.7, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 911699767305664, "steps": 20}
---

# 图片生成/图生图/Qwen-lmage-CN深度_线稿_软边缘_姿态等多种控制_InstantX_CN版_1962434744128507905.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-lmage-CN深度_线稿_软边缘_姿态等多种控制_InstantX_CN版_1962434744128507905.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ControlNetApplyAdvanced` ★核心
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `Anything Everywhere`
- `PreviewImage`
- `DWPreprocessor`
- `Anything Everywhere`
- `LoraLoaderModelOnly` ★核心
- `AIO_Preprocessor`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `ControlNetApplyAdvanced` ★核心
- `AIO_Preprocessor`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `LoadImage`
- `ControlNetLoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`

## 关键参数

- `controlnet_strength` = `0.7`
- `seed` = `911699767305664`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（20/32）

**有卡**：`ControlNetApplyAdvanced`、`DWPreprocessor`、`LoraLoaderModelOnly`、`AIO_Preprocessor`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`ControlNetLoader`、`VAEDecode`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
