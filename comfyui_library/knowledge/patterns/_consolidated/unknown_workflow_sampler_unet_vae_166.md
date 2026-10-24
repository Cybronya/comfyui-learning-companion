---
name: unknown_workflow_sampler_unet_vae_166
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.862167
common_nodes: [CLIPLoader, CR Text, ConditioningZeroOut, CropWithPadInfo, Image Comparer (rgthree), KSampler, LoadImage, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-Edit-2511图像编辑不偏移+万物移除-增加物体 V1.0_2008472523880538113.json, 图片生成/图生图/单图编辑背景无偏移_2008730411949625346.json, 图片生成/图生图/口述改图 零偏移 无偏移 0偏移  Qwen Edit 2511_2013903660815749122.json, 图片生成/图生图/高斯泼溅任意角度编辑 林耀_2013640884365037570.json, 图片生成/文生图/Qwen Edit 2511小志版0漂移_2073296578672160769.json, 图片生成/文生图/高斯泼溅任意角度编辑_2073302227107803137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_166

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-image-Edit-2511图像编辑不偏移+万物移除-增加物体 V1.0_2008472523880538113.json、图片生成/图生图/单图编辑背景无偏移_2008730411949625346.json、图片生成/图生图/口述改图 零偏移 无偏移 0偏移  Qwen Edit 2511_2013903660815749122.json、图片生成/图生图/高斯泼溅任意角度编辑 林耀_2013640884365037570.json、图片生成/文生图/Qwen Edit 2511小志版0漂移_2073296578672160769.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `LoadSharpModel` —— 2/6 个有
- `PreviewAny` —— 2/6 个有
- `SharpPredict` —— 2/6 个有
- `YCGaussianPreview` —— 2/6 个有
- `EasyCache` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `Power Lora Loader (rgthree)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | beta57 | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 beta57，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
