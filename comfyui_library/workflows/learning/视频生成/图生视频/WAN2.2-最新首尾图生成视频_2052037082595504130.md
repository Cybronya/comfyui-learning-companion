---
key: 视频生成/图生视频/WAN2.2-最新首尾图生成视频_2052037082595504130.json
name: WAN2.2-最新首尾图生成视频_2052037082595504130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2-最新首尾图生成视频_2052037082595504130.json
hash: dcf1fcdd8dfcf52a
coverage: 0.837838
learned_at: 2026-10-15 22:37:26
nodes: [RIFE VFI, easy cleanGpuUsed, RTXVideoSuperResolution, VAEDecode, WanMoeKSampler, INTConstant, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, wanBlockSwap, wanBlockSwap, LayerUtility: PurgeVRAM, SimpleMath+, GetNode, ImageSmartSharpen+, Note, Note, UNETLoader, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, SetNode, VHS_VideoCombine, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, CLIPTextEncode, WanVideoNAG, CLIPTextEncode, CLIPLoader, LoraLoaderModelOnly, Note, LoraLoaderModelOnly, ImageResizeKJ, WanFirstLastFrameToVideo, INTConstant]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/图生视频/WAN2.2-最新首尾图生成视频_2052037082595504130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052037082595504130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（37 个）：
- `RIFE VFI`
- `easy cleanGpuUsed`
- `RTXVideoSuperResolution`
- `VAEDecode` ★核心
- `WanMoeKSampler` ★核心
- `INTConstant`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `wanBlockSwap`
- `wanBlockSwap`
- `LayerUtility: PurgeVRAM`
- `SimpleMath+`
- `GetNode`
- `ImageSmartSharpen+`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `SetNode`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJ`
- `WanFirstLastFrameToVideo`
- `INTConstant`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **84%**（31/37）

**有卡**：`RIFE VFI`、`easy cleanGpuUsed`、`RTXVideoSuperResolution`、`VAEDecode`、`WanMoeKSampler`、`INTConstant`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`wanBlockSwap`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`ImageSmartSharpen+`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`VHS_VideoCombine`、`LoadImage`、`CLIPTextEncode`、`WanVideoNAG`、`CLIPLoader`、`LoraLoaderModelOnly`、`ImageResizeKJ`、`WanFirstLastFrameToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
