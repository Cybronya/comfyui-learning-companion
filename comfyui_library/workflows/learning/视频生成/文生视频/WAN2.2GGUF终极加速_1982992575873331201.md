---
key: 视频生成/文生视频/WAN2.2GGUF终极加速_1982992575873331201.json
name: WAN2.2GGUF终极加速_1982992575873331201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2GGUF终极加速_1982992575873331201.json
hash: c71abf6dc40952c9
coverage: 0.884615
learned_at: 2026-10-11 02:45:02
nodes: [SimpleMath+, Note, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, VAEDecode, LoadImage, WanMoeKSampler, VHS_VideoCombine, FILM VFI, VHS_VideoCombine, wanBlockSwap, PathchSageAttentionKJ, PathchSageAttentionKJ, wanBlockSwap, WanImageToVideo, ModelPatchTorchSettings, ModelPatchTorchSettings, DF_Integer, CLIPTextEncode, UnetLoaderGGUF, UnetLoaderGGUF, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: [FILM VFI, SimpleMath+]
parameters: {"cfg": 4, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
discoveries: [次要节点 `FILM VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
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

覆盖率 **88%**（23/26）

**有卡**：`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAEDecode`、`LoadImage`、`WanMoeKSampler`、`VHS_VideoCombine`、`wanBlockSwap`、`PathchSageAttentionKJ`、`WanImageToVideo`、`ModelPatchTorchSettings`、`DF_Integer`、`UnetLoaderGGUF`、`CLIPLoader`、`VAELoader`

**缺卡**（2）：`FILM VFI`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、WanMoeKSampler、DF_Integer

## 学习发现

- 次要节点 `FILM VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
