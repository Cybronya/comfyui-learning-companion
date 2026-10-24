---
name: unknown_workflow_sampler_vae_23
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.976545
common_nodes: [EmptyLatentImage, GetImageSizeAndCount, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2511三图编辑V1_2004063684311826433.json, 图片生成/图生图/Qwen Edit 2511三图编辑_2007451400346804226.json, 图片生成/图生图/Qwen Edit 2511三图编辑_2013275595538440193.json, 图片生成/图生图/Qwen Edit 2511双图编辑-{姿势迁移}_2004097691007238145.json, 图片生成/图生图/Qwen Edit 2511双图编辑-{姿势迁移}_2004110460536406018.json, 图片生成/图生图/Qwen Edit 2511双图编辑V1（姿势迁移-高成功率版）_2003814602951540738.json, 图片生成/图生图/Qwen Edit 2511四视图草图化Lora对比_2004170555572035586.json, 图片生成/图生图/Qwen-Edit Aio V4模型双图编辑（姿势迁移）_1977742904007557121.json, 图片生成/图生图/Qwen-Edit Aio V5模型双图编辑（姿势迁移）_1978125750916243457.json, 图片生成/图生图/Qwen-Edit Aio V7模型双图编辑（姿势迁移）_1985328636607741953.json, 图片生成/图生图/Qwen动作迁移+SeedVR2_2031548094671753217.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_23

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2511三图编辑V1_2004063684311826433.json、图片生成/图生图/Qwen Edit 2511三图编辑_2007451400346804226.json、图片生成/图生图/Qwen Edit 2511三图编辑_2013275595538440193.json、图片生成/图生图/Qwen Edit 2511双图编辑-{姿势迁移}_2004097691007238145.json、图片生成/图生图/Qwen Edit 2511双图编辑-{姿势迁移}_2004110460536406018.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
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
- `CLIPLoader` —— 8/11 个有
- `ImageConcatMulti` —— 8/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `UNETLoader` —— 8/11 个有
- `VAELoader` —— 8/11 个有
- `DWPreprocessor` —— 7/11 个有
- `PDIMAGE_LongerSize` —— 7/11 个有
- `CheckpointLoaderSimple` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `AddLabel` —— 1/11 个有
- `INTConstant` —— 1/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `SeedVR2` —— 1/11 个有
- `SeedVR2BlockSwap` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 73% |
| 调度器 | beta57 | - | 11 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 768 | 768 - 768 | 11 | 100% |
| 高度 | 768 | 768 - 768 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 73%
- 调度器 最常用 beta57，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，11 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 768 - 768，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
