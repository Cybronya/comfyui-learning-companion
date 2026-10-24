---
name: unknown_workflow_lora_sampler_unet_79
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.8725
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2511 Vs 2509 VS AIO 5.3图像编辑对比_2003654613410693122.json, 图片生成/图生图/Qwen Edit 2511 vs 2509 vs aio5.3双图编辑对比_2003805263956221954.json, 图片生成/图生图/Qwen Edit 2511 vs 2509 vs aio5.3双图编辑对比（蒙版操作）_2003666330425409538.json, 图片生成/图生图/Qwen Edit 2511 双图编辑V1（一致性加强版）_2005539977784160257.json, 图片生成/图生图/Qwen Edit 2511多种模型效果对比_2004546822368624642.json, 图片生成/图生图/单图编辑Qwen Edit 2511 Vs 2509 VS AIO 5.3版的对比_2003748383162572802.json, 图片生成/图生图/图像编辑对比Qwen Edit 2511 Vs 2509_2004017562595803137.json, 图片生成/文生图/Qwen image Edit 2511_2509_Aio 5.3效果对比_2004920649099476993.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_79

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2511 Vs 2509 VS AIO 5.3图像编辑对比_2003654613410693122.json、图片生成/图生图/Qwen Edit 2511 vs 2509 vs aio5.3双图编辑对比_2003805263956221954.json、图片生成/图生图/Qwen Edit 2511 vs 2509 vs aio5.3双图编辑对比（蒙版操作）_2003666330425409538.json、图片生成/图生图/Qwen Edit 2511 双图编辑V1（一致性加强版）_2005539977784160257.json、图片生成/图生图/Qwen Edit 2511多种模型效果对比_2004546822368624642.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 7/8 个有
- `ImageConcatMulti` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `CheckpointLoaderSimple` —— 6/8 个有
- `PDIMAGE_LongerSize` —— 6/8 个有
- `LayerUtility: PurgeVRAM` —— 5/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `CR Prompt Text` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `DuckHideNode` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `Textbox` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | beta57 | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 beta57，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（23/8 个样本）：Steps较低可能导致细节不足
