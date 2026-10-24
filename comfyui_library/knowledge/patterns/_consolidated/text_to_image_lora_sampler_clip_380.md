---
name: text_to_image_lora_sampler_clip_380
type: Text To Image
frequency: 5
level: strong
coverage: 0.9206
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfySwitchNode, ConditioningZeroOut, CreateVideo, EmptyImage, EmptyLatentImage, GetImageSizeAndCount, ImageCompositeMasked, ImageFromBatch, ImageScaleToTotalPixels, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MaskPreview, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveBoolean, ResolutionSelector, SAM3_Detect, SAM3_TrackToMask, SAM3_VideoTrack, SaveVideo, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3视频驱动角色替换，动作迁移姿态复刻图生视频一致性方案_2103249643990769666.json, 视频生成/图生视频/MiniMax H3视频驱动角色替换，动作迁移姿态复刻图生视频一致性方案_2103595025631371265.json, 视频生成/图生视频/MiniMaxH3视频驱动角色替换 人物一致性更强_2108999228914753538.json, 视频生成/图生视频/MiniMaxH3视频驱动角色替换，动作迁移图生视频三合一_2110798532784517121.json, 视频生成/图生视频/MiniMaxH3视频驱动角色替换｜动作迁移图生视频一步到位_2110720119595954177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_380

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3视频驱动角色替换，动作迁移姿态复刻图生视频一致性方案_2103249643990769666.json、视频生成/图生视频/MiniMax H3视频驱动角色替换，动作迁移姿态复刻图生视频一致性方案_2103595025631371265.json、视频生成/图生视频/MiniMaxH3视频驱动角色替换 人物一致性更强_2108999228914753538.json、视频生成/图生视频/MiniMaxH3视频驱动角色替换，动作迁移图生视频三合一_2110798532784517121.json、视频生成/图生视频/MiniMaxH3视频驱动角色替换｜动作迁移图生视频一步到位_2110720119595954177.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyImage`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `ResolutionSelector`
- `SAM3_Detect`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SaveVideo`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 4/5 个有
- `DA3Inference` —— 2/5 个有
- `DA3Render` —— 2/5 个有
- `FeatherMask` —— 2/5 个有
- `GrowMask` —— 2/5 个有
- `LoadDA3Model` —— 2/5 个有
- `MiniMaxH3FunControlNetApply` —— 2/5 个有
- `ModelPatchLoader` —— 2/5 个有
- `PreviewImage` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| ControlNet 权重 | 0.2 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
