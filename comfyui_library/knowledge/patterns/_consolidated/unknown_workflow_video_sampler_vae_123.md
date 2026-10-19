---
name: unknown_workflow_video_sampler_vae_123
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7405
common_nodes: [ImageConcatMulti, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, Note Plus (mtb), VHS_VideoCombine, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1907454783161307138.json, 视频生成/图生视频/1922711297270452225.json, 视频生成/图生视频/1907459540840026113.json, 视频生成/图生视频/1907808853109387266.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_123

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1907454783161307138.json、视频生成/图生视频/1922711297270452225.json、视频生成/图生视频/1907459540840026113.json、视频生成/图生视频/1907808853109387266.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageConcatMulti`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Note Plus (mtb)`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerMask: BiRefNetUltraV2` —— 3/4 个有
- `LayerMask: LoadBiRefNetModelV2` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `WanVideoBlockSwap` —— 3/4 个有
- `GrowMaskWithBlur` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `JWImageResizeByLongerSide` —— 2/4 个有
- `LayerMask: LoadSegmentAnythingModels` —— 2/4 个有
- `LayerMask: SegmentAnythingUltra V3` —— 2/4 个有
- `TTP_Expand_And_Mask` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `InpaintPreprocessor` —— 1/4 个有
- `LayerUtility: ImageBlend V2` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `VHS_MergeImages` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有
- `WanVideoVACEModelSelect` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
