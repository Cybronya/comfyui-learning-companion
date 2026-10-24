---
name: text_to_image_sampler_clip_vae_10
type: Text To Image
frequency: 12
level: moderate
coverage: 0.918167
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Midjourney_1970301959590866945.json, 图片生成/文生图/Mymang-Qwen 2509 AIO文生图_1977361796124286978.json, 图片生成/文生图/Q版_1978028438453891074.json, 图片生成/文生图/RealRose LoRA生图工作流_1919938265468567553.json, 图片生成/文生图/Red-Z image Base-10步出图极速版_2018674863816318977.json, 图片生成/文生图/SuperZimage图片处理（4K文生图）_2041019748875509762.json, 图片生成/文生图/Z-Anime-动漫文生图_2049110641390129153.json, 图片生成/文生图/Z-IMAGE 文生图工作流_2071465207611871233.json, 图片生成/文生图/Z-Image-Base高质量多细节文生图_2015636535781101570.json, 图片生成/文生图/Z-Image镜片·光学镜片场景生成_2044682719262674946.json, 图片生成/文生图/Z-image最强真实人物细节多场景生成_2003710733722525697.json, 图片生成/文生图/超智能提示词反推照片V2_2004362690019684353.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_10

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Midjourney_1970301959590866945.json、图片生成/文生图/Mymang-Qwen 2509 AIO文生图_1977361796124286978.json、图片生成/文生图/Q版_1978028438453891074.json、图片生成/文生图/RealRose LoRA生图工作流_1919938265468567553.json、图片生成/文生图/Red-Z image Base-10步出图极速版_2018674863816318977.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 9/12 个有
- `VAELoader` —— 9/12 个有
- `CLIPLoader` —— 8/12 个有
- `PreviewImage` —— 6/12 个有
- `CheckpointLoaderSimple` —— 4/12 个有
- `AspectRatio` —— 3/12 个有
- `ConditioningZeroOut` —— 3/12 个有
- `LoraLoader` —— 3/12 个有
- `ModelSamplingAuraFlow` —— 3/12 个有
- `easy promptList` —— 3/12 个有
- `DyPE_FLUX` —— 1/12 个有
- `Fast Groups Muter (rgthree)` —— 1/12 个有
- `LayerUtility: PurgeVRAM` —— 1/12 个有
- `Text Multiline` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12.5 | 4 - 30 | 12 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 12 | 0% |
| 采样算法 | euler | - | 12 | 67% |
| 调度器 | simple | - | 12 | 58% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1052 | 504 - 4096 | 12 | 31% |
| 高度 | 1180 | 720 - 2048 | 12 | 71% |
| LoRA 模型强度 | 0.8 | 0.7 - 0.8 | 3 | 94% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12.5，观测区间 4 - 30，12 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，12 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，12 个样本，一致性 67%
- 调度器 最常用 simple，12 个样本，一致性 58%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 504 - 4096，12 个样本，取值分散，一致性仅 31%
- 高度 中位数 1180，观测区间 720 - 2048，12 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.7 - 0.8，3 个样本，取值集中（一致性 94%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
