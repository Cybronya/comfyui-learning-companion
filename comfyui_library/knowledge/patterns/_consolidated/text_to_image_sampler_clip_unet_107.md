---
name: text_to_image_sampler_clip_unet_107
type: Text To Image
frequency: 7
level: moderate
coverage: 0.919714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2031033876067393537.json, 图片生成/文生图/2031306114851147777.json, 图片生成/文生图/251225001.013. Z image_v3升级版更强提示词理解_2004252074999246849.json, 图片生成/文生图/87time 造相-Z-Image-Turbo_1992926870398238721.json, 图片生成/文生图/AA--Z-image-base 和Zimage-turbo对比_2016204048063533058.json, 图片生成/文生图/Z-image-文生图（自用测试版）_2052717804557742081.json, 图片生成/文生图/Z-image轻量级 AI 图像生成_1994293019830665217.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_107

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/2031033876067393537.json、图片生成/文生图/2031306114851147777.json、图片生成/文生图/251225001.013. Z image_v3升级版更强提示词理解_2004252074999246849.json、图片生成/文生图/87time 造相-Z-Image-Turbo_1992926870398238721.json、图片生成/文生图/AA--Z-image-base 和Zimage-turbo对比_2016204048063533058.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/7 个有
- `ModelSamplingAuraFlow` —— 3/7 个有
- `EmptySD3LatentImage` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 2/7 个有
- `AnyAspectRatio` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImpactInt` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 832 - 1920 | 7 | 67% |
| 高度 | 1368 | 1080 - 1920 | 7 | 76% |
| 采样步数 | 10 | 7 - 50 | 7 | 23% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 41% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 832 - 1920，7 个样本
- 高度 中位数 1368，观测区间 1080 - 1920，7 个样本
- 采样步数 中位数 10，观测区间 7 - 50，7 个样本，取值分散，一致性仅 23%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
