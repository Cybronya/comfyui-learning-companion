---
name: unknown_workflow_upscale_sampler_unet_17
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.815
common_nodes: [CreateVideo, GroupSwitcher, Image Comparer (rgthree), InvertBoolean, KSampler, LoadImage, PDIMAGE_LongerSize, PixaromaGroupSwitch, PrimitiveBoolean, PrimitiveInt, SaveImage, SaveVideo, SeedVR2Conditioning, SeedVR2Preprocess, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, VHS_LoadVideo, VHS_VideoInfoSource, VOSR2ModelLoader, VOSR2Upscale, ZML_SwitchOutput, easy compareVideos, easy ifElse, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/图像_视频高清放大_VORS2+SeedVR2_2114636603317645314.json, 图片生成/图生图/图像_视频高清放大_VORS2+SeedVR2_2115295764950904834.json, 平台全量/图像_视频高清放大  VORS2+SeedVR2_2109483780502286337.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_17

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图像_视频高清放大_VORS2+SeedVR2_2114636603317645314.json、图片生成/图生图/图像_视频高清放大_VORS2+SeedVR2_2115295764950904834.json、平台全量/图像_视频高清放大  VORS2+SeedVR2_2109483780502286337.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateVideo`
- `GroupSwitcher`
- `Image Comparer (rgthree)`
- `InvertBoolean`
- `KSampler`
- `LoadImage`
- `PDIMAGE_LongerSize`
- `PixaromaGroupSwitch`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `SaveImage`
- `SaveVideo`
- `SeedVR2Conditioning`
- `SeedVR2Preprocess`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoInfoSource`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `ZML_SwitchOutput`
- `easy compareVideos`
- `easy ifElse`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | 1 - 1 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
