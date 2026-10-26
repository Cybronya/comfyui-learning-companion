---
name: unknown_workflow_video_inpaint_sampler_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.743
common_nodes: [GetNode, GrowMaskWithBlur, ImageResizeKJ, InpaintPreprocessor, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LoadImage, LoadWanVideoT5TextEncoder, MaskToImage, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1 FusionX VACE视频编辑_1949674343244144641.json, 视频生成/图生视频/视频版万物迁移_1934214235734106114.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.1 FusionX VACE视频编辑_1949674343244144641.json、视频生成/图生视频/视频版万物迁移_1934214235734106114.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `GrowMaskWithBlur`
- `ImageResizeKJ`
- `InpaintPreprocessor`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskToImage`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `ColorMatch` —— 1/2 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/2 个有
- `GIMMVFI_interpolate` —— 1/2 个有
- `ImageBlend` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageSmartSharpen+` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `Int` —— 1/2 个有
- `LoadImageFromUrl` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `WanVideoVACEModelSelect` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
