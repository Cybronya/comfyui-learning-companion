---
name: text_to_image_sampler_clip_unet_69
type: Text To Image
frequency: 9
level: moderate
coverage: 0.893889
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2 写实文生图_2069944402356817921.json, 图片生成/图生图/Z-image文生图去AI感_2026166309813227522.json, 图片生成/图生图/Z-image最新优化版（速度快）_1995420868127940610.json, 图片生成/图生图/z-image-turbo-参考图生图_2057716109838733314.json, 图片生成/图生图/z-image图生图工作流_2001988545583673345.json, 图片生成/图生图/z-image图生图工作流_2009950317806358530.json, 图片生成/文生图/001.Z-image生图巅峰005.五列表文生图.json_2033727476014260226.json, 图片生成/文生图/Krea2 写实文生图_2069839901595619329.json, 图片生成/文生图/Z-image增强真实感_1995774071407259650.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_69

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Krea2 写实文生图_2069944402356817921.json、图片生成/图生图/Z-image文生图去AI感_2026166309813227522.json、图片生成/图生图/Z-image最新优化版（速度快）_1995420868127940610.json、图片生成/图生图/z-image-turbo-参考图生图_2057716109838733314.json、图片生成/图生图/z-image图生图工作流_2001988545583673345.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy promptList` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `LoadImage` —— 3/9 个有
- `PrimitiveInt` —— 3/9 个有
- `VAEEncode` —— 3/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `Dapao_LlamaChat` —— 1/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `ModelSamplingAuraFlow` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 480 - 1280 | 9 | 76% |
| 高度 | 1536 | 720 - 1920 | 9 | 68% |
| 采样步数 | 9 | 6 - 10 | 9 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 0.8 - 1 | 9 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 480 - 1280，9 个样本
- 高度 中位数 1536，观测区间 720 - 1920，9 个样本
- 采样步数 中位数 9，观测区间 6 - 10，9 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，9 个样本，取值集中（一致性 91%）
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
