---
name: unknown_workflow_lora_sampler_unet_143
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8816
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问图像编辑Plus增强版image_edit多图融合，人物一致性，姿态迁移，服装迁移_1968691125903085570.json, 图片生成/图生图/图像转证件照qwen编辑plus_1971115039363080193.json, 图片生成/图生图/图生图-控制姿势：Qwen-Image Edit Plus_1988231763208093697.json, 图片生成/图生图/图生图：Qwen-Image Edit Plus_1986626403615571970.json, 图片生成/图生图/指定图片人物，文生图换背景，_2043663846178562050.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_143

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/千问图像编辑Plus增强版image_edit多图融合，人物一致性，姿态迁移，服装迁移_1968691125903085570.json、图片生成/图生图/图像转证件照qwen编辑plus_1971115039363080193.json、图片生成/图生图/图生图-控制姿势：Qwen-Image Edit Plus_1988231763208093697.json、图片生成/图生图/图生图：Qwen-Image Edit Plus_1986626403615571970.json、图片生成/图生图/指定图片人物，文生图换背景，_2043663846178562050.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 4/5 个有
- `AIO_Preprocessor` —— 3/5 个有
- `CFGNorm` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `OpenposePreprocessor` —— 2/5 个有
- `TextEncodeQwenImageEdit` —— 2/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 5 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 5 | 82% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1080 | 928 - 1184 | 5 | 92% |
| 高度 | 1656 | 1536 - 1920 | 5 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，5 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，5 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 928 - 1184，5 个样本，取值集中（一致性 92%）
- 高度 中位数 1656，观测区间 1536 - 1920，5 个样本，取值集中（一致性 92%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
