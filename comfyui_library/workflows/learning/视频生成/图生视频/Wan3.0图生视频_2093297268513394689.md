---
key: 视频生成/图生视频/Wan3.0图生视频_2093297268513394689.json
name: Wan3.0图生视频_2093297268513394689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan3.0图生视频_2093297268513394689.json
hash: 372591d78bf5fa53
coverage: 0.956522
learned_at: 2026-10-16 23:42:31
nodes: [Note, UNETLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, CLIPTextEncode, WanFirstLastFrameToVideo, VAEDecode, SaveVideo, WanFirstLastFrameToVideo, KSamplerAdvanced, VAEDecode, CreateVideo, SaveVideo, CreateVideo, LoadImage, LoadImage, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan3.0图生视频_2093297268513394689.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan3.0图生视频_2093297268513394689.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `SaveVideo`
- `WanFirstLastFrameToVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `CreateVideo`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`UNETLoader`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`VAEDecode`、`SaveVideo`、`KSamplerAdvanced`、`CreateVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、SaveVideo
