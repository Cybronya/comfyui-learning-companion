---
name: unknown_workflow_video_sampler_vae_117
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.81175
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, ImageConcatMulti, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1934799342199087105.json, 视频生成/图生视频/1936424375866281985.json, 视频生成/图生视频/1934580873092079617.json, 视频生成/文生视频/1935319269842550786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_117

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1934799342199087105.json、视频生成/图生视频/1936424375866281985.json、视频生成/图生视频/1934580873092079617.json、视频生成/文生视频/1935319269842550786.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `WanVideoMagCache` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `MaskPreview` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `easy int` —— 2/4 个有
- `ImpactInt` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `WanVideoEnhanceAVideo` —— 1/4 个有
- `WanVideoLoraSelect` —— 1/4 个有
- `WanVideoVACEModelSelect` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
