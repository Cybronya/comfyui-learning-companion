---
name: unknown_workflow_video_upscale_sampler_31
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.918
common_nodes: [CR Text, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageScaleToMegapixels, ImpactInt, LoadWanVideoT5TextEncoder, Note Plus (mtb), RH_LLMAPI_NODE, SimpleMath+, UpscaleModelLoader, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.1 14B FusionX 图生视频高清极速简化版-StarAI_1936402446031949825.json, 视频生成/文生视频/🥪FusionX 文生视频 自动扩写润色 超清臻享版🥪_1934859086565711873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_31

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Wan2.1 14B FusionX 图生视频高清极速简化版-StarAI_1936402446031949825.json、视频生成/文生视频/🥪FusionX 文生视频 自动扩写润色 超清臻享版🥪_1934859086565711873.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageScaleToMegapixels`
- `ImpactInt`
- `LoadWanVideoT5TextEncoder`
- `Note Plus (mtb)`
- `RH_LLMAPI_NODE`
- `SimpleMath+`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `Switch any [Crystools]` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoMagCache` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `easy textSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
