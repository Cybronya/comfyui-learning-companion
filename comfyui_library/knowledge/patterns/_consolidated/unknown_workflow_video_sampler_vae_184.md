---
name: unknown_workflow_video_sampler_vae_184
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5655
common_nodes: [GetNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextBox, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1934287864869908481.json, 视频生成/图生视频/1934982902193004545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_184

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1934287864869908481.json、视频生成/图生视频/1934982902193004545.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：57%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextBox`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `EmptyImage` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `LayerUtility: Integer` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
