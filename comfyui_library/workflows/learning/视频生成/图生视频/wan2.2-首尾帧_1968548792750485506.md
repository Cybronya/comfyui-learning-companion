---
key: 视频生成/图生视频/wan2.2-首尾帧_1968548792750485506.json
name: wan2.2-首尾帧_1968548792750485506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1968548792750485506.json
hash: b63c903d1b93a207
coverage: 1
learned_at: 2026-10-15 22:31:45
nodes: [VAELoader, CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, LayerUtility: ImageScaleByAspectRatio V2, WanFirstLastFrameToVideo, VAEDecode, Int, LoraLoaderModelOnly, LoraLoaderModelOnly, Mute / Bypass Repeater (rgthree), MathExpression|pysssss, ImageResizeKJv2, LoadImage, MathExpression|pysssss, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, Int, Fast Bypasser (rgthree), UNETLoader, UNETLoader, LoadImage, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2-首尾帧_1968548792750485506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968548792750485506.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `Int`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Mute / Bypass Repeater (rgthree)`
- `MathExpression|pysssss`
- `ImageResizeKJv2`
- `LoadImage`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `Fast Bypasser (rgthree)`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanFirstLastFrameToVideo`、`VAEDecode`、`Int`、`LoraLoaderModelOnly`、`Mute / Bypass Repeater (rgthree)`、`MathExpression|pysssss`、`ImageResizeKJv2`、`LoadImage`、`CLIPTextEncode`、`Fast Bypasser (rgthree)`、`UNETLoader`、`KSamplerAdvanced`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
