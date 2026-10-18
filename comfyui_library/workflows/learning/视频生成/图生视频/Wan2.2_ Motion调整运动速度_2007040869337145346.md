---
key: 视频生成/图生视频/Wan2.2_ Motion调整运动速度_2007040869337145346.json
name: Wan2.2_ Motion调整运动速度_2007040869337145346.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2_ Motion调整运动速度_2007040869337145346.json
hash: d94f8f8d0d49d310
coverage: 0.941176
learned_at: 2026-10-15 22:34:03
nodes: [CLIPTextEncode, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, CLIPTextEncode, LoadImage, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, WanMotionScale, VHS_VideoCombine, WanImageToVideo]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2_ Motion调整运动速度_2007040869337145346.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2007040869337145346.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（17 个）：
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `WanMotionScale`
- `VHS_VideoCombine`
- `WanImageToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`CLIPTextEncode`、`KSamplerAdvanced`、`VAEDecode`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`WanMotionScale`、`VHS_VideoCombine`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
