---
name: text_to_image_video_lora_sampler_163
type: Text To Image
frequency: 3
level: strong
coverage: 0.915
common_nodes: [ACE_AudioCrop, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLatentImage, GrowMaskWithBlur, ImageAndMaskPreview, ImageFromBatch, JjkText, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadSAM3Model, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewAny, PreviewImage, RH_LLMAPI_Pro_Node, RandomNoise, SAM3BBoxCollector, SAM3PointCollector, SAM3Segmentation, SAM3_TrackToMask, SAM3_VideoTrack, SamplerCustomAdvanced, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive, easy convertAnything, easy int, solarL_SaveImagesToZip, ttN concat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3模型驱动视频换头视频生视频实现面部无缝替换，视频生视频方案_2107573037087420418.json, 视频生成/图生视频/MiniMax_H3模型驱动视频换头，视频生视频实现面部无缝替换_2106921543413620737.json, 视频生成/图生视频/minimax H3视频换头自动遮罩版｜换脸不露痕迹边缘自然_2103718058362757122.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_163

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3模型驱动视频换头视频生视频实现面部无缝替换，视频生视频方案_2107573037087420418.json、视频生成/图生视频/MiniMax_H3模型驱动视频换头，视频生视频实现面部无缝替换_2106921543413620737.json、视频生成/图生视频/minimax H3视频换头自动遮罩版｜换脸不露痕迹边缘自然_2103718058362757122.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `ACE_AudioCrop`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GrowMaskWithBlur`
- `ImageAndMaskPreview`
- `ImageFromBatch`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadSAM3Model`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewAny`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SAM3BBoxCollector`
- `SAM3PointCollector`
- `SAM3Segmentation`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`
- `easy convertAnything`
- `easy int`
- `solarL_SaveImagesToZip`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `孤海注释` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
