---
name: unknown_workflow_lora_sampler_unet_196
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.797
common_nodes: [Any Switch (rgthree), Anything Everywhere3, CLIPLoader, CR SDXL Aspect Ratio, ConditioningZeroOut, CropWithPadInfo, EmptyLatentImage, Fast Groups Muter (rgthree), FluxKontextImageScale, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed-Image-Edit——支持多图编辑_2026634164103028738.json, 图片生成/图生图/Jojo—qwen_image_dit_2511-单图、双图、三图自定义工作流_2003723593496338433.json, 图片生成/图生图/Qwen_image_edit_2511-单图、双图、三图自定义工作流（优化版）_2004164393304760321.json, 平台全量/平替 全能图像2.0  一致性图像融合+多图编辑+指定修图 FireRed-Image-Edit_2028273951922720769.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_196

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FireRed-Image-Edit——支持多图编辑_2026634164103028738.json、图片生成/图生图/Jojo—qwen_image_dit_2511-单图、双图、三图自定义工作流_2003723593496338433.json、图片生成/图生图/Qwen_image_edit_2511-单图、双图、三图自定义工作流（优化版）_2004164393304760321.json、平台全量/平替 全能图像2.0  一致性图像融合+多图编辑+指定修图 FireRed-Image-Edit_2028273951922720769.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Anything Everywhere3`
- `CLIPLoader`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `FluxKontextImageScale`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `easy int`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 2/4 个有
- `LayerUtility: ImageReel` —— 2/4 个有
- `LayerUtility: ImageReelComposit` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| 采样步数 | 8 | 8 - 10 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 4 | 65% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 10，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
