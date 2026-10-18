---
key: 视频生成/图生视频/wan2.2图生视频_1997975012088905729.json
name: wan2.2图生视频_1997975012088905729.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频_1997975012088905729.json
hash: 37233e44de2f3e76
coverage: 1
learned_at: 2026-10-15 22:33:31
nodes: [CLIPLoader, VAELoader, UNETLoader, UNETLoader, ModelSamplingSD3, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, VAEDecode, SaveVideo, KSamplerAdvanced, KSamplerAdvanced, LoadImage, CLIPTextEncode, CreateVideo, WanImageToVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2图生视频_1997975012088905729.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997975012088905729.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `WanImageToVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveVideo`、`KSamplerAdvanced`、`LoadImage`、`CreateVideo`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
