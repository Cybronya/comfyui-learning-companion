---
name: unknown_workflow_lora_sampler_unet_216
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.509333
common_nodes: [CFGNorm, CLIPLoader, CR Text, ConditioningZeroOut, CropWithPadInfo, GetNode, Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, SetNode, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【111】Qwen image edit 2511图像编辑_2004815399067811841.json, 图片生成/图生图/【113】Qwen edit 2511图像编辑+CN控制【产品换背景】_2008359301148053506.json, 图片生成/图生图/【113】Qwen edit 2511图像编辑+CN控制【人物换装】_2009606071433830402.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_216

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【111】Qwen image edit 2511图像编辑_2004815399067811841.json、图片生成/图生图/【113】Qwen edit 2511图像编辑+CN控制【产品换背景】_2008359301148053506.json、图片生成/图生图/【113】Qwen edit 2511图像编辑+CN控制【人物换装】_2009606071433830402.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：51%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CR Image Input Switch (4 way)` —— 2/3 个有
- `CannyEdgePreprocessor` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `DepthAnythingV2Preprocessor` —— 2/3 个有
- `OpenposePreprocessor` —— 2/3 个有
- `SetUnionControlNetType` —— 2/3 个有
- `easy imagePixelPerfect` —— 2/3 个有
- `GGUFLoaderKJ` —— 1/3 个有
- `ImageAndMaskPreview` —— 1/3 个有
- `NunchakuQwenImageDiTLoader` —— 1/3 个有
- `NunchakuQwenImageLoraLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.2 | - | 1 | 100% |
| LoRA 文本强度 | disable | - | 1 | 100% |
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
