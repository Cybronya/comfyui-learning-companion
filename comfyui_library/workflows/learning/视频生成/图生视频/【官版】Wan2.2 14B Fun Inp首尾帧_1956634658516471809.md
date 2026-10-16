---
key: 视频生成/图生视频/【官版】Wan2.2 14B Fun Inp首尾帧_1956634658516471809.json
name: 【官版】Wan2.2 14B Fun Inp首尾帧_1956634658516471809.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956634658516471809.json
hash: 0a2e61b01e34b187
coverage: 0.891892
learned_at: 2026-10-15 22:31:14
nodes: [CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, CLIPLoader, VAELoader, UNETLoader, UNETLoader, LoadImage, LoadImage, WanFunInpaintToVideo, VAEDecode, CreateVideo, SaveVideo, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, MarkdownNote, LoadImage, LoadImage, CLIPTextEncode, MarkdownNote, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, WanFunInpaintToVideo, Note, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, Note, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/【官版】Wan2.2 14B Fun Inp首尾帧_1956634658516471809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956634658516471809.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（37 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `WanFunInpaintToVideo`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `WanFunInpaintToVideo`
- `Note`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `Note`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`WanFunInpaintToVideo`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`LoraLoaderModelOnly`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
