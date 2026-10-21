---
name: unknown_workflow_video_sampler_vae_45
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7104
common_nodes: [GetImageSizeAndCount, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1925382654517030913.json, 视频生成/图生视频/1925399301634109442.json, 视频生成/图生视频/1926507512189624322.json, 视频生成/图生视频/1926119230994018305.json, 视频生成/图生视频/1925182598413545473.json, 视频生成/图生视频/1924743024252022785.json, 视频生成/图生视频/1923359866998411265.json, 视频生成/图生视频/1928359146670964738.json, 视频生成/文生视频/1923433916261126146.json, 视频生成/文生视频/1934860931379699714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_45

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1925382654517030913.json、视频生成/图生视频/1925399301634109442.json、视频生成/图生视频/1926507512189624322.json、视频生成/图生视频/1926119230994018305.json、视频生成/图生视频/1925182598413545473.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 10 个 workflow 都包含：
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 9/10 个有
- `EmptyImage` —— 9/10 个有
- `ImageConcatMulti` —— 9/10 个有
- `WanVideoTeaCache` —— 9/10 个有
- `GetNode` —— 8/10 个有
- `LoadImage` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `VHS_LoadVideo` —— 8/10 个有
- `WanVideoVACEStartToEndFrame` —— 8/10 个有
- `ImageResizeKJv2` —— 7/10 个有
- `MaskPreview` —— 7/10 个有
- `DepthAnything_V2` —— 6/10 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 6/10 个有
- `ImagePadKJ` —— 6/10 个有
- `WanVideoTorchCompileSettings` —— 6/10 个有
- `GetImageRangeFromBatch` —— 5/10 个有
- `WanVideoLoraSelect` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `ImageResizeKJ` —— 3/10 个有
- `MaskPreview+` —— 3/10 个有
- `WanVideoEnhanceAVideo` —— 3/10 个有
- `ImageFromBatch+` —— 2/10 个有
- `ImageResize+` —— 1/10 个有
- `ImpactInt` —— 1/10 个有
- `MimicMotionGetPoses` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `WanVideoApplyNAG` —— 1/10 个有
- `WanVideoMagCache` —— 1/10 个有
- `WanVideoTextEncodeSingle` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
