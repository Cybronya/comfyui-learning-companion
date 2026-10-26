---
name: unknown_workflow_video_sampler_vae_176
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.942
common_nodes: [CR Text, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, JWInteger, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, PrimitiveString, RHHiddenNodes, SeedVR2BlockSwap, SeedVR2GGUF, ShowText|pysssss, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/复刻视频之文生视频反推万相wan2.2+MiniCPM4.5V+专属提示词_1962056229839421442.json, 视频生成/图生视频/复刻视频之图生视频反推万相wan2.2+MiniCPM4.5V+Stand-in+动作迁移+专属扩词_1962159024101900289.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_176

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/复刻视频之文生视频反推万相wan2.2+MiniCPM4.5V+专属提示词_1962056229839421442.json、视频生成/图生视频/复刻视频之图生视频反推万相wan2.2+MiniCPM4.5V+Stand-in+动作迁移+专属扩词_1962159024101900289.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `JWInteger`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveString`
- `RHHiddenNodes`
- `SeedVR2BlockSwap`
- `SeedVR2GGUF`
- `ShowText|pysssss`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyFaceProcessor` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `FaceProcessorLoader` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `WanVideoAddStandInLatent` —— 1/2 个有
- `WanVideoEasyCache` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `WanVideoVACEEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
