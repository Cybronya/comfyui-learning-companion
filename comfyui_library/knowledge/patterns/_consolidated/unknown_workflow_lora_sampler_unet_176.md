---
name: unknown_workflow_lora_sampler_unet_176
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7952
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物自动换衣服，生成模特穿版图 Qwen 升级版_1985702289119879170.json, 图片生成/图生图/低成本一键换装_2048011891754147841.json, 平台全量/Qwen Edit 2511万物迁移(无偏移蒙版双图版)_2004168352312532994.json, 平台全量/Qwen+Edit+2511无偏移换装_2005232407508910082.json, 平台全量/QwenEditUtils ——遮罩区域丝滑换装_1988952185385922561.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_176

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/人物自动换衣服，生成模特穿版图 Qwen 升级版_1985702289119879170.json、图片生成/图生图/低成本一键换装_2048011891754147841.json、平台全量/Qwen Edit 2511万物迁移(无偏移蒙版双图版)_2004168352312532994.json、平台全量/Qwen+Edit+2511无偏移换装_2005232407508910082.json、平台全量/QwenEditUtils ——遮罩区域丝滑换装_1988952185385922561.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `QwenEditAdaptiveLongestEdge` —— 3/5 个有
- `PreviewAny` —— 1/5 个有
- `QwenEditAny2Image` —— 1/5 个有
- `QwenEditAny2Latent` —— 1/5 个有
- `QwenEditConfigJsonParser` —— 1/5 个有
- `QwenEditListExtractor` —— 1/5 个有
- `RBGImageStitchPlus` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta57 | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta57，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
