---
key: 视频生成/文生视频/video_wan2_2_14B_qwenvl-prompt-generate_1981270580760576001.json
name: video_wan2_2_14B_qwenvl-prompt-generate_1981270580760576001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/video_wan2_2_14B_qwenvl-prompt-generate_1981270580760576001.json
hash: a4fd5ce8f91ac0e7
coverage: 0.6
learned_at: 2026-10-11 02:45:03
nodes: [SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, EmptyHunyuanLatentVideo, KSamplerAdvanced, VAEDecode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CFGZeroStar, PathchSageAttentionKJ, WanVideoNAG, CLIPTextEncode, PreviewAny, VHS_VideoCombine, AILab_QwenVL]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/video_wan2_2_14B_qwenvl-prompt-generate_1981270580760576001.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/video_wan2_2_14B_qwenvl-prompt-generate_1981270580760576001.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（35 个）：
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
- `PreviewAny`
- `VHS_VideoCombine`
- `AILab_QwenVL`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **60%**（21/35）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGZeroStar`、`PathchSageAttentionKJ`、`WanVideoNAG`、`VHS_VideoCombine`、`AILab_QwenVL`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、CFGZeroStar
