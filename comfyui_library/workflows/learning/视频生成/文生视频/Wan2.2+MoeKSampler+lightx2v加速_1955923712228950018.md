---
key: 视频生成/文生视频/Wan2.2+MoeKSampler+lightx2v加速_1955923712228950018.json
name: Wan2.2+MoeKSampler+lightx2v加速_1955923712228950018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2+MoeKSampler+lightx2v加速_1955923712228950018.json
hash: 6d7da1887ea63573
coverage: 0.806452
learned_at: 2026-10-10 23:07:06
nodes: [Note, Note, CLIPTextEncode, VAELoader, UNETLoader, Note, UNETLoader, CLIPTextEncode, CLIPLoader, VAELoader, Note, Note, UNETLoader, WanImageToVideo, Note, UNETLoader, VAEDecode, WanMoeKSampler, CLIPTextEncode, CLIPLoader, VAEDecode, CLIPTextEncode, EmptyHunyuanLatentVideo, ImageResizeKJv2, VHS_VideoCombine, CLIPTextEncode, CLIPLoader, VAELoader, Note, Note, WanImageToVideo, Note, UNETLoader, VAEDecode, CLIPTextEncode, ImageResizeKJv2, Note, Note, CLIPTextEncode, VAELoader, Note, UNETLoader, CLIPTextEncode, CLIPLoader, VAEDecode, EmptyHunyuanLatentVideo, WanMoeKSampler, WanMoeKSampler, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LoadImage, LoraLoaderModelOnly, WanMoeKSampler, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "uni_pc", "sampler_name": 4, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2+MoeKSampler+lightx2v加速_1955923712228950018.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2+MoeKSampler+lightx2v加速_1955923712228950018.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（62 个）：
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `Note`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `WanImageToVideo`
- `Note`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `WanMoeKSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `Note`
- `WanImageToVideo`
- `Note`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `WanMoeKSampler` ★核心
- `WanMoeKSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `WanMoeKSampler` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `4`
- `scheduler` = `1`
- `denoise` = `uni_pc`

## 知识

覆盖率 **81%**（50/62）

**有卡**：`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`WanImageToVideo`、`VAEDecode`、`WanMoeKSampler`、`EmptyHunyuanLatentVideo`、`ImageResizeKJv2`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
