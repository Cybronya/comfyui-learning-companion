---
name: unknown_workflow_video_sampler_clip_240
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.791
common_nodes: [AIO_Preprocessor, GetImageSizeAndCount, GetNode, ImageBlend, ImageConcatMulti, ImageResizeKJ, JjkShowText, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, SetNode, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoControlEmbeds, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy clearCacheAll]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1FUNControlnetOTT20250416A横版_1912373863278411778.json, 视频生成/图生视频/图生视频-动作迁移_1990585465176809474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_240

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.1FUNControlnetOTT20250416A横版_1912373863278411778.json、视频生成/图生视频/图生视频-动作迁移_1990585465176809474.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBlend`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `JjkShowText`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `Text Concatenate`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoControlEmbeds`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 1/2 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LTXVPromptEnhancer` —— 1/2 个有
- `LTXVPromptEnhancerLoader` —— 1/2 个有
- `LayerMask: LoadFlorence2Model` —— 1/2 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/2 个有
- `MeshGraphormer-DepthMapPreprocessor` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
