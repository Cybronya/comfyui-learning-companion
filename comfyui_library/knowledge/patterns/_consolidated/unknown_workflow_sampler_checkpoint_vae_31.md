---
name: unknown_workflow_sampler_checkpoint_vae_31
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.969
common_nodes: [CheckpointLoaderSimple, EmptyLatentImage, GetImageSizeAndCount, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AIO V5.3图像编辑王者LongCat Edit_1999826374938554369.json, 图片生成/图生图/LongCat Edit VS QwenEdit 2509 AIO V5.3_1997646158753411073.json, 图片生成/图生图/Qwen Edit Anything 2 Real卡通变真人V1_1997706066995646465.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_31

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/AIO V5.3图像编辑王者LongCat Edit_1999826374938554369.json、图片生成/图生图/LongCat Edit VS QwenEdit 2509 AIO V5.3_1997646158753411073.json、图片生成/图生图/Qwen Edit Anything 2 Real卡通变真人V1_1997706066995646465.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `Float` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `LongCatImageEdit` —— 2/3 个有
- `LongCatImageModelLoader` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `MemoryCleaner` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 3 | 100% |
| 高度 | 768 | 768 - 768 | 3 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
