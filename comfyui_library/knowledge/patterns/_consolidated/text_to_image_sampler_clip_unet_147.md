---
name: text_to_image_sampler_clip_unet_147
type: Text To Image
frequency: 5
level: strong
coverage: 0.9136
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Int, KSampler, LayerUtility: PurgeVRAM V2, SaveImage, SeedVR2, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image+SeedVR2-文生图-图片放大-高清直出_2021747203928236033.json, 图片生成/文生图/Z-image+SeedVR2-文生图-高清出图_2081632081444167681.json, 图片生成/文生图/Z-image+SeedVR2-超真实人物照-文生图-图片放大-高清直出_1993893780149436418.json, 图片生成/文生图/Z-image图片反推-文生图SeedVR2-放大_1994031072033832962.json, 图片生成/文生图/书法字体-毛笔字-Z-image+SeedVR2-文生图-图片放大-高清直出_2034222491228446722.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_147

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-image+SeedVR2-文生图-图片放大-高清直出_2021747203928236033.json、图片生成/文生图/Z-image+SeedVR2-文生图-高清出图_2081632081444167681.json、图片生成/文生图/Z-image+SeedVR2-超真实人物照-文生图-图片放大-高清直出_1993893780149436418.json、图片生成/文生图/Z-image图片反推-文生图SeedVR2-放大_1994031072033832962.json、图片生成/文生图/书法字体-毛笔字-Z-image+SeedVR2-文生图-图片放大-高清直出_2034222491228446722.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Int`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `SeedVR2`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CustomAddLabel` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `AddLabel` —— 1/5 个有
- `CR Text Replace` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RH_LLMAPI_Pro_Node` —— 1/5 个有
- `ShowText` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 5 | 100% |
| 高度 | 1920 | 1920 - 1920 | 5 | 100% |
| 采样步数 | 10 | 10 - 10 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
