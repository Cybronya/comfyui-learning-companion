---
name: image_to_image_video_lora_sampler_8
type: Image To Image
frequency: 3
level: strong
coverage: 0.892
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, FluxKontextImageScale, GetNode, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, Power Lora Loader (rgthree), PreviewImage, ReferenceLatent, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoFreeInitArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM V2, Power Lora Loader (rgthree)]
members: [图片生成/文生图/1945854630372798466.json, 视频生成/图生视频/1945854630372798466.json, 视频生成/图生视频/1945865001003610114.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_8

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1945854630372798466.json、视频生成/图生视频/1945854630372798466.json、视频生成/图生视频/1945865001003610114.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetNode`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Power Lora Loader (rgthree)`
- `PreviewImage`
- `ReferenceLatent`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoFreeInitArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 2/3 个有
- `GetImageSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM V2、Power Lora Loader (rgthree)
