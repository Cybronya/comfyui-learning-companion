---
name: unknown_workflow_video_sampler_clip_131
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78425
common_nodes: [ImageConcanate, ImageSizeInfo, JWImageResizeByLongerSide, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, MarwanFaceCropping, PreviewImage, TTP_Expand_And_Mask, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/通义万相KISS图生视频WAN工作流V1_1895031951948972033.json, 视频生成/图生视频/1895031951948972033.json, 视频生成/图生视频/1895076353941307393.json, 视频生成/图生视频/1894963534298546178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_131

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/通义万相KISS图生视频WAN工作流V1_1895031951948972033.json、视频生成/图生视频/1895031951948972033.json、视频生成/图生视频/1895076353941307393.json、视频生成/图生视频/1894963534298546178.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageConcanate`
- `ImageSizeInfo`
- `JWImageResizeByLongerSide`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `MarwanFaceCropping`
- `PreviewImage`
- `TTP_Expand_And_Mask`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 2/4 个有
- `WanVideoExperimentalArgs` —— 2/4 个有
- `WanVideoSLG` —— 2/4 个有
- `WanVideoTeaCache` —— 2/4 个有
- `Note _O` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
