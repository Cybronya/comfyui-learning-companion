---
name: unknown_workflow_lora_sampler_unet_137
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.915667
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, QwenEditConfigPreparer, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/即梦一键去水印工作流_2013106532182925314.json, 图片生成/图生图/去豆包水印（保持原图不变）_2011639686401363969.json, 图片生成/图生图/移除即梦水印单图版（保持原图不变）_2010907294711681026.json, 图片生成/文生图/Qwen Edit 2511小志版——解决像素偏移（自己控制输出尺寸）_2029197668701970433.json, 平台全量/Qwen Edit 2511小志版——解决像素偏移_2010537686016204802.json, 平台全量/qwen-edit-2509万物迁移2.0_1999420938271813633.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_137

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/即梦一键去水印工作流_2013106532182925314.json、图片生成/图生图/去豆包水印（保持原图不变）_2011639686401363969.json、图片生成/图生图/移除即梦水印单图版（保持原图不变）_2010907294711681026.json、图片生成/文生图/Qwen Edit 2511小志版——解决像素偏移（自己控制输出尺寸）_2029197668701970433.json、平台全量/Qwen Edit 2511小志版——解决像素偏移_2010537686016204802.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CropWithPadInfo` —— 5/6 个有
- `QwenEditOutputExtractor` —— 5/6 个有
- `ImageConcanate` —— 4/6 个有
- `CR Text` —— 3/6 个有
- `GrowMaskWithBlur` —— 3/6 个有
- `ImageCompositeMasked` —— 3/6 个有
- `LayerUtility: ImageMaskScaleAs` —— 3/6 个有
- `MaskPreview+` —— 3/6 个有
- `QwenEditAdaptiveLongestEdge` —— 2/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 6 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | beta57 | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 beta57，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
