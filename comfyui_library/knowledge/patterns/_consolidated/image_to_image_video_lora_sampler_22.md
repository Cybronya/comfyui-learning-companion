---
name: image_to_image_video_lora_sampler_22
type: Image To Image
frequency: 2
level: weak
coverage: 0.93
common_nodes: [CFGNorm, CLIPLoader, CLIPVisionLoader, CM_NearestSDXLResolution, CR Prompt Text, CR Text Concatenate, EmptyLatentImage, GetImageRangeFromBatch, GetNode, ImageBatch, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, ReverseImageBatch, Seed (rgthree), SetNode, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/飞行模式wan21训练版_1983410694139879426.json, 视频生成/图生视频/飞行模式wan21训练版_姿态参考_1983410617056993281.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/飞行模式wan21训练版_1983410694139879426.json、视频生成/图生视频/飞行模式wan21训练版_姿态参考_1983410617056993281.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPVisionLoader`
- `CM_NearestSDXLResolution`
- `CR Prompt Text`
- `CR Text Concatenate`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageBatch`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `ReverseImageBatch`
- `Seed (rgthree)`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEasyCache`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DrawViTPose` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `OnnxDetectionModelLoader` —— 1/2 个有
- `PoseAndFaceDetection` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
