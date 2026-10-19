---
name: unknown_workflow_video_sampler_vae_174
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.906
common_nodes: [CR Text, DF_Integer, ImageResizeKJ, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, RH_LLMAPI_NODE, ShowText|pysssss, SimpleMath+, StringToInt, Text Multiline, TextSwitchCase, VHS_LoadVideo, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader, easy textSwitch]
problems: []
missing: []
members: [视频生成/图生视频/1934580529734066178.json, 视频生成/图生视频/1934580534721093634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_174

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1934580529734066178.json、视频生成/图生视频/1934580534721093634.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `DF_Integer`
- `ImageResizeKJ`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `SimpleMath+`
- `StringToInt`
- `Text Multiline`
- `TextSwitchCase`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy textSwitch`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `DepthAnything_V2` —— 1/2 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
