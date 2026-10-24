---
name: text_to_image_sampler_clip_unet_170
type: Text To Image
frequency: 3
level: strong
coverage: 0.789
common_nodes: [AILab_QwenVL, AddLabel, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LayerUtility: PurgeVRAM V2, SaveImage, SeedVR2, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Z-image+SeedVR2+QwenVL-最强一键洗图-图片反推-高清直出_1995102033059438594.json, 图片生成/图生图/Z-image+SeedVR2-海报洗图-图片反推-文生图-图片放大-高清直出_1993989854629396481.json, 图片生成/文生图/Z-image+SeedVR2-自动提示词-高清直出_1994317340802220034.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_170

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-image+SeedVR2+QwenVL-最强一键洗图-图片反推-高清直出_1995102033059438594.json、图片生成/图生图/Z-image+SeedVR2-海报洗图-图片反推-文生图-图片放大-高清直出_1993989854629396481.json、图片生成/文生图/Z-image+SeedVR2-自动提示词-高清直出_1994317340802220034.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `SeedVR2`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchTextReplace` —— 2/3 个有
- `Int` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PrimitiveBoolean` —— 2/3 个有
- `easy ifElse` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `JWStringMultiline` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `easy promptList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 720 - 1080 | 3 | 82% |
| 高度 | 1920 | 1280 - 1920 | 3 | 82% |
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 720 - 1080，3 个样本，取值集中（一致性 82%）
- 高度 中位数 1920，观测区间 1280 - 1920，3 个样本，取值集中（一致性 82%）
- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
