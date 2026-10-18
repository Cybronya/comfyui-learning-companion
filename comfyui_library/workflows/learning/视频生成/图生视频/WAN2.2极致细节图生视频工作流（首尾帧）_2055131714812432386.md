---
key: 视频生成/图生视频/WAN2.2极致细节图生视频工作流（首尾帧）_2055131714812432386.json
name: WAN2.2极致细节图生视频工作流（首尾帧）_2055131714812432386.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2极致细节图生视频工作流（首尾帧）_2055131714812432386.json
hash: d3d667d1a60ef0a5
coverage: 0.943396
learned_at: 2026-10-15 22:37:54
nodes: [Note, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchTorchSettings, UNETLoader, UNETLoader, CLIPLoader, VAELoader, PathchSageAttentionKJ, ModelPatchTorchSettings, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, WanMoeKSampler, VAEDecode, PlaySound|pysssss, VHS_VideoCombine, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPVisionLoader, PathchSageAttentionKJ, CLIPVisionEncode, CLIPVisionEncode, CLIPTextEncode, CLIPTextEncode, easy int, WanFirstLastFrameToVideo, WanMoeKSampler, PlaySound|pysssss, VAEDecode, VHS_VideoCombine, VHS_VideoCombine, FL_RIFE, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Fast Groups Bypasser (rgthree), FL_RIFE]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "fixed"}
---

# 视频生成/图生视频/WAN2.2极致细节图生视频工作流（首尾帧）_2055131714812432386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055131714812432386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `Note`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `WanMoeKSampler` ★核心
- `VAEDecode` ★核心
- `PlaySound|pysssss`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `PathchSageAttentionKJ`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `WanFirstLastFrameToVideo`
- `WanMoeKSampler` ★核心
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `FL_RIFE`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `FL_RIFE`

## 关键参数

- `seed` = `0.9`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **94%**（50/53）

**有卡**：`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`、`ModelPatchTorchSettings`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`WanImageToVideo`、`WanMoeKSampler`、`VAEDecode`、`PlaySound|pysssss`、`VHS_VideoCombine`、`CLIPVisionLoader`、`CLIPVisionEncode`、`easy int`、`WanFirstLastFrameToVideo`、`FL_RIFE`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
