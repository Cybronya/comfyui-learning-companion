---
name: image_to_image_video_lora_sampler_20
type: Image To Image
frequency: 2
level: weak
coverage: 0.686
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CR Prompt Text, ConditioningZeroOut, DrawViTPose, EmptyFlux2LatentImage, FillMaskWithColor, GetImageSize, GetNode, ImageResizeKJv2, ImageScaleToTotalPixels, JWInteger, KSampler, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LayerUtility: PurgeVRAM V2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, ReferenceLatent, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoSource, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/本地开源免费，sea sponge swing_2057138676102160386.json, 视频生成/图生视频/本地开源免费，拿破仑进行曲换脸版_2056990007289798657.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/本地开源免费，sea sponge swing_2057138676102160386.json、视频生成/图生视频/本地开源免费，拿破仑进行曲换脸版_2056990007289798657.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DrawViTPose`
- `EmptyFlux2LatentImage`
- `FillMaskWithColor`
- `GetImageSize`
- `GetNode`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `JWInteger`
- `KSampler`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `ReferenceLatent`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
