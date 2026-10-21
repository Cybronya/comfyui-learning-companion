---
name: text_to_image_sampler_clip_unet_135
type: Text To Image
frequency: 3
level: moderate
coverage: 0.896
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Int, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image+SeedVR2-超真实人物照-文生图-图片放大-高清直出_1993893780149436418.json, 图片生成/文生图/Z-image_1995048903902998530.json, 图片生成/文生图/Z-image图片反推-文生图SeedVR2-放大_1994031072033832962.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_135

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image+SeedVR2-超真实人物照-文生图-图片放大-高清直出_1993893780149436418.json、图片生成/文生图/Z-image_1995048903902998530.json、图片生成/文生图/Z-image图片反推-文生图SeedVR2-放大_1994031072033832962.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Int`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `SeedVR2` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `AddLabel` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 2416 | 3 | 59% |
| 高度 | 1920 | 1080 - 1920 | 3 | 76% |
| 采样步数 | 10 | 10 - 14 | 3 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 2416，3 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，3 个样本
- 采样步数 中位数 10，观测区间 10 - 14，3 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
