---
name: text_to_image_sampler_clip_unet_83
type: Text To Image
frequency: 8
level: weak
coverage: 0.91475
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AA--Z-image-base 和Zimage-turbo对比_2016204048063533058.json, 图片生成/文生图/AI牛马文生图写实风_2038437485671358466.json, 图片生成/文生图/Boogu_Turbo 文生图_2069444653648273409.json, 图片生成/文生图/Boogu_Turbo_文生图工作流_2069274849616416770.json, 图片生成/文生图/Boogu文生图标准版_2068941708238352385.json, 图片生成/文生图/Krea2_2K_4K直出_超写实人像光影_2095323854578216962.json, 图片生成/文生图/LH-DMT版本-2.生图片类-038. Z image_v3升级版更强提示词理解-文生图_2016524578054475777.json, 图片生成/文生图/Z-Anime-基于ZIB底模的动漫风格模型_2064727085071032322.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_83

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/AA--Z-image-base 和Zimage-turbo对比_2016204048063533058.json、图片生成/文生图/AI牛马文生图写实风_2038437485671358466.json、图片生成/文生图/Boogu_Turbo 文生图_2069444653648273409.json、图片生成/文生图/Boogu_Turbo_文生图工作流_2069274849616416770.json、图片生成/文生图/Boogu文生图标准版_2068941708238352385.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/8 个有
- `ModelSamplingAuraFlow` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `EmptySD3LatentImage` —— 1/8 个有
- `ImageScaleBy` —— 1/8 个有
- `Power Lora Loader (rgthree)` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `VAEEncode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 11 | 4 - 50 | 8 | 15% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 34% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 0.3 - 1 | 8 | 75% |
| 宽度 | 1080 | 1024 - 2048 | 8 | 70% |
| 高度 | 1052 | 1024 - 1920 | 8 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 11，观测区间 4 - 50，8 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，8 个样本
- 宽度 中位数 1080，观测区间 1024 - 2048，8 个样本
- 高度 中位数 1052，观测区间 1024 - 1920，8 个样本
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
