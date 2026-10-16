---
key: 视频生成/图生视频/WAN2.2 图生视频 4步出图_2016945597965672449.json
name: WAN2.2 图生视频 4步出图_2016945597965672449.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2016945597965672449.json
hash: 31dba6742a2ed151
coverage: 1
learned_at: 2026-10-15 22:34:44
nodes: [ModelSamplingSD3, VAEDecode, CLIPTextEncode, VAELoader, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, CLIPLoader, LoadImage, CLIPTextEncode, VHS_VideoCombine, WanImageToVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2 图生视频 4步出图_2016945597965672449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2016945597965672449.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（16 个）：
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `WanImageToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`ModelSamplingSD3`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`VHS_VideoCombine`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
