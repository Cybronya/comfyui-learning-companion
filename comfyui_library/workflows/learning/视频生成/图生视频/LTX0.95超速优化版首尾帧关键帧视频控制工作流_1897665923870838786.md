---
key: 视频生成/图生视频/LTX0.95超速优化版首尾帧关键帧视频控制工作流_1897665923870838786.json
name: LTX0.95超速优化版首尾帧关键帧视频控制工作流_1897665923870838786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1897665923870838786.json
hash: 494bd79d77ca7d22
coverage: 0.918367
learned_at: 2026-10-15 22:29:19
nodes: [CLIPTextEncode, KSamplerSelect, CLIPTextEncode, Note, KSamplerSelect, LTXVScheduler, String Replace (mtb), String Replace (mtb), String Replace (mtb), String Replace (mtb), RandomNoise, ImageScale, ImageConcatMulti, VHS_VideoCombine, LTXVAddGuide, LTXVPreprocess, LTXVPreprocess, LTXVAddGuide, easy showAnything, STGGuider, SamplerCustomAdvanced, LTXVCropGuides, Note Plus (mtb), LayerUtility: PurgeVRAM, StringFunction|pysssss, LayerUtility: PurgeVRAM, VAEDecodeTiled, CheckpointLoaderSimple, PathchSageAttentionKJ, PatchModelPatcherOrder, JWImageResizeByLongerSide, LayerUtility: PurgeVRAM, RH_Captioner, LoadImage, LoadImage, CLIPLoader, VHS_VideoCombine, Note _O, EmptyLTXVLatentVideo, Note _O, Note _O, Note, easy showAnything, Note _O, ImageScale, LTXVConditioning, ApplyFBCacheOnModel, LTXVApplySTG, LTXVApplySTG]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-video-2b-v0.9.5.safetensors"}
---

# 视频生成/图生视频/LTX0.95超速优化版首尾帧关键帧视频控制工作流_1897665923870838786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1897665923870838786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（49 个）：
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `String Replace (mtb)`
- `String Replace (mtb)`
- `String Replace (mtb)`
- `String Replace (mtb)`
- `RandomNoise`
- `ImageScale`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `LTXVAddGuide`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVAddGuide`
- `easy showAnything`
- `STGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `Note Plus (mtb)`
- `LayerUtility: PurgeVRAM`
- `StringFunction|pysssss`
- `LayerUtility: PurgeVRAM`
- `VAEDecodeTiled` ★核心
- `CheckpointLoaderSimple` ★核心
- `PathchSageAttentionKJ`
- `PatchModelPatcherOrder`
- `JWImageResizeByLongerSide`
- `LayerUtility: PurgeVRAM`
- `RH_Captioner`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `VHS_VideoCombine`
- `Note _O`
- `EmptyLTXVLatentVideo`
- `Note _O`
- `Note _O`
- `Note`
- `easy showAnything`
- `Note _O`
- `ImageScale`
- `LTXVConditioning`
- `ApplyFBCacheOnModel`
- `LTXVApplySTG`
- `LTXVApplySTG`

## 关键参数

- `checkpoint` = `ltx-video-2b-v0.9.5.safetensors`

## 知识

覆盖率 **92%**（45/49）

**有卡**：`CLIPTextEncode`、`KSamplerSelect`、`LTXVScheduler`、`String Replace (mtb)`、`RandomNoise`、`ImageScale`、`ImageConcatMulti`、`VHS_VideoCombine`、`LTXVAddGuide`、`LTXVPreprocess`、`STGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`Note Plus (mtb)`、`LayerUtility: PurgeVRAM`、`StringFunction|pysssss`、`VAEDecodeTiled`、`CheckpointLoaderSimple`、`PathchSageAttentionKJ`、`PatchModelPatcherOrder`、`JWImageResizeByLongerSide`、`RH_Captioner`、`LoadImage`、`CLIPLoader`、`Note _O`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`ApplyFBCacheOnModel`、`LTXVApplySTG`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled、EmptyLTXVLatentVideo
