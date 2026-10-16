---
key: 视频生成/图生视频/Remix_i2v_v2.1图生视频工作流_2067237434458468353.json
name: Remix_i2v_v2.1图生视频工作流_2067237434458468353.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067237434458468353.json
hash: 7ce10bbaef9a6c93
coverage: 1
learned_at: 2026-10-15 22:39:58
nodes: [KSamplerAdvanced, CLIPTextEncode, CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, WanImageToVideo, VAELoader, VAEDecode, VHS_VideoCombine, LoraLoaderModelOnly, UNETLoader, UNETLoader, CLIPTextEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Remix_i2v_v2.1图生视频工作流_2067237434458468353.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067237434458468353.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `VAELoader`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`KSamplerAdvanced`、`CLIPTextEncode`、`CLIPLoader`、`ModelSamplingSD3`、`WanImageToVideo`、`VAELoader`、`VAEDecode`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
