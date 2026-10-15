---
key: 视频生成/文生视频/WAN2.2GGUF终极加速_1982992575873331201.json
name: WAN2.2GGUF终极加速_1982992575873331201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2GGUF终极加速_1982992575873331201.json
hash: c71abf6dc40952c9
coverage: 0.961538
learned_at: 2026-10-15 22:47:04
nodes: [SimpleMath+, Note, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, VAEDecode, LoadImage, WanMoeKSampler, VHS_VideoCombine, FILM VFI, VHS_VideoCombine, wanBlockSwap, PathchSageAttentionKJ, PathchSageAttentionKJ, wanBlockSwap, WanImageToVideo, ModelPatchTorchSettings, ModelPatchTorchSettings, DF_Integer, CLIPTextEncode, UnetLoaderGGUF, UnetLoaderGGUF, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/文生视频/WAN2.2GGUF终极加速_1982992575873331201.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2GGUF终极加速_1982992575873331201.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（26 个）：
- `SimpleMath+`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `WanMoeKSampler` ★核心
- `VHS_VideoCombine`
- `FILM VFI`
- `VHS_VideoCombine`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `WanImageToVideo`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `DF_Integer`
- `CLIPTextEncode` ★核心
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`SimpleMath+`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAEDecode`、`LoadImage`、`WanMoeKSampler`、`VHS_VideoCombine`、`FILM VFI`、`wanBlockSwap`、`PathchSageAttentionKJ`、`WanImageToVideo`、`ModelPatchTorchSettings`、`DF_Integer`、`UnetLoaderGGUF`、`CLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、WanMoeKSampler、DF_Integer
