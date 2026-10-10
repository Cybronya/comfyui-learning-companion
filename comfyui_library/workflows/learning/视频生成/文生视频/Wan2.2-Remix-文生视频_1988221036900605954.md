---
key: 视频生成/文生视频/Wan2.2-Remix-文生视频_1988221036900605954.json
name: Wan2.2-Remix-文生视频_1988221036900605954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-Remix-文生视频_1988221036900605954.json
hash: ebe2911e08b8d93b
coverage: 0.928571
learned_at: 2026-10-11 02:57:38
nodes: [CLIPLoader, INTConstant, VAELoader, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, INTConstant, INTConstant, UNETLoader, UNETLoader, WanImageToVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, MuyeTextEditOutput, SimpleMath+, LayerUtility: TextJoin, Wan22PromptSelector]
patterns: []
missing: [LayerUtility: TextJoin, SimpleMath+]
parameters: {"cfg": 6, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
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

覆盖率 **93%**（26/28）

**有卡**：`CLIPLoader`、`INTConstant`、`VAELoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`WanImageToVideo`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`MuyeTextEditOutput`、`Wan22PromptSelector`

**缺卡**（2）：`LayerUtility: TextJoin`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Wan22PromptSelector

## 学习发现

- 次要节点 `LayerUtility: TextJoin` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
