---
key: 平台全量/通义万相WAN2.1视频转视频一致性修复-简化版_1924405005007114242.json
name: 通义万相WAN2.1视频转视频一致性修复-简化版_1924405005007114242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/通义万相WAN2.1视频转视频一致性修复-简化版_1924405005007114242.json
hash: ea65522aadbe4f64
coverage: 0.62
learned_at: 2026-11-14 02:48:28
nodes: [LayerUtility: ImageScaleByAspectRatio V2, Florence2Run, DownloadAndLoadFlorence2Model, ShowText|pysssss, CLIPLoader, ImageFromBatch+, Int, SetNode, SetNode, SetNode, VAELoader, SetNode, SetNode, UNETLoader, LayerUtility: PurgeVRAM, ImageUpscaleWithModel, RIFE VFI, UpscaleModelLoader, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, VAEDecodeTiled, KSampler, GetNode, InstructPixToPixConditioning, LoraLoaderModelOnly, CFGZeroStarAndInit, ImageBlur, CLIPTextEncode, LayerUtility: PurgeVRAM, SetNode, GetNode, SkipLayerGuidanceWanVideo, VHS_VideoCombine, SetNode, GetNode, Fast Groups Bypasser (rgthree), Seed_, Fast Groups Bypasser (rgthree), WanVideoEnhanceAVideoKJ, VHS_VideoCombine, WanVideoTeaCacheKJ, CLIPTextEncode, GetNode, VHS_LoadVideo, Int]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "gradient_estimation", "scheduler": "normal", "seed": 927434060160158, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/通义万相WAN2.1视频转视频一致性修复-简化版_1924405005007114242.json

> 来源文件 `comfyui_library/workflows/平台全量/通义万相WAN2.1视频转视频一致性修复-简化版_1924405005007114242.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（50 个）：
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
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `ImageUpscaleWithModel`
- `RIFE VFI`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `GetNode`
- `InstructPixToPixConditioning`
- `LoraLoaderModelOnly` ★核心
- `CFGZeroStarAndInit`
- `ImageBlur`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `SkipLayerGuidanceWanVideo`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Seed_`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoEnhanceAVideoKJ`
- `VHS_VideoCombine`
- `WanVideoTeaCacheKJ`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VHS_LoadVideo`
- `Int`

## 关键参数

- `seed` = `927434060160158`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `gradient_estimation`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **62%**（31/50）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`CLIPLoader`、`ImageFromBatch+`、`Int`、`VAELoader`、`UNETLoader`、`LayerUtility: PurgeVRAM`、`ImageUpscaleWithModel`、`RIFE VFI`、`UpscaleModelLoader`、`VHS_VideoCombine`、`ImageConcatMulti`、`VAEDecodeTiled`、`KSampler`、`InstructPixToPixConditioning`、`LoraLoaderModelOnly`、`CFGZeroStarAndInit`、`ImageBlur`、`CLIPTextEncode`、`SkipLayerGuidanceWanVideo`、`Seed_`、`WanVideoEnhanceAVideoKJ`、`WanVideoTeaCacheKJ`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、CFGZeroStarAndInit、Seed_

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
