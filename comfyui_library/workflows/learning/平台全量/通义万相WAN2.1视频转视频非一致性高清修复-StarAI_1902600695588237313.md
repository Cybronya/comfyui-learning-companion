---
key: 平台全量/通义万相WAN2.1视频转视频非一致性高清修复-StarAI_1902600695588237313.json
name: 通义万相WAN2.1视频转视频非一致性高清修复-StarAI_1902600695588237313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/通义万相WAN2.1视频转视频非一致性高清修复-StarAI_1902600695588237313.json
hash: 1fbd0712e40da10e
coverage: 0.64
learned_at: 2026-11-14 02:48:30
nodes: [LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, ImageFromBatch+, Int, UNETLoader, Int, SetNode, SetNode, SetNode, VAELoader, SetNode, Seed_, SetNode, VHS_LoadVideo, LayerUtility: PurgeVRAM, ImageUpscaleWithModel, RIFE VFI, GetNode, CLIPTextEncode, CLIPTextEncode, WanVideoTeaCacheKJ, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, VHS_VideoCombine, VHS_VideoCombine, VAEEncodeTiled, VAEDecodeTiled, LayerUtility: PurgeVRAM, KSampler, UpscaleModelLoader, VHS_VideoCombine, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SkipLayerGuidanceWanVideo, GetNode, WanVideoEnhanceAVideoKJ, CFGZeroStarAndInit, GetNode, GetNode, Note Plus (mtb), SetNode, SetNode, Florence2Run, DownloadAndLoadFlorence2Model, Switch any [Crystools], CR Text]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 0.25000000000000006, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 964481024274340, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/通义万相WAN2.1视频转视频非一致性高清修复-StarAI_1902600695588237313.json

> 来源文件 `comfyui_library/workflows/平台全量/通义万相WAN2.1视频转视频非一致性高清修复-StarAI_1902600695588237313.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（50 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `ImageFromBatch+`
- `Int`
- `UNETLoader` ★核心
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `Seed_`
- `SetNode`
- `VHS_LoadVideo`
- `LayerUtility: PurgeVRAM`
- `ImageUpscaleWithModel`
- `RIFE VFI`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoTeaCacheKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEEncodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SkipLayerGuidanceWanVideo`
- `GetNode`
- `WanVideoEnhanceAVideoKJ`
- `CFGZeroStarAndInit`
- `GetNode`
- `GetNode`
- `Note Plus (mtb)`
- `SetNode`
- `SetNode`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `Switch any [Crystools]`
- `CR Text`

## 关键参数

- `seed` = `964481024274340`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **64%**（32/50）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`ImageFromBatch+`、`Int`、`UNETLoader`、`VAELoader`、`Seed_`、`VHS_LoadVideo`、`LayerUtility: PurgeVRAM`、`ImageUpscaleWithModel`、`RIFE VFI`、`CLIPTextEncode`、`WanVideoTeaCacheKJ`、`ImageConcatMulti`、`VHS_VideoCombine`、`VAEEncodeTiled`、`VAEDecodeTiled`、`KSampler`、`UpscaleModelLoader`、`SkipLayerGuidanceWanVideo`、`WanVideoEnhanceAVideoKJ`、`CFGZeroStarAndInit`、`Note Plus (mtb)`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`Switch any [Crystools]`、`CR Text`

**用到的条目**：KSampler、VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、CFGZeroStarAndInit、Seed_、SkipLayerGuidanceWanVideo

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
