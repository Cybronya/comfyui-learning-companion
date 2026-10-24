---
name: unknown_workflow_lora_sampler_unet_40
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.904583
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2511 单图编辑_2003992185257246722.json, 图片生成/图生图/Qwen Edit 2511多角度视角控制_2011041597944766465.json, 图片生成/图生图/Qwen Edit 2511多角度视角控制_2011327150468632577.json, 图片生成/图生图/Qwen Edit 2511多角度视角控制camera多角度控制人物多角度快速生成_2011788170161037314.json, 图片生成/图生图/Qwen Image Edit 2511 图生图_2053690401625784322.json, 图片生成/图生图/Qwen Image Edit2509二维动漫变真实照片_1991121748395425794.json, 图片生成/图生图/Qwen-Image-Edit-2511图像编辑_1988633859002646530.json, 图片生成/图生图/Qwen2509平面图像转真实_1989667494489149441.json, 图片生成/图生图/QwenEdit2509任意风格转写实_1990057267645042689.json, 图片生成/图生图/QwenEdit2509去除光斑_过曝_欠曝修复_1990309519743963137.json, 图片生成/图生图/QwenEdit2509重新打光_1990321830420508673.json, 图片生成/图生图/qwen2511人物换装（增强服装一致性，自动蒙版）V2_2005472336822366209.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_40

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2511 单图编辑_2003992185257246722.json、图片生成/图生图/Qwen Edit 2511多角度视角控制_2011041597944766465.json、图片生成/图生图/Qwen Edit 2511多角度视角控制_2011327150468632577.json、图片生成/图生图/Qwen Edit 2511多角度视角控制camera多角度控制人物多角度快速生成_2011788170161037314.json、图片生成/图生图/Qwen Image Edit 2511 图生图_2053690401625784322.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenEditOutputExtractor` —— 10/12 个有
- `Image Comparer (rgthree)` —— 9/12 个有
- `CropWithPadInfo` —— 8/12 个有
- `CFGNorm` —— 5/12 个有
- `ImageScaleBy` —— 5/12 个有
- `ModelSamplingAuraFlow` —— 5/12 个有
- `LayerUtility: ImageReel` —— 4/12 个有
- `LayerUtility: ImageReelComposit` —— 4/12 个有
- `PreviewImage` —— 4/12 个有
- `QwenMultiangleCameraNode` —— 3/12 个有
- `Text Multiline` —— 3/12 个有
- `easy showAnything` —— 3/12 个有
- `ImageScaleToTotalPixels` —— 2/12 个有
- `PrimitiveStringMultiline` —— 2/12 个有
- `ClothesSegment` —— 1/12 个有
- `EmptySD3LatentImage` —— 1/12 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/12 个有
- `GrowMask` —— 1/12 个有
- `ImageStitch` —— 1/12 个有
- `MaskToImage` —— 1/12 个有
- `ReferenceLatent` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 12 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | beta57 | - | 12 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 beta57，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（15/12 个样本）：Steps较低可能导致细节不足
