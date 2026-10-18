---
key: 视频生成/图生视频/Wan2.2首尾帧视频生成_1952049916556292097.json
name: Wan2.2首尾帧视频生成_1952049916556292097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2首尾帧视频生成_1952049916556292097.json
hash: 479093498ff98413
coverage: 1
learned_at: 2026-10-15 22:31:00
nodes: [VAELoader, CLIPVisionEncode, CLIPVisionEncode, VAEDecode, CLIPTextEncode, WanFirstLastFrameToVideo, CLIPLoader, PathchSageAttentionKJ, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, LoadImage, LoadImage, CR Text, UNETLoader, UNETLoader, CLIPVisionLoader, SaveVideo, VHS_VideoCombine, CreateVideo, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2首尾帧视频生成_1952049916556292097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952049916556292097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（25 个）：
- `VAELoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `WanFirstLastFrameToVideo`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `CR Text`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `SaveVideo`
- `VHS_VideoCombine`
- `CreateVideo`
- `LoadImage`
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`VAELoader`、`CLIPVisionEncode`、`VAEDecode`、`CLIPTextEncode`、`WanFirstLastFrameToVideo`、`CLIPLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`LoadImage`、`CR Text`、`UNETLoader`、`CLIPVisionLoader`、`SaveVideo`、`VHS_VideoCombine`、`CreateVideo`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
