---
key: 图片生成/文生图/wan2.2文生图和视频美女lora工作流-美女保持完美一致性_1961428825634750466.json
name: wan2.2文生图和视频美女lora工作流-美女保持完美一致性_1961428825634750466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生图和视频美女lora工作流-美女保持完美一致性_1961428825634750466.json
hash: 7482a64ff6f8b700
coverage: 0.605263
learned_at: 2026-10-10 20:59:27
nodes: [SetNode, GetNode, GetNode, GetNode, CFGZeroStar, UNETLoader, VAELoader, SetNode, LoraLoaderModelOnly, VAEDecode, GetNode, SetNode, LoraLoaderModelOnly, UNETLoader, SetNode, WanVideoNAG, SetNode, CLIPLoader, ModelSamplingSD3, GetNode, ModelSamplingSD3, PathchSageAttentionKJ, GetNode, VHS_VideoCombine, EmptyHunyuanLatentVideo, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, PreviewImage, String, SetNode, CLIPTextEncode, JoinStringMulti, LoraLoaderModelOnly, LoraLoaderModelOnly, JWStringMultiline, MarkdownNote, Note]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 2.5, "scheduler": "ddim", "seed": "enable", "steps": "randomize"}
---

# 图片生成/文生图/wan2.2文生图和视频美女lora工作流-美女保持完美一致性_1961428825634750466.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2文生图和视频美女lora工作流-美女保持完美一致性_1961428825634750466.json`

## 结构

**节点**（38 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGZeroStar`
- `UNETLoader`
- `VAELoader`
- `SetNode`
- `LoraLoaderModelOnly`
- `VAEDecode`
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `SetNode`
- `WanVideoNAG`
- `SetNode`
- `CLIPLoader`
- `ModelSamplingSD3`
- `GetNode`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `GetNode`
- `VHS_VideoCombine`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `KSamplerAdvanced`
- `PreviewImage`
- `String`
- `SetNode`
- `CLIPTextEncode`
- `JoinStringMulti`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `JWStringMultiline`
- `MarkdownNote`
- `Note`

## 关键参数

- `cfg` = `8`
- `denoise` = `simple`
- `sampler_name` = `2.5`
- `scheduler` = `ddim`
- `seed` = `enable`
- `steps` = `randomize`

## 知识

覆盖率 **61%**（23/38）

**有卡**：`SetNode`、`GetNode`、`CFGZeroStar`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VAEDecode`、`WanVideoNAG`、`CLIPLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`
