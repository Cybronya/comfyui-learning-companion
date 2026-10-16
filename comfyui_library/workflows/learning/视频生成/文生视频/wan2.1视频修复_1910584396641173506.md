---
key: 视频生成/文生视频/wan2.1视频修复_1910584396641173506.json
name: wan2.1视频修复_1910584396641173506.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1910584396641173506.json
hash: acfe5139702cc2b0
coverage: 0.607143
learned_at: 2026-10-15 22:43:22
nodes: [LayerMask: PersonMaskUltra V2, CXH_DownloadAndLoadFlorence2Model, CLIPLoader, WanVideoTeaCacheKJ, CFGZeroStarAndInit, Anything Everywhere3, ShowText|pysssss, ShowText|pysssss, LayerUtility: PurgeVRAM V2, RH_Translator, Florence2Run, SetNode, GetNode, CLIPTextEncode, CLIPTextEncode, SetNode, LayerUtility: CropByMask, VHS_VideoCombine, VHS_VideoCombine, VAEDecodeTiled, LayerUtility: PurgeVRAM V2, GetNode, ImageUpscaleWithModel, VHS_VideoCombine, GetImageRangeFromBatch, LayerUtility: PurgeVRAM V2, RIFE VFI, WanVideoEnhanceAVideoKJ, VAELoader, GetNode, PreviewImage, ImageConcatMulti, KSampler, SkipLayerGuidanceWanVideo, GetNode, UpscaleModelLoader, ImageScaleBy, UNETLoader, SetNode, GetNode, GetNode, ImageBlur, ImpactSwitch, easy int, GetNode, SetNode, InstructPixToPixConditioning, Note, VHS_LoadVideo, SetNode, SetNode, Note, Note, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 472840585328931, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/wan2.1视频修复_1910584396641173506.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1910584396641173506.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `LayerMask: PersonMaskUltra V2`
- `CXH_DownloadAndLoadFlorence2Model`
- `CLIPLoader`
- `WanVideoTeaCacheKJ`
- `CFGZeroStarAndInit`
- `Anything Everywhere3`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `LayerUtility: PurgeVRAM V2`
- `RH_Translator`
- `Florence2Run`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `LayerUtility: CropByMask`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `ImageUpscaleWithModel`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `LayerUtility: PurgeVRAM V2`
- `RIFE VFI`
- `WanVideoEnhanceAVideoKJ`
- `VAELoader`
- `GetNode`
- `PreviewImage`
- `ImageConcatMulti`
- `KSampler` ★核心
- `SkipLayerGuidanceWanVideo`
- `GetNode`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageBlur`
- `ImpactSwitch`
- `easy int`
- `GetNode`
- `SetNode`
- `InstructPixToPixConditioning`
- `Note`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `472840585328931`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **61%**（34/56）

**有卡**：`LayerMask: PersonMaskUltra V2`、`CXH_DownloadAndLoadFlorence2Model`、`CLIPLoader`、`WanVideoTeaCacheKJ`、`CFGZeroStarAndInit`、`LayerUtility: PurgeVRAM V2`、`RH_Translator`、`Florence2Run`、`CLIPTextEncode`、`LayerUtility: CropByMask`、`VHS_VideoCombine`、`VAEDecodeTiled`、`ImageUpscaleWithModel`、`GetImageRangeFromBatch`、`RIFE VFI`、`WanVideoEnhanceAVideoKJ`、`VAELoader`、`ImageConcatMulti`、`KSampler`、`SkipLayerGuidanceWanVideo`、`UpscaleModelLoader`、`ImageScaleBy`、`UNETLoader`、`ImageBlur`、`easy int`、`InstructPixToPixConditioning`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、CFGZeroStarAndInit、SkipLayerGuidanceWanVideo

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
