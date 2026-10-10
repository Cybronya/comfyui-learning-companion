---
key: 视频生成/文生视频/Wan2.2&lightx2v加速_1950385703961149441.json
name: Wan2.2&lightx2v加速_1950385703961149441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2&lightx2v加速_1950385703961149441.json
hash: da8b0d8daaea6c48
coverage: 0.947368
learned_at: 2026-10-10 23:07:05
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, VAEDecode, VHS_VideoCombine, UNETLoader, UNETLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, WanImageToVideo, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, MarkdownNote, EmptyHunyuanLatentVideo, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, CLIPTextEncode, MarkdownNote, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, UNETLoader, CFGZeroStarAndInit, EmptyHunyuanLatentVideo, WanVideoEnhanceAVideoKJ, KSamplerAdvanced, PathchSageAttentionKJ, PathchSageAttentionKJ, WanVideoEnhanceAVideoKJ, CFGZeroStarAndInit, VAEDecode, VHS_VideoCombine, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2&lightx2v加速_1950385703961149441.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2&lightx2v加速_1950385703961149441.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（57 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `CFGZeroStarAndInit`
- `EmptyHunyuanLatentVideo`
- `WanVideoEnhanceAVideoKJ`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `WanVideoEnhanceAVideoKJ`
- `CFGZeroStarAndInit`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `beta`

## 知识

覆盖率 **95%**（54/57）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`VAEDecode`、`VHS_VideoCombine`、`UNETLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`WanImageToVideo`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`CFGZeroStarAndInit`、`WanVideoEnhanceAVideoKJ`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
