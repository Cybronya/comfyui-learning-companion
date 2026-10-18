---
key: 视频生成/图生视频/Wan2.2 首尾帧 VBVR lora逻辑推理增强_2028500989350776833.json
name: Wan2.2 首尾帧 VBVR lora逻辑推理增强_2028500989350776833.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 首尾帧 VBVR lora逻辑推理增强_2028500989350776833.json
hash: 0826550820169a60
coverage: 0.95
learned_at: 2026-10-15 22:35:19
nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, UNETLoader, UNETLoader, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, SaveVideo, VAELoader, Note, ModelSamplingSD3, LoraLoaderModelOnly, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, LoadImage, CLIPTextEncode, WanFirstLastFrameToVideo]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 首尾帧 VBVR lora逻辑推理增强_2028500989350776833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2028500989350776833.json`

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
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`CreateVideo`、`UNETLoader`、`VAEDecode`、`KSamplerAdvanced`、`SaveVideo`、`VAELoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`LoadImage`、`WanFirstLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
