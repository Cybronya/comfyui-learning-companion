---
name: text_to_image_sampler_clip_unet_40
type: Text To Image
frequency: 14
level: moderate
coverage: 0.921643
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image文生图_1993984303098953730.json, 图片生成/文生图/Z-image文生图_1994050196562706434.json, 图片生成/文生图/Z-image文生图_1994253056955138050.json, 图片生成/文生图/Z-image文生图_1994323420024422402.json, 图片生成/文生图/Z-image文生图_1994684914001977346.json, 图片生成/文生图/Z-image文生图_1996854775096516609.json, 图片生成/文生图/Z-image文生图_2002645259123322881.json, 图片生成/文生图/Z-image文生图_2003370209052401665.json, 图片生成/文生图/Z-image文生图——25年末的超级王炸_1994392372287053826.json, 图片生成/文生图/Z-image文生图奇幻风格_1997646513021104130.json, 图片生成/文生图/Z_image文生图-宫崎骏风格｜吉卜力风格｜卡通动漫｜二次元｜_2088507302923034626.json, 图片生成/文生图/krea2-turbo-极简极速文生图小说用_2103827094890434561.json, 图片生成/文生图/▶▷Krea2-标准生图)_2077775542920769537.json, 平台全量/▶▷MOSS-Image-文生图8步_2118900814457692161.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_40

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Z-image文生图_1993984303098953730.json、图片生成/文生图/Z-image文生图_1994050196562706434.json、图片生成/文生图/Z-image文生图_1994253056955138050.json、图片生成/文生图/Z-image文生图_1994323420024422402.json、图片生成/文生图/Z-image文生图_1994684914001977346.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 12/14 个有
- `LoraLoaderModelOnly` —— 6/14 个有
- `PreviewImage` —— 4/14 个有
- `Seed (rgthree)` —— 4/14 个有
- `Fast Groups Bypasser (rgthree)` —— 3/14 个有
- `CR Prompt Text` —— 2/14 个有
- `Label (rgthree)` —— 2/14 个有
- `Float` —— 1/14 个有
- `ImpactInt` —— 1/14 个有
- `JWInteger` —— 1/14 个有
- `ResolutionSelector` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 5 - 12 | 14 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 86% |
| 调度器 | simple | - | 14 | 79% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1080 | 688 - 1920 | 14 | 68% |
| 高度 | 1280 | 720 - 1920 | 14 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 5 - 12，14 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 86%
- 调度器 最常用 simple，14 个样本，一致性 79%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 688 - 1920，14 个样本
- 高度 中位数 1280，观测区间 720 - 1920，14 个样本
