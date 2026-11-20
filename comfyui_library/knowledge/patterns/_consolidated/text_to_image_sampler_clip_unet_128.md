---
name: text_to_image_sampler_clip_unet_128
type: Text To Image
frequency: 6
level: moderate
coverage: 0.878667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Anime VS Z-image  VS  ERNIE-image-动漫风格对比_2049475191444606977.json, 图片生成/文生图/Z-Anime-自动提示词二次元动漫生成_2049497102346100738.json, 图片生成/文生图/Z-Image-De-Turbo文生图_1997688531524980738.json, 图片生成/文生图/krea2+Afterlight+最强文生图(媲美MJ)_2082826253823995905.json, 图片生成/文生图/反推提示词+Z-image文生图_2015983039649681410.json, 图片生成/文生图/百度ERNIE-image-tubro-文生图+Qwen3.5提示词增加优化_2044778668962095105.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_128

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-Anime VS Z-image  VS  ERNIE-image-动漫风格对比_2049475191444606977.json、图片生成/文生图/Z-Anime-自动提示词二次元动漫生成_2049497102346100738.json、图片生成/文生图/Z-Image-De-Turbo文生图_1997688531524980738.json、图片生成/文生图/krea2+Afterlight+最强文生图(媲美MJ)_2082826253823995905.json、图片生成/文生图/反推提示词+Z-image文生图_2015983039649681410.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `llama_cpp_instruct_adv` —— 4/6 个有
- `llama_cpp_model_loader` —— 4/6 个有
- `LoadImage` —— 3/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `Qwen3_VQA` —— 2/6 个有
- `AddLabel` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 6 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 6 | 44% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 896 | 720 - 1080 | 6 | 84% |
| 高度 | 1280 | 1280 - 1920 | 6 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，6 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，6 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 720 - 1080，6 个样本，取值集中（一致性 84%）
- 高度 中位数 1280，观测区间 1280 - 1920，6 个样本
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
