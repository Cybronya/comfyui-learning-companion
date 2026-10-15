---
key: 视频生成/文生视频/Wan2.2最新图生视频-加速版_2071097964008927234.json
name: Wan2.2最新图生视频-加速版_2071097964008927234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2最新图生视频-加速版_2071097964008927234.json
hash: a3f52f43e81d3100
coverage: 0.857143
learned_at: 2026-10-15 22:47:16
nodes: [INTConstant, WanMoeKSampler, VAEDecode, WanImageToVideo, LayerUtility: PurgeVRAM, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+, Note, Note, ImageSmartSharpen+, INTConstant, Note, ModelPatchTorchSettings, wanBlockSwap, ModelPatchTorchSettings, WanVideoNAG, CLIPTextEncode, UNETLoader, MarkdownNote, wanBlockSwap, easy cleanGpuUsed, RIFE VFI, UpscaleModelLoader, ImageUpscaleWithModel, Fast Groups Bypasser (rgthree), CLIPLoader, UNETLoader, VAELoader, LoadImage, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "euler", "sampler_name": 1, "scheduler": 1, "seed": 0.9, "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2最新图生视频-加速版_2071097964008927234.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2最新图生视频-加速版_2071097964008927234.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `INTConstant`
- `WanMoeKSampler` ★核心
- `VAEDecode` ★核心
- `WanImageToVideo`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SimpleMath+`
- `Note`
- `Note`
- `ImageSmartSharpen+`
- `INTConstant`
- `Note`
- `ModelPatchTorchSettings`
- `wanBlockSwap`
- `ModelPatchTorchSettings`
- `WanVideoNAG`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`
- `wanBlockSwap`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `Fast Groups Bypasser (rgthree)`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`

## 关键参数

- `seed` = `0.9`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`INTConstant`、`WanMoeKSampler`、`VAEDecode`、`WanImageToVideo`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`ImageSmartSharpen+`、`ModelPatchTorchSettings`、`wanBlockSwap`、`WanVideoNAG`、`CLIPTextEncode`、`UNETLoader`、`easy cleanGpuUsed`、`RIFE VFI`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`CLIPLoader`、`VAELoader`、`LoadImage`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanMoeKSampler
