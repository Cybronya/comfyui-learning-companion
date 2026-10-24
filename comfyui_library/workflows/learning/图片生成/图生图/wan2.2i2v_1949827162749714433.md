---
key: 图片生成/图生图/wan2.2i2v_1949827162749714433.json
name: wan2.2i2v_1949827162749714433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2i2v_1949827162749714433.json
hash: 84985259721e02df
coverage: 1
learned_at: 2026-10-23 11:46:00
nodes: [CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, UNETLoader, CLIPLoader, CLIPVisionLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPVisionEncode, VAEDecode, LoadImage, VHS_VideoCombine, KSamplerAdvanced, VAELoader, VAEDecode, UNETLoader, WanImageToVideo, JWInteger, TextBox, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/wan2.2i2v_1949827162749714433.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2i2v_1949827162749714433.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（21 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `WanImageToVideo`
- `JWInteger`
- `TextBox`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`CLIPTextEncode`、`KSamplerAdvanced`、`UNETLoader`、`CLIPLoader`、`CLIPVisionLoader`、`ModelSamplingSD3`、`CLIPVisionEncode`、`VAEDecode`、`LoadImage`、`VHS_VideoCombine`、`VAELoader`、`WanImageToVideo`、`JWInteger`、`TextBox`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
