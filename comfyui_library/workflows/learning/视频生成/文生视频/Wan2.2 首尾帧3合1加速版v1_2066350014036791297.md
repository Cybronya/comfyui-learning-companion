---
key: 视频生成/文生视频/Wan2.2 首尾帧3合1加速版v1_2066350014036791297.json
name: Wan2.2 首尾帧3合1加速版v1_2066350014036791297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 首尾帧3合1加速版v1_2066350014036791297.json
hash: 36b16602a808f430
coverage: 0.737705
learned_at: 2026-10-11 20:21:31
nodes: [VAELoader, VHS_VideoCombine, WanImageToVideo, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, VHS_VideoCombine, Note, VHS_VideoCombine, CLIPLoader, CLIPVisionLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, Note, LoadImage, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPTextEncode, CLIPVisionEncode, CLIPVisionEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, PlaySound|pysssss, PreviewImage, WanMoeKSampler, UNETLoader, UNETLoader, UNETLoader, UNETLoader, Fast Groups Bypasser (rgthree), VAEDecode, FL_RIFE, LayerUtility: ImageScaleByAspectRatio V2, WanFirstLastFrameToVideo, FL_RIFE, LayerUtility: ImageScaleByAspectRatio V2, easy int, PreviewImage, PreviewImage, ModelPatchTorchSettings, WanMoeKSampler, VAEDecode, PlaySound|pysssss, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VHS_VideoCombine, Note, CLIPTextEncode]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PlaySound|pysssss, PlaySound|pysssss, easy int]
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2 首尾帧3合1加速版v1_2066350014036791297.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 首尾帧3合1加速版v1_2066350014036791297.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VHS_VideoCombine`
- `Note`
- `VHS_VideoCombine`
- `CLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `PlaySound|pysssss`
- `PreviewImage`
- `WanMoeKSampler` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `FL_RIFE`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanFirstLastFrameToVideo`
- `FL_RIFE`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `PreviewImage`
- `PreviewImage`
- `ModelPatchTorchSettings`
- `WanMoeKSampler` ★核心
- `VAEDecode` ★核心
- `PlaySound|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `Note`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **74%**（45/61）

**有卡**：`VAELoader`、`VHS_VideoCombine`、`WanImageToVideo`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPTextEncode`、`LoadImage`、`CLIPVisionEncode`、`WanMoeKSampler`、`UNETLoader`、`VAEDecode`、`FL_RIFE`、`WanFirstLastFrameToVideo`

**缺卡**（6）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`PlaySound|pysssss`、`PlaySound|pysssss`、`easy int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `PlaySound|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
