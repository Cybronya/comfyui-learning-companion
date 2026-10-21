---
name: unknown_workflow_video_lora_sampler_150
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.665417
common_nodes: [CLIPLoader, CLIPVisionLoader, DWPreprocessor, EmptySD3LatentImage, FaceMaskFromPoseKeypoints, GetNode, ImageCropByMaskAndResize, ImageResizeKJv2, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, PixelPerfectResolution, PrimitiveInt, SetNode, SimpleMath+, Text, Text Concatenate, Text Multiline, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2070319838932848642.json, 视频生成/图生视频/1989649967868506113.json, 视频生成/图生视频/2039884885216727041.json, 视频生成/图生视频/1975542884365635585.json, 视频生成/图生视频/2058746076395565058.json, 视频生成/图生视频/2010268951330164737.json, 视频生成/图生视频/2059808792103178241.json, 视频生成/图生视频/2064897106015510530.json, 视频生成/图生视频/2062118089738776577.json, 视频生成/图生视频/2067052913171714049.json, 视频生成/图生视频/2072208106070822914.json, 视频生成/图生视频/2072484558993444865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_150

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/2070319838932848642.json、视频生成/图生视频/1989649967868506113.json、视频生成/图生视频/2039884885216727041.json、视频生成/图生视频/1975542884365635585.json、视频生成/图生视频/2058746076395565058.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `EmptySD3LatentImage`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PixelPerfectResolution`
- `PrimitiveInt`
- `SetNode`
- `SimpleMath+`
- `Text`
- `Text Concatenate`
- `Text Multiline`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 11/12 个有
- `VHS_VideoCombine` —— 11/12 个有
- `CFGNorm` —— 1/12 个有
- `ModelSamplingAuraFlow` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `TT_img_enc_v2` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
