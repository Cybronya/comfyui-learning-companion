---
name: text_to_image_controlnet_ipadapter_video
type: Text To Image
frequency: 3
level: strong
coverage: 0.813
common_nodes: [ACN_AdvancedControlNetApply, ADE_ApplyAnimateDiffModelSimple, ADE_LoadAnimateDiffModel, ADE_LoopedUniformContextOptions, ADE_MultivalDynamic, ADE_UseEvolvedSampling, BatchCount+, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoaderAdvanced, CreateFadeMaskAdvanced, EmptyLatentImage, IPAdapterUnifiedLoader, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, MaskToImage, PreviewImage, RepeatImageBatch, SimpleMath+, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_SplitImages, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1915253502032154625.json, 视频生成/图生视频/1787313920449458177.json, 视频生成/图生视频/1787418483718369281.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_video

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1915253502032154625.json、视频生成/图生视频/1787313920449458177.json、视频生成/图生视频/1787418483718369281.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `ACN_AdvancedControlNetApply`
- `ADE_ApplyAnimateDiffModelSimple`
- `ADE_LoadAnimateDiffModel`
- `ADE_LoopedUniformContextOptions`
- `ADE_MultivalDynamic`
- `ADE_UseEvolvedSampling`
- `BatchCount+`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoaderAdvanced`
- `CreateFadeMaskAdvanced`
- `EmptyLatentImage`
- `IPAdapterUnifiedLoader`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `PreviewImage`
- `RepeatImageBatch`
- `SimpleMath+`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_SplitImages`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `IPAdapterBatch` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `Color Correct (mtb)` —— 1/3 个有
- `FILM VFI` —— 1/3 个有
- `IPAdapterAdvanced` —— 1/3 个有
- `IPAdapterNoise` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `ImageSharpen` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 11 | 11 - 11 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | lcm | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 0.4 - 1 | 3 | 65% |
| ControlNet 权重 | 0.4 | 0.4 - 0.45 | 3 | 94% |
| 宽度 | 360 | 320 - 512 | 3 | 79% |
| 高度 | 512 | 384 - 568 | 3 | 84% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 11，观测区间 11 - 11，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，3 个样本
- ControlNet 权重 中位数 0.4，观测区间 0.4 - 0.45，3 个样本，取值集中（一致性 94%）
- 宽度 中位数 360，观测区间 320 - 512，3 个样本
- 高度 中位数 512，观测区间 384 - 568，3 个样本，取值集中（一致性 84%）
