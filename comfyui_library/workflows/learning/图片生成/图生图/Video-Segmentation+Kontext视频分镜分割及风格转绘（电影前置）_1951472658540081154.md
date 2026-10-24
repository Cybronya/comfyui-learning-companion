---
key: 图片生成/图生图/Video-Segmentation+Kontext视频分镜分割及风格转绘（电影前置）_1951472658540081154.json
name: Video-Segmentation+Kontext视频分镜分割及风格转绘（电影前置）_1951472658540081154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Video-Segmentation+Kontext视频分镜分割及风格转绘（电影前置）_1951472658540081154.json
hash: 7ae8425ec1a81632
coverage: 0.866667
learned_at: 2026-10-23 11:27:19
nodes: [DownloadAndLoadTransNetModel, BatchCount+, MathExpression|pysssss, UNETLoader, DualCLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, VAEEncode, VAEDecode, PreviewImage, LoraLoader, Int, TransNetV2_Run, LoadVideo, ShowText|pysssss, SelectVideo, easy forLoopStart, VHS_LoadVideoPath, SaveImage, easy forLoopEnd, easy batchAnything, PreviewImage, PreviewImage, JWImageResizeByLongerSide, ImageFromBatch, FluxGuidance, ReferenceLatent, TeaCache, KSampler]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "ghibliStyle_kontext_byJaneB.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 874206368777206, "steps": 20, "strength_clip": 1, "strength_model": 1}
---

# 图片生成/图生图/Video-Segmentation+Kontext视频分镜分割及风格转绘（电影前置）_1951472658540081154.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Video-Segmentation+Kontext视频分镜分割及风格转绘（电影前置）_1951472658540081154.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `DownloadAndLoadTransNetModel`
- `BatchCount+`
- `MathExpression|pysssss`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `LoraLoader` ★核心
- `Int`
- `TransNetV2_Run`
- `LoadVideo`
- `ShowText|pysssss`
- `SelectVideo`
- `easy forLoopStart`
- `VHS_LoadVideoPath`
- `SaveImage`
- `easy forLoopEnd`
- `easy batchAnything`
- `PreviewImage`
- `PreviewImage`
- `JWImageResizeByLongerSide`
- `ImageFromBatch`
- `FluxGuidance`
- `ReferenceLatent`
- `TeaCache`
- `KSampler` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `ghibliStyle_kontext_byJaneB.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `seed` = `874206368777206`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（26/30）

**有卡**：`DownloadAndLoadTransNetModel`、`BatchCount+`、`MathExpression|pysssss`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`VAEDecode`、`LoraLoader`、`Int`、`TransNetV2_Run`、`LoadVideo`、`SelectVideo`、`easy forLoopStart`、`VHS_LoadVideoPath`、`SaveImage`、`easy forLoopEnd`、`easy batchAnything`、`JWImageResizeByLongerSide`、`ImageFromBatch`、`FluxGuidance`、`ReferenceLatent`、`TeaCache`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、FluxGuidance、ReferenceLatent、VAEEncode
