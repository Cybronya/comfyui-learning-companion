---
name: unknown_workflow_video_sampler_vae_60
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.75025
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.1-VACE+FusionX+NAG扩展视频_1934807918095343617.json, 视频生成/图生视频/vace阔图_1925382654517030913.json, 视频生成/图生视频/vace首尾帧_1925399301634109442.json, 视频生成/图生视频/【VACE系列】首尾帧工作流初体验_1925182598413545473.json, 视频生成/图生视频/最新Wan2.1+Vace  视频画面内容拓展【中文注释简单易懂】_1911760861873274882.json, 视频生成/图生视频/极速视频编辑 Self-Forcing + VACE nightly_1928359146670964738.json, 视频生成/文生视频/万相控制视频 VACE nightly_1923433916261126146.json, 视频生成/文生视频/🥪【大炮视频】FusionX VACE首尾帧+姿态迁移🥪_1934860931379699714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_60

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/WAN2.1-VACE+FusionX+NAG扩展视频_1934807918095343617.json、视频生成/图生视频/vace阔图_1925382654517030913.json、视频生成/图生视频/vace首尾帧_1925399301634109442.json、视频生成/图生视频/【VACE系列】首尾帧工作流初体验_1925182598413545473.json、视频生成/图生视频/最新Wan2.1+Vace  视频画面内容拓展【中文注释简单易懂】_1911760861873274882.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTeaCache` —— 7/8 个有
- `WanVideoTextEncode` —— 7/8 个有
- `WanVideoVACEModelSelect` —— 7/8 个有
- `ImagePadKJ` —— 6/8 个有
- `VHS_LoadVideo` —— 6/8 个有
- `GetImageRangeFromBatch` —— 5/8 个有
- `GetNode` —— 5/8 个有
- `ImageResizeKJv2` —— 5/8 个有
- `LoadImage` —— 5/8 个有
- `MaskPreview` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `WanVideoVACEStartToEndFrame` —— 5/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `DepthAnything_V2` —— 3/8 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 3/8 个有
- `ImageResizeKJ` —— 3/8 个有
- `MaskPreview+` —— 3/8 个有
- `WanVideoEnhanceAVideo` —— 3/8 个有
- `WanVideoApplyNAG` —— 2/8 个有
- `WanVideoMagCache` —— 2/8 个有
- `WanVideoTextEncodeSingle` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `WanVideoLoraSelect` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
