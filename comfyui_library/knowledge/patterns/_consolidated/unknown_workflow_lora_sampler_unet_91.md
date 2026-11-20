---
name: unknown_workflow_lora_sampler_unet_91
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.856111
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2511双图融合_2011333778131656706.json, 图片生成/图生图/qwen编辑plus_1957721637841989634.json, 图片生成/图生图/图像转证件照qwen编辑plus_1971115039363080193.json, 图片生成/图生图/电商产品展示 单图参考 qwen2511_2012505537132371969.json, 图片生成/图生图/电商产品展示 双图参考 qwen2511_2012719006670655489.json, 图片生成/图生图/电商产品展示 固定模特Ip_1986229520292347906.json, 图片生成/图生图/雪7.tonnie-edit 2509-提取服装_2002798214925414402.json, 平台全量/电商三图参考生图 千问Plus_1977590192519434242.json, 平台全量/电商双图参考生图 千问Plus_1977545005961236481.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_91

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/qwen2511双图融合_2011333778131656706.json、图片生成/图生图/qwen编辑plus_1957721637841989634.json、图片生成/图生图/图像转证件照qwen编辑plus_1971115039363080193.json、图片生成/图生图/电商产品展示 单图参考 qwen2511_2012505537132371969.json、图片生成/图生图/电商产品展示 双图参考 qwen2511_2012719006670655489.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 7/9 个有
- `CFGNorm` —— 6/9 个有
- `TextEncodeQwenImageEditPlus` —— 6/9 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 5/9 个有
- `EmptyLatentImage` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `RepeatLatentBatch` —— 3/9 个有
- `TextEncodeQwenImageEdit` —— 3/9 个有
- `ImageAndMaskPreview` —— 2/9 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/9 个有
- `Image Levels Adjustment` —— 1/9 个有
- `ImpactInt` —— 1/9 个有
- `PreviewImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1184 | 3 | 83% |
| 高度 | 1536 | 1280 - 1656 | 3 | 89% |
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1184，3 个样本，取值集中（一致性 83%）
- 高度 中位数 1536，观测区间 1280 - 1656，3 个样本，取值集中（一致性 89%）
- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
