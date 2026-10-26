---
key: 图片生成/反推提示词/video_wan2_2_14B_qwenvl-video-prompt-video_1981195099193376769.json
name: video_wan2_2_14B_qwenvl-video-prompt-video_1981195099193376769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/video_wan2_2_14B_qwenvl-video-prompt-video_1981195099193376769.json
hash: 489d78727c0c6a36
coverage: 0.611111
learned_at: 2026-10-26 01:47:05
nodes: [SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, EmptyHunyuanLatentVideo, KSamplerAdvanced, VAEDecode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStar, PathchSageAttentionKJ, WanVideoNAG, CLIPTextEncode, VHS_LoadVideo, VHS_VideoCombine, PreviewAny, AILab_QwenVL]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 图片生成/反推提示词/video_wan2_2_14B_qwenvl-video-prompt-video_1981195099193376769.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/video_wan2_2_14B_qwenvl-video-prompt-video_1981195099193376769.json`

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
- `VHS_LoadVideo`
- `VHS_VideoCombine`
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

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGZeroStar`、`PathchSageAttentionKJ`、`WanVideoNAG`、`VHS_LoadVideo`、`VHS_VideoCombine`、`AILab_QwenVL`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、CFGZeroStar
