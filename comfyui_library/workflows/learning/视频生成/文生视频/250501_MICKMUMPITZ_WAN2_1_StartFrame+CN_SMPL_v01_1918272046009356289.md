---
key: 视频生成/文生视频/250501_MICKMUMPITZ_WAN2_1_StartFrame+CN_SMPL_v01_1918272046009356289.json
name: 250501_MICKMUMPITZ_WAN2_1_StartFrame+CN_SMPL_v01_1918272046009356289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/250501_MICKMUMPITZ_WAN2_1_StartFrame+CN_SMPL_v01_1918272046009356289.json
hash: 895216fc2718ed08
coverage: 0.458716
learned_at: 2026-10-10 22:58:18
nodes: [Reroute, VHS_VideoCombine, Reroute, Reroute, Reroute, Reroute, Reroute, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, CLIPTextEncode, MarkdownNote, EmptyImage, VHS_VideoCombine, ImageBlend, ImageResizeKJ, GetNode, PreviewImage, DWPreprocessor, GetImageSizeAndCount, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, GetNode, Reroute, DepthAnythingV2Preprocessor, ImageResizeKJ, ImageResizeKJ, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, Reroute, SetNode, MaskToImage, ImageBlend, SetNode, Fast Groups Bypasser (rgthree), VHS_VideoCombine, ImageBlend, ImageResizeKJ, VRAM_Debug, SetNode, ImageBlend, VRAM_Debug, RMBG, GetNode, VHS_VideoCombine, WanFunControlToVideo, CLIPVisionEncode, ImageResizeKJ, GetNode, GetNode, VHS_VideoCombine, ImageListToImageBatch, SegsToCombinedMask, SetNode, MediaPipe-FaceMeshPreprocessor, ImpactImageBatchToImageList, MediaPipeFaceMeshToSEGS, GetNode, ImageConcatMulti, Note, CR Text Input Switch, Note, CR Text, Note, DisplayText_Zho, GetNode, Note, SkipLayerGuidanceDiT, ModelSamplingSD3, UNetTemporalAttentionMultiply, GetNode, CFGZeroStar, GetNode, SetNode, DownloadAndLoadDepthAnythingV2Model, SetNode, CLIPVisionLoader, SetNode, VAELoader, SetNode, CLIPLoader, UNETLoader, SetNode, LoraLoaderModelOnly, Note, GetNode, GetNode, RH_Captioner, ImageResizeKJ, KSampler, easy clearCacheAll, Primitive integer [Crystools], Primitive integer [Crystools], Note, VAEDecodeTiled, VHS_VideoCombine, VHS_LoadVideo, LoadImage, GetNode, VHS_VideoCombine]
patterns: []
missing: [CR Text, CR Text Input Switch, MediaPipe-FaceMeshPreprocessor, Primitive integer [Crystools], Primitive integer [Crystools], easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll]
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 382302099220888, "steps": 30}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Input Switch` 知识库中没有该节点类型的任何知识, 次要节点 `MediaPipe-FaceMeshPreprocessor` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/250501_MICKMUMPITZ_WAN2_1_StartFrame+CN_SMPL_v01_1918272046009356289.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/250501_MICKMUMPITZ_WAN2_1_StartFrame+CN_SMPL_v01_1918272046009356289.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（109 个）：
- `Reroute`
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `EmptyImage`
- `VHS_VideoCombine`
- `ImageBlend`
- `ImageResizeKJ`
- `GetNode`
- `PreviewImage`
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `Reroute`
- `DepthAnythingV2Preprocessor`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `Reroute`
- `SetNode`
- `MaskToImage`
- `ImageBlend`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `ImageBlend`
- `ImageResizeKJ`
- `VRAM_Debug`
- `SetNode`
- `ImageBlend`
- `VRAM_Debug`
- `RMBG`
- `GetNode`
- `VHS_VideoCombine`
- `WanFunControlToVideo`
- `CLIPVisionEncode`
- `ImageResizeKJ`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageListToImageBatch`
- `SegsToCombinedMask`
- `SetNode`
- `MediaPipe-FaceMeshPreprocessor`
- `ImpactImageBatchToImageList`
- `MediaPipeFaceMeshToSEGS`
- `GetNode`
- `ImageConcatMulti`
- `Note`
- `CR Text Input Switch`
- `Note`
- `CR Text`
- `Note`
- `DisplayText_Zho`
- `GetNode`
- `Note`
- `SkipLayerGuidanceDiT`
- `ModelSamplingSD3`
- `UNetTemporalAttentionMultiply`
- `GetNode`
- `CFGZeroStar`
- `GetNode`
- `SetNode`
- `DownloadAndLoadDepthAnythingV2Model`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `GetNode`
- `GetNode`
- `RH_Captioner`
- `ImageResizeKJ`
- `KSampler` ★核心
- `easy clearCacheAll`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Note`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `GetNode`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `382302099220888`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **46%**（50/109）

**有卡**：`VHS_VideoCombine`、`CLIPTextEncode`、`EmptyImage`、`ImageBlend`、`ImageResizeKJ`、`DWPreprocessor`、`GetImageSizeAndCount`、`DepthAnythingV2Preprocessor`、`MaskToImage`、`VRAM_Debug`、`RMBG`、`WanFunControlToVideo`、`CLIPVisionEncode`、`ImageListToImageBatch`、`SegsToCombinedMask`、`ImpactImageBatchToImageList`、`MediaPipeFaceMeshToSEGS`、`ImageConcatMulti`、`DisplayText_Zho`、`SkipLayerGuidanceDiT`、`ModelSamplingSD3`、`UNetTemporalAttentionMultiply`、`CFGZeroStar`、`DownloadAndLoadDepthAnythingV2Model`、`CLIPVisionLoader`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`RH_Captioner`、`KSampler`、`VAEDecodeTiled`、`VHS_LoadVideo`、`LoadImage`

**缺卡**（9）：`CR Text`、`CR Text Input Switch`、`MediaPipe-FaceMeshPreprocessor`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、DepthAnythingV2Preprocessor

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Input Switch` 知识库中没有该节点类型的任何知识
- 次要节点 `MediaPipe-FaceMeshPreprocessor` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
