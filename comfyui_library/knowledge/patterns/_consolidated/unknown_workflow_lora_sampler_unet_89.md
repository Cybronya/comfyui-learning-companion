---
name: unknown_workflow_lora_sampler_unet_89
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.803125
common_nodes: [CLIPLoader, ConditioningZeroOut, ImageScaleBy, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2509图像编辑 浮云2.3_2018594385880944642.json, 图片生成/图生图/Qwen Edit 2511 单图、双图、三图 编辑_2017210536177438721.json, 图片生成/图生图/Qwen Edit 2511图像编辑V1-单图编辑_2003668776639995905.json, 图片生成/图生图/Qwen Edit 2511图像编辑V2（一致性加强版）_2003550580272447490.json, 图片生成/图生图/Qwen Edit 2511图像编辑_2003784726580240385.json, 图片生成/图生图/Qwen Edit 2511多图像编辑（一致性加强版）_2003696893463019521.json, 图片生成/图生图/Qwen+Edit+2511图像编辑V1-单图编辑_2003717023706300417.json, 图片生成/图生图/【新版】动漫转真人_1988926427942760450.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_89

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2509图像编辑 浮云2.3_2018594385880944642.json、图片生成/图生图/Qwen Edit 2511 单图、双图、三图 编辑_2017210536177438721.json、图片生成/图生图/Qwen Edit 2511图像编辑V1-单图编辑_2003668776639995905.json、图片生成/图生图/Qwen Edit 2511图像编辑V2（一致性加强版）_2003550580272447490.json、图片生成/图生图/Qwen Edit 2511图像编辑_2003784726580240385.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CropWithPadInfo` —— 7/8 个有
- `PreviewAny` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `PrimitiveStringMultiline` —— 7/8 个有
- `QwenEditOutputExtractor` —— 7/8 个有
- `ImageConcanate` —— 6/8 个有
- `CR Prompt Text` —— 2/8 个有
- `EmptyLatentImage` —— 2/8 个有
- `easy imageConcat` —— 2/8 个有
- `FluxResolutionNode` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `ImpactSwitch` —— 1/8 个有
- `TextEncodeQwenImageEditPlus` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | beta57 | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 1108 | - | 2 | 46% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 beta57，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 1108，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- 高发问题（10/8 个样本）：Steps较低可能导致细节不足
