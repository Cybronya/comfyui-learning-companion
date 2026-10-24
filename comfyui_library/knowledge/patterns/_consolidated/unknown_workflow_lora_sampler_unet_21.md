---
name: unknown_workflow_lora_sampler_unet_21
type: Unknown Workflow
frequency: 19
level: strong
coverage: 0.952368
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2511_2112493435893673986.json, 图片生成/图生图/qwen2511之开源最强换装-人工智能张老师_2093716710770700289.json, 图片生成/图生图/qwen2511之开源最强换装_2045516546491031553.json, 图片生成/图生图/qwen2511之开源最强换装_2056968344452030465.json, 图片生成/图生图/qwen2511之开源最强换装_2092418470146297857.json, 图片生成/图生图/qwen2511之开源最强换装_2092490595444023297.json, 图片生成/图生图/qwen2511之开源最强换装_2094718768906854401.json, 图片生成/图生图/qwen2511之开源最强换装_2097203246325653505.json, 图片生成/图生图/qwen2511之开源最强换装_2098945002738114561.json, 图片生成/图生图/qwen2511之开源最强换装_2112368004746010625.json, 图片生成/图生图/qwen2511图片编辑工作流_2061628984315703298.json, 图片生成/图生图/qwen2511开源最强换装 一键快速出图_2092915833847771137.json, 图片生成/图生图/qwen2511开源最强换装 一键快速出图_2092956995065307137.json, 图片生成/图生图/一致性人物换装从头到脚一键换装_2071441629101248514.json, 图片生成/图生图/一键换装_2054723475348172802.json, 图片生成/图生图/一键换装_完美替换衣物_超高一致性保持_2068338454383124482.json, 图片生成/图生图/一键换装完美替换衣物，超高一致性保持【帽子可选】_2066855682535682049.json, 图片生成/图生图/一键换装：完美替换衣物，超高一致性保持。_2028771700019568642.json, 图片生成/图生图/内裤换装_2049129061464678401.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/qwen2511_2112493435893673986.json、图片生成/图生图/qwen2511之开源最强换装-人工智能张老师_2093716710770700289.json、图片生成/图生图/qwen2511之开源最强换装_2045516546491031553.json、图片生成/图生图/qwen2511之开源最强换装_2056968344452030465.json、图片生成/图生图/qwen2511之开源最强换装_2092418470146297857.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 13/19 个有
- `PrimitiveStringMultiline` —— 7/19 个有
- `Image Comparer (rgthree)` —— 6/19 个有
- `PreviewImage` —— 5/19 个有
- `ImageStitch` —— 3/19 个有
- `Int` —— 2/19 个有
- `TT_img_enc` —— 2/19 个有
- `CR Text` —— 1/19 个有
- `EmptyImage` —— 1/19 个有
- `INTConstant` —— 1/19 个有
- `ImpactSwitch` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | beta57 | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 beta57，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：Steps较低可能导致细节不足
