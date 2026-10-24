---
name: unknown_workflow_lora_sampler_unet_111
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.868667
common_nodes: [CFGNorm, CLIPLoader, CR Text, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, GetImageSize, ImageConcanate, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, QwenEditConfigPreparer, QwenEditOutputExtractor, RH_Captioner, SaveImage, Text Concatenate, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit2511+姿势Lora  更稳定迁移_2008486705380204546.json, 图片生成/图生图/Qwen-Edit2511+姿势Lora  更稳定迁移_2008753878052904961.json, 图片生成/图生图/Qwen-Image-Edit2511+Lora姿势迁移_2007684850882449409.json, 图片生成/图生图/Qwen-Image-Edit2511+姿势Lora，更稳定迁移_2007272179959865345.json, 图片生成/图生图/Qwent2511 姿势稳定迁移_2008020776473071618.json, 图片生成/图生图/优秀的姿势模仿自动提示词Qwen-Image-Edit2511+AnyPose Lora_2007843959200030721.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_111

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit2511+姿势Lora  更稳定迁移_2008486705380204546.json、图片生成/图生图/Qwen-Edit2511+姿势Lora  更稳定迁移_2008753878052904961.json、图片生成/图生图/Qwen-Image-Edit2511+Lora姿势迁移_2007684850882449409.json、图片生成/图生图/Qwen-Image-Edit2511+姿势Lora，更稳定迁移_2007272179959865345.json、图片生成/图生图/Qwent2511 姿势稳定迁移_2008020776473071618.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSize`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `RH_Captioner`
- `SaveImage`
- `Text Concatenate`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactMinMax` —— 5/6 个有
- `QwenVisionNode` —— 5/6 个有
- `AddLabel` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `MaxNode` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `SetNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 6 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
