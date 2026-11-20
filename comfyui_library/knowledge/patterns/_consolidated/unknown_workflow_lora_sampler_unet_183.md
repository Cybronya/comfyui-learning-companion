---
name: unknown_workflow_lora_sampler_unet_183
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8132
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/批量电商去logo变白底图放大工作流_2009470367953330177.json, 图片生成/文生图/Qwen-edit-图像编辑_2087118096384479233.json, 平台全量/Qwen-图像编辑-产品精修-批量_2081655659585687554.json, 平台全量/qwen-edit_2511高清放大流_2006264678862819329.json, 平台全量/千问图片编辑（支持多图参考）qwen2511最新版_1980812503116632065.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_183

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/批量电商去logo变白底图放大工作流_2009470367953330177.json、图片生成/文生图/Qwen-edit-图像编辑_2087118096384479233.json、平台全量/Qwen-图像编辑-产品精修-批量_2081655659585687554.json、平台全量/qwen-edit_2511高清放大流_2006264678862819329.json、平台全量/千问图片编辑（支持多图参考）qwen2511最新版_1980812503116632065.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `TextEncodeQwenImageEditPlusPro_lrzjason` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `ImageUpscaleWithModel` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `LayerUtility: LoadImagesFromPath` —— 2/5 个有
- `UpscaleModelLoader` —— 2/5 个有
- `DF_Text_Box` —— 1/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `TextEncodeQwenImageEditPlus` —— 1/5 个有
- `Upscale Model Loader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1824 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
