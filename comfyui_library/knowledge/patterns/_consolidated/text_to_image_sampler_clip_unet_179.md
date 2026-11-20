---
name: text_to_image_sampler_clip_unet_179
type: Text To Image
frequency: 3
level: strong
coverage: 0.827
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoadImage, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image 洗图流：简约反推提示词+放大_2001900316637446145.json, 图片生成/文生图/Z-image 文生图（提示词反推+高清修复）_1993866861928448001.json, 数字人/数字人/真实人物_1994430521302192129.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_179

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-image 洗图流：简约反推提示词+放大_2001900316637446145.json、图片生成/文生图/Z-image 文生图（提示词反推+高清修复）_1993866861928448001.json、数字人/数字人/真实人物_1994430521302192129.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `ShowText` —— 2/3 个有
- `AspectRatio` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 720 | 720 - 1920 | 3 | 49% |
| 高度 | 1280 | 1080 - 1280 | 3 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 720 - 1920，3 个样本，取值分散，一致性仅 49%
- 高度 中位数 1280，观测区间 1080 - 1280，3 个样本，取值集中（一致性 92%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
