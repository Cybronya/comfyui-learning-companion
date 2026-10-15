---
key: 视频生成/文生视频/Wan2.2-Remix-文生视频_1988221036900605954.json
name: Wan2.2-Remix-文生视频_1988221036900605954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-Remix-文生视频_1988221036900605954.json
hash: ebe2911e08b8d93b
coverage: 1
learned_at: 2026-10-15 22:47:12
nodes: [CLIPLoader, INTConstant, VAELoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, INTConstant, INTConstant, UNETLoader, UNETLoader, WanImageToVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, MuyeTextEditOutput, SimpleMath+, LayerUtility: TextJoin, Wan22PromptSelector]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2-Remix-文生视频_1988221036900605954.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-Remix-文生视频_1988221036900605954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（28 个）：
- `CLIPLoader`
- `INTConstant`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `WanImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `MuyeTextEditOutput`
- `SimpleMath+`
- `LayerUtility: TextJoin`
- `Wan22PromptSelector`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`CLIPLoader`、`INTConstant`、`VAELoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`WanImageToVideo`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`MuyeTextEditOutput`、`SimpleMath+`、`LayerUtility: TextJoin`、`Wan22PromptSelector`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Wan22PromptSelector
