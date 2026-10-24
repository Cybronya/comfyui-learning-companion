---
name: unknown_workflow_lora_sampler_unet_286
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.888
common_nodes: [CFGNorm, CLIPLoader, CR Prompt Text, ConditioningZeroOut, Fast Groups Bypasser (rgthree), KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RH_Nano_Banana2_Image2Image, RH_RhartImageG2OfficialImageToImage, SaveImage, TextEncodeQwenImageEditPlusPro_lrzjason, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/定点图像编辑（5号流）(1)_2057708772252016642.json, 图片生成/文生图/KR08_买家秀生成（8号流）科然拼好课-管波_2063938295737966593.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_286

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/定点图像编辑（5号流）(1)_2057708772252016642.json、图片生成/文生图/KR08_买家秀生成（8号流）科然拼好课-管波_2063938295737966593.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RH_Nano_Banana2_Image2Image`
- `RH_RhartImageG2OfficialImageToImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PromptBatchQueue` —— 1/2 个有
- `RH_Captioner_Pro` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `TextConcatenate` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
