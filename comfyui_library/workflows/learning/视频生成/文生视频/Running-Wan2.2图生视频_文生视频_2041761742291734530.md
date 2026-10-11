---
key: 视频生成/文生视频/Running-Wan2.2图生视频_文生视频_2041761742291734530.json
name: Running-Wan2.2图生视频_文生视频_2041761742291734530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Running-Wan2.2图生视频_文生视频_2041761742291734530.json
hash: 009da893b98ffa41
coverage: 0.791667
learned_at: 2026-10-11 19:49:42
nodes: [UNETLoader, UNETLoader, CLIPLoader, VAELoader, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, PlaySound|pysssss, VAEDecode, EmptyHunyuanLatentVideo, WanImageToVideo, Note, ModelPatchTorchSettings, PathchSageAttentionKJ, Note, ModelPatchTorchSettings, PathchSageAttentionKJ, WanMoeKSampler, VHS_VideoCombine]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, PlaySound|pysssss]
parameters: {"cfg": 3, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Running-Wan2.2图生视频_文生视频_2041761742291734530.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Running-Wan2.2图生视频_文生视频_2041761742291734530.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `WanImageToVideo`
- `Note`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Note`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `WanMoeKSampler` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `3`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`WanImageToVideo`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`WanMoeKSampler`、`VHS_VideoCombine`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`PlaySound|pysssss`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
