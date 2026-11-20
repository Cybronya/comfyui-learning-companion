---
name: unknown_workflow_lora_sampler_unet_349
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9145
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, DWPreprocessor, EmptySD3LatentImage, GetImageSize, Image Comparer (rgthree), ImageScale, ImageScaleToTotalPixels, KSampler (Efficient), LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/千问Edit 2511 图像编辑_2012166386520428546.json, 平台全量/2511相机转角度_2011257251520061442.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_349

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/千问Edit 2511 图像编辑_2012166386520428546.json、平台全量/2511相机转角度_2011257251520061442.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `EmptySD3LatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `KSampler (Efficient)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LayerUtility: ExtendCanvasV2` —— 1/2 个有
- `QwenMultiangleCameraNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5.5 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 5.5，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
