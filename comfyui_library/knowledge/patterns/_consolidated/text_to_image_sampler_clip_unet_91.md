---
name: text_to_image_sampler_clip_unet_91
type: Text To Image
frequency: 5
level: strong
coverage: 0.9176
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, SaveImage, SeedVR2, SeedVR2BlockSwap, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen_文生图_都市动漫风格_1994239278764982273.json, 图片生成/文生图/Qwen_文生图_都市动漫风格_1994278880112476161.json, 图片生成/文生图/Z-image基础工作流+白茶月光超级清纯大模型+ SeedVR 4K 超清放大_2081687162319364097.json, 图片生成/文生图/lty_古风动漫V1.0_1992764574332153857.json, 图片生成/文生图/超美人像：瑶光+如梦似幻【漫剧资产创建】_2062895287097708546.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_91

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen_文生图_都市动漫风格_1994239278764982273.json、图片生成/文生图/Qwen_文生图_都市动漫风格_1994278880112476161.json、图片生成/文生图/Z-image基础工作流+白茶月光超级清纯大模型+ SeedVR 4K 超清放大_2081687162319364097.json、图片生成/文生图/lty_古风动漫V1.0_1992764574332153857.json、图片生成/文生图/超美人像：瑶光+如梦似幻【漫剧资产创建】_2062895287097708546.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `SeedVR2ExtraArgs` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `LoadImage` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `TTResolutionSelector` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `easy int` —— 1/5 个有
- `easy promptLine` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 720 - 1920 | 5 | 55% |
| 高度 | 1280 | 1080 - 1920 | 5 | 79% |
| 采样步数 | 8 | 8 - 9 | 5 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 720 - 1920，5 个样本
- 高度 中位数 1280，观测区间 1080 - 1920，5 个样本
- 采样步数 中位数 8，观测区间 8 - 9，5 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
