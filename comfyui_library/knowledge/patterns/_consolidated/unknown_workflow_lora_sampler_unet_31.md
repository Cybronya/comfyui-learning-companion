---
name: unknown_workflow_lora_sampler_unet_31
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM]
members: [图片生成/图生图/2092956995065307137.json, 图片生成/图生图/2093635203448270849.json, 图片生成/文生图/Qwen Edit 2511多角度视角控制_2073300184922148866.json, 图片生成/文生图/Qwen Edit 2511小志版0漂移_2073296578672160769.json, 图片生成/文生图/高斯泼溅任意角度编辑_2073302227107803137.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_31

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2092956995065307137.json、图片生成/图生图/2093635203448270849.json、图片生成/文生图/Qwen Edit 2511多角度视角控制_2073300184922148866.json、图片生成/文生图/Qwen Edit 2511小志版0漂移_2073296578672160769.json、图片生成/文生图/高斯泼溅任意角度编辑_2073302227107803137.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 3/5 个有
- `QwenEditAdaptiveLongestEdge` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `LoadSharpModel` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `QwenMultiangleCameraNode` —— 1/5 个有
- `SharpPredict` —— 1/5 个有
- `YCGaussianPreview` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta57 | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta57，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM
