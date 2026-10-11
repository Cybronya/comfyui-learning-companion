---
key: 视频生成/文生视频/Remix_i2v_v2.1工作流_2050521770255495170.json
name: Remix_i2v_v2.1工作流_2050521770255495170
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Remix_i2v_v2.1工作流_2050521770255495170.json
hash: 74c13688c09ee114
coverage: 0.944444
learned_at: 2026-10-11 19:49:42
nodes: [CLIPLoader, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, VAEDecode, VHS_VideoCombine, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, WanImageToVideo]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Remix_i2v_v2.1工作流_2050521770255495170.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Remix_i2v_v2.1工作流_2050521770255495170.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（18 个）：
- `CLIPLoader`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`CLIPLoader`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`WanImageToVideo`

**缺卡**（1）：`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
