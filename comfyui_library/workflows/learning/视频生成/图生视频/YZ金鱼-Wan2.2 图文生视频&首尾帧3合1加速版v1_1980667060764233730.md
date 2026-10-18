---
key: 视频生成/图生视频/YZ金鱼-Wan2.2 图文生视频&首尾帧3合1加速版v1_1980667060764233730.json
name: YZ金鱼-Wan2.2 图文生视频&首尾帧3合1加速版v1_1980667060764233730.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/YZ金鱼-Wan2.2 图文生视频&首尾帧3合1加速版v1_1980667060764233730.json
hash: 3578fcf942500779
coverage: 0.836066
learned_at: 2026-10-15 22:32:32
nodes: [VAELoader, VHS_VideoCombine, VHS_VideoCombine, WanImageToVideo, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, VHS_VideoCombine, Note, VHS_VideoCombine, CLIPLoader, CLIPVisionLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, Note, LoadImage, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPTextEncode, CLIPVisionEncode, CLIPVisionEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, PlaySound|pysssss, PreviewImage, WanMoeKSampler, UNETLoader, UNETLoader, UNETLoader, UNETLoader, Fast Groups Bypasser (rgthree), VAEDecode, FL_RIFE, LayerUtility: ImageScaleByAspectRatio V2, WanFirstLastFrameToVideo, FL_RIFE, LayerUtility: ImageScaleByAspectRatio V2, easy int, PreviewImage, PreviewImage, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, ModelPatchTorchSettings, WanMoeKSampler, VAEDecode, Note, PlaySound|pysssss, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/YZ金鱼-Wan2.2 图文生视频&首尾帧3合1加速版v1_1980667060764233730.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980667060764233730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `VAELoader`
- `VHS_VideoCombine`
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
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `ModelPatchTorchSettings`
- `WanMoeKSampler` ★核心
- `VAEDecode` ★核心
- `Note`
- `PlaySound|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **84%**（51/61）

**有卡**：`VAELoader`、`VHS_VideoCombine`、`WanImageToVideo`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`CLIPLoader`、`CLIPVisionLoader`、`CLIPTextEncode`、`LoadImage`、`CLIPVisionEncode`、`PlaySound|pysssss`、`WanMoeKSampler`、`UNETLoader`、`VAEDecode`、`FL_RIFE`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanFirstLastFrameToVideo`、`easy int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
