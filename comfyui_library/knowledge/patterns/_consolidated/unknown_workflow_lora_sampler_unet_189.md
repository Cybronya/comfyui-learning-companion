---
name: unknown_workflow_lora_sampler_unet_189
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9625
common_nodes: [CLIPLoader, ConditioningZeroOut, EmptySD3LatentImage, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一句话改图_2083780142928846850.json, 图片生成/图生图/动态姿势_2083204997793271810.json, 图片生成/图生图/扩图_2083084702419873793.json, 图片生成/图生图/扩图_2083175757135826945.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_189

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一句话改图_2083780142928846850.json、图片生成/图生图/动态姿势_2083204997793271810.json、图片生成/图生图/扩图_2083084702419873793.json、图片生成/图生图/扩图_2083175757135826945.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FlashVSR_SM_KSampler` —— 3/4 个有
- `FlashVSR_SM_Model` —— 3/4 个有
- `GetImageRangeFromBatch` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `easy imageSize` —— 3/4 个有
- `CFGNorm` —— 2/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `Qwen3VL_Chat` —— 2/4 个有
- `ZML_LimitImageAspect` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9.02565e+08 | 4 - 9.02565e+08 | 4 | 42% |
| Prompt 约束强度(CFG) | randomize | - | 4 | 75% |
| 采样算法 | 2 | 2 - 2 | 3 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 重绘幅度 | 11 | 1 - 11 | 4 | 49% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9.02565e+08，观测区间 4 - 9.02565e+08，4 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 最常用 randomize，4 个样本，一致性 75%
- 采样算法 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 1 - 11，4 个样本，取值分散，一致性仅 49%
- 风险：采样步数 观测到 9.02565e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
