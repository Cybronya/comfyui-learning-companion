---
key: 视频生成/图生视频/Wan2.2 分镜版本 VBVR lora逻辑推理增强PLUS版_2034133687608025089.json
name: Wan2.2 分镜版本 VBVR lora逻辑推理增强PLUS版_2034133687608025089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2034133687608025089.json
hash: dd524e524f374d65
coverage: 0.95
learned_at: 2026-10-15 22:35:43
nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, UNETLoader, UNETLoader, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, SaveVideo, VAELoader, Note, ModelSamplingSD3, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, WanFirstLastFrameToVideo, LoadImage, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 分镜版本 VBVR lora逻辑推理增强PLUS版_2034133687608025089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034133687608025089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SaveVideo`
- `VAELoader`
- `Note`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanFirstLastFrameToVideo`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`CreateVideo`、`UNETLoader`、`VAEDecode`、`KSamplerAdvanced`、`SaveVideo`、`VAELoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`WanFirstLastFrameToVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
