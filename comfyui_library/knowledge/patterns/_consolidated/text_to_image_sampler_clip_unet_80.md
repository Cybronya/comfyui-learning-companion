---
name: text_to_image_sampler_clip_unet_80
type: Text To Image
frequency: 9
level: moderate
coverage: 0.951111
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ernie文生图质感_2044774941454766081.json, 图片生成/文生图/ideogram4_2062708650468265986.json, 图片生成/文生图/krea2 turbo文生图 极致美学_2069948625094012930.json, 图片生成/文生图/krea2 文生图 无LORA_2093341821593284609.json, 图片生成/文生图/krea2 文生图 无LORA_2111016861499486209.json, 图片生成/文生图/krea2的极致美学_2069777686637142018.json, 图片生成/文生图/longCat-基础文生图_2028462654980886530.json, 图片生成/文生图/miaomiao RealSkin Anima 1.0 文生图_2114597001806569473.json, 图片生成/文生图/二次元-anima模型-文生图_2055198430875660289.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_80

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/ernie文生图质感_2044774941454766081.json、图片生成/文生图/ideogram4_2062708650468265986.json、图片生成/文生图/krea2 turbo文生图 极致美学_2069948625094012930.json、图片生成/文生图/krea2 文生图 无LORA_2093341821593284609.json、图片生成/文生图/krea2 文生图 无LORA_2111016861499486209.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 2/9 个有
- `CFGNorm` —— 1/9 个有
- `CompressImages` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `SaveAnimatedWEBP` —— 1/9 个有
- `TextConcat` —— 1/9 个有
- `Textbox` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 40 | 9 | 45% |
| Prompt 约束强度(CFG) | 4 | 1 - 8 | 9 | 29% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 904 - 1920 | 9 | 75% |
| 高度 | 1536 | 1024 - 2280 | 9 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 40，9 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 8，9 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 904 - 1920，9 个样本
- 高度 中位数 1536，观测区间 1024 - 2280，9 个样本
