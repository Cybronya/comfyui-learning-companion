---
key: 视频生成/图生视频/Jason-Wan2.2 Remix V3.0 图生视频&首尾帧生视频_2056998498276569090.json
name: Jason-Wan2.2 Remix V3.0 图生视频&首尾帧生视频_2056998498276569090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Jason-Wan2.2 Remix V3.0 图生视频&首尾帧生视频_2056998498276569090.json
hash: 560005d53274ce61
coverage: 0.924528
learned_at: 2026-10-15 22:38:07
nodes: [CLIPLoader, VAELoader, UNETLoader, UNETLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, WanMoeKSampler, CLIPTextEncode, DuckHideNode, VHS_VideoCombine, CLIPTextEncode, FL_RIFE, VAEDecode, WanImageToVideo, CLIPVisionEncode, CLIPLoader, VAELoader, UNETLoader, UNETLoader, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPTextEncode, DuckHideNode, VHS_VideoCombine, SaveImage, CLIPTextEncode, VHS_VideoCombine, CLIPVisionLoader, VHS_VideoCombine, LoadImage, PreviewImage, PreviewImage, LoadImage, CLIPVisionLoader, CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionEncode, WanMoeKSampler, WanFirstLastFrameToVideo, VAEDecode, ImageScaleBy, FL_RIFE, SaveImage, Fast Groups Bypasser (rgthree), ImageScaleBy]
patterns: []
missing: []
parameters: {"cfg": 16, "denoise": "euler_ancestral", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "increment"}
---

# 视频生成/图生视频/Jason-Wan2.2 Remix V3.0 图生视频&首尾帧生视频_2056998498276569090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2056998498276569090.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `WanMoeKSampler` ★核心
- `CLIPTextEncode` ★核心
- `DuckHideNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `FL_RIFE`
- `VAEDecode` ★核心
- `WanImageToVideo`
- `CLIPVisionEncode`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `DuckHideNode`
- `VHS_VideoCombine`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionEncode`
- `WanMoeKSampler` ★核心
- `WanFirstLastFrameToVideo`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `FL_RIFE`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleBy`

## 关键参数

- `seed` = `0.9`
- `steps` = `increment`
- `cfg` = `16`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler_ancestral`

## 知识

覆盖率 **92%**（49/53）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanMoeKSampler`、`CLIPTextEncode`、`DuckHideNode`、`VHS_VideoCombine`、`FL_RIFE`、`VAEDecode`、`WanImageToVideo`、`CLIPVisionEncode`、`SaveImage`、`CLIPVisionLoader`、`WanFirstLastFrameToVideo`、`ImageScaleBy`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler、CLIPVisionEncode
