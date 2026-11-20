---
name: unknown_workflow_video_sampler_vae_211
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.936
common_nodes: [AIO_Preprocessor, ColorMatch, DWPreprocessor, EmptyImage, GetImageSizeAndCount, ImageBlend, ImageConcatMulti, ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, RH_Captioner, ShowText|pysssss, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/FusionX VACE 动作迁移 姿态深度控制 图生视频高清极速版-StarAI_1938335512916852737.json, 视频生成/图生视频/人物动作迁移_图生视频_wan2.2_1969653436927143937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_211

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/FusionX VACE 动作迁移 姿态深度控制 图生视频高清极速版-StarAI_1938335512916852737.json、视频生成/图生视频/人物动作迁移_图生视频_wan2.2_1969653436927143937.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `ColorMatch`
- `DWPreprocessor`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageBlend`
- `ImageConcatMulti`
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RH_Captioner`
- `ShowText|pysssss`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `ImageScaleToMegapixels` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `Text` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoMagCache` —— 1/2 个有
- `WanVideoTeaCache` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
