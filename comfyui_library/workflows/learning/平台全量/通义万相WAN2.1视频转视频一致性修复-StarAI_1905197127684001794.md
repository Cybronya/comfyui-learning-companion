---
key: 平台全量/通义万相WAN2.1视频转视频一致性修复-StarAI_1905197127684001794.json
name: 通义万相WAN2.1视频转视频一致性修复-StarAI_1905197127684001794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/通义万相WAN2.1视频转视频一致性修复-StarAI_1905197127684001794.json
hash: cf8d628162498fc4
coverage: 0.627451
learned_at: 2026-11-14 02:48:28
nodes: [LayerUtility: ImageScaleByAspectRatio V2, Florence2Run, DownloadAndLoadFlorence2Model, ShowText|pysssss, CLIPLoader, ImageFromBatch+, Int, SetNode, SetNode, SetNode, VAELoader, SetNode, SetNode, Int, UNETLoader, Seed_, LayerUtility: PurgeVRAM, ImageUpscaleWithModel, RIFE VFI, UpscaleModelLoader, VHS_VideoCombine, Fast Groups Bypasser (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, VAEDecodeTiled, KSampler, GetNode, Fast Groups Bypasser (rgthree), GetNode, VHS_VideoCombine, InstructPixToPixConditioning, WanVideoTeaCacheKJ, LoraLoaderModelOnly, CFGZeroStarAndInit, ImageBlur, CLIPTextEncode, LayerUtility: PurgeVRAM, CLIPTextEncode, SetNode, GetNode, SkipLayerGuidanceWanVideo, WanVideoEnhanceAVideoKJ, VHS_VideoCombine, Note Plus (mtb), VHS_LoadVideo, SetNode, GetNode]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "gradient_estimation", "scheduler": "normal", "seed": 927434060160158, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/通义万相WAN2.1视频转视频一致性修复-StarAI_1905197127684001794.json

> 来源文件 `comfyui_library/workflows/平台全量/通义万相WAN2.1视频转视频一致性修复-StarAI_1905197127684001794.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（51 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `ShowText|pysssss`
- `CLIPLoader`
- `ImageFromBatch+`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `Int`
- `UNETLoader` ★核心
- `Seed_`
- `LayerUtility: PurgeVRAM`
- `ImageUpscaleWithModel`
- `RIFE VFI`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `VHS_VideoCombine`
- `InstructPixToPixConditioning`
- `WanVideoTeaCacheKJ`
- `LoraLoaderModelOnly` ★核心
- `CFGZeroStarAndInit`
- `ImageBlur`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `SkipLayerGuidanceWanVideo`
- `WanVideoEnhanceAVideoKJ`
- `VHS_VideoCombine`
- `Note Plus (mtb)`
- `VHS_LoadVideo`
- `SetNode`
- `GetNode`

## 关键参数

- `seed` = `927434060160158`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `gradient_estimation`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **63%**（32/51）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`CLIPLoader`、`ImageFromBatch+`、`Int`、`VAELoader`、`UNETLoader`、`Seed_`、`LayerUtility: PurgeVRAM`、`ImageUpscaleWithModel`、`RIFE VFI`、`UpscaleModelLoader`、`VHS_VideoCombine`、`ImageConcatMulti`、`VAEDecodeTiled`、`KSampler`、`InstructPixToPixConditioning`、`WanVideoTeaCacheKJ`、`LoraLoaderModelOnly`、`CFGZeroStarAndInit`、`ImageBlur`、`CLIPTextEncode`、`SkipLayerGuidanceWanVideo`、`WanVideoEnhanceAVideoKJ`、`Note Plus (mtb)`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、CFGZeroStarAndInit、Seed_

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
