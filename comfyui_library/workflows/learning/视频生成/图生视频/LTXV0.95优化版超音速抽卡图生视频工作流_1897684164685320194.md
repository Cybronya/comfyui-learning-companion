---
key: 视频生成/图生视频/LTXV0.95优化版超音速抽卡图生视频工作流_1897684164685320194.json
name: LTXV0.95优化版超音速抽卡图生视频工作流_1897684164685320194.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1897684164685320194.json
hash: 984dfc7883105467
coverage: 0.9375
learned_at: 2026-10-15 22:29:19
nodes: [CLIPTextEncode, String Replace (mtb), easy showAnything, String Replace (mtb), CLIPTextEncode, easy showAnything, String Replace (mtb), LTXVPreprocess, LTXVScheduler, SamplerCustomAdvanced, STGGuider, Note Plus (mtb), KSamplerSelect, ApplyFBCacheOnModel, StringFunction|pysssss, LayerUtility: PurgeVRAM, VAEDecodeTiled, LayerUtility: PurgeVRAM, RH_Captioner, PathchSageAttentionKJ, PatchModelPatcherOrder, CheckpointLoaderSimple, CLIPLoader, LoadImage, JWImageResizeByLongerSide, GetImageSizeAndCount, VHS_VideoCombine, String Replace (mtb), LTXVImgToVideo, LTXVApplySTG, RandomNoise, LayerUtility: PurgeVRAM]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-video-2b-v0.9.5.safetensors"}
---

# 视频生成/图生视频/LTXV0.95优化版超音速抽卡图生视频工作流_1897684164685320194.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1897684164685320194.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `CLIPTextEncode` ★核心
- `String Replace (mtb)`
- `easy showAnything`
- `String Replace (mtb)`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `String Replace (mtb)`
- `LTXVPreprocess`
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `STGGuider`
- `Note Plus (mtb)`
- `KSamplerSelect` ★核心
- `ApplyFBCacheOnModel`
- `StringFunction|pysssss`
- `LayerUtility: PurgeVRAM`
- `VAEDecodeTiled` ★核心
- `LayerUtility: PurgeVRAM`
- `RH_Captioner`
- `PathchSageAttentionKJ`
- `PatchModelPatcherOrder`
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `LoadImage`
- `JWImageResizeByLongerSide`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `String Replace (mtb)`
- `LTXVImgToVideo`
- `LTXVApplySTG`
- `RandomNoise`
- `LayerUtility: PurgeVRAM`

## 关键参数

- `checkpoint` = `ltx-video-2b-v0.9.5.safetensors`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`CLIPTextEncode`、`String Replace (mtb)`、`LTXVPreprocess`、`LTXVScheduler`、`SamplerCustomAdvanced`、`STGGuider`、`Note Plus (mtb)`、`KSamplerSelect`、`ApplyFBCacheOnModel`、`StringFunction|pysssss`、`LayerUtility: PurgeVRAM`、`VAEDecodeTiled`、`RH_Captioner`、`PathchSageAttentionKJ`、`PatchModelPatcherOrder`、`CheckpointLoaderSimple`、`CLIPLoader`、`LoadImage`、`JWImageResizeByLongerSide`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`LTXVImgToVideo`、`LTXVApplySTG`、`RandomNoise`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled、GetImageSizeAndCount
