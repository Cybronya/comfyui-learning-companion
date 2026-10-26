---
name: unknown_workflow_lora_sampler_unet_194
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9125
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/即梦一键去水印工作流_2013106532182925314.json, 图片生成/图生图/去豆包水印（保持原图不变）_2011639686401363969.json, 图片生成/图生图/移除即梦水印单图版（保持原图不变）_2010907294711681026.json, 图片生成/文生图/Qwen Edit 2511小志版——解决像素偏移（自己控制输出尺寸）_2029197668701970433.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_194

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/即梦一键去水印工作流_2013106532182925314.json、图片生成/图生图/去豆包水印（保持原图不变）_2011639686401363969.json、图片生成/图生图/移除即梦水印单图版（保持原图不变）_2010907294711681026.json、图片生成/文生图/Qwen Edit 2511小志版——解决像素偏移（自己控制输出尺寸）_2029197668701970433.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `Image Comparer (rgthree)`
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
- `GrowMaskWithBlur` —— 3/4 个有
- `ImageCompositeMasked` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `LayerUtility: ImageMaskScaleAs` —— 3/4 个有
- `MaskPreview+` —— 3/4 个有
- `CR Text` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
