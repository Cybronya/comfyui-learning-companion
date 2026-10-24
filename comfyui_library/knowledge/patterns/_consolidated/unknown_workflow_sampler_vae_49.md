---
name: unknown_workflow_sampler_vae_49
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.818
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, ImageScaleBy, KSampler, LoadImage, PreviewAny, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2509线稿转效果图_2013203241940553730.json, 图片生成/图生图/qwen_edit_2511_batch漫剧_视频分镜多宫格_2026894835206066177.json, 图片生成/图生图/qwen_edit_2511_mulity_angle 角度转换_人物一致性_2026894851593211905.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_49

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen2509线稿转效果图_2013203241940553730.json、图片生成/图生图/qwen_edit_2511_batch漫剧_视频分镜多宫格_2026894835206066177.json、图片生成/图生图/qwen_edit_2511_mulity_angle 角度转换_人物一致性_2026894851593211905.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `ImageScaleBy`
- `KSampler`
- `LoadImage`
- `PreviewAny`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `CombinationText` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `NunchakuQwenImageDiTLoader` —— 1/3 个有
- `QwenMultiangleCameraNode` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `StringFunction|pysssss` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy promptList` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
