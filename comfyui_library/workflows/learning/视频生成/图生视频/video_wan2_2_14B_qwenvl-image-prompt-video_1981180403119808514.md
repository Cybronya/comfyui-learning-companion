---
key: 视频生成/图生视频/video_wan2_2_14B_qwenvl-image-prompt-video_1981180403119808514.json
name: video_wan2_2_14B_qwenvl-image-prompt-video_1981180403119808514.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1981180403119808514.json
hash: dd05a0322f855f2a
coverage: 0.611111
learned_at: 2026-10-15 22:32:36
nodes: [SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, VHS_VideoCombine, CLIPTextEncode, KSamplerAdvanced, EmptyHunyuanLatentVideo, KSamplerAdvanced, VAEDecode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStar, PathchSageAttentionKJ, WanVideoNAG, CLIPTextEncode, LoadImage, PreviewAny, AILab_QwenVL]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/video_wan2_2_14B_qwenvl-image-prompt-video_1981180403119808514.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981180403119808514.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（36 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGZeroStar`
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `PreviewAny`
- `AILab_QwenVL`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **61%**（22/36）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VHS_VideoCombine`、`CLIPTextEncode`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGZeroStar`、`PathchSageAttentionKJ`、`WanVideoNAG`、`LoadImage`、`AILab_QwenVL`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
