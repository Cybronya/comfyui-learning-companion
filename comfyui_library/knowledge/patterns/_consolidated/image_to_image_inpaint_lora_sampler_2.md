---
name: image_to_image_inpaint_lora_sampler_2
type: Image To Image
frequency: 5
level: strong
coverage: 0.9108
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, Get resolution [Crystools], GrowMaskWithBlur, INPAINT_MaskedBlur, INPAINT_MaskedFill, Image Comparer (rgthree), ImageCropByMaskAndResize, ImageScale, ImageToMask, ImageUncropByMask, JoinStrings, KSampler, LayerMask: MaskPreview, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, StringConstantMultiline, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/局部重绘Qwen edit 优化版_2084263071580778498.json, 图片生成/图生图/局部重绘Qwen edit 优化版_2099726381256101890.json, 图片生成/图生图/局部重绘Qwen_edit_优化版_2100396043715309569.json, 图片生成/图生图/局部重绘Qwen_edit_优化版_2100486266654650369.json, 图片生成/图生图/局部重绘Qwen_edit_优化版_2110205341303656449.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/局部重绘Qwen edit 优化版_2084263071580778498.json、图片生成/图生图/局部重绘Qwen edit 优化版_2099726381256101890.json、图片生成/图生图/局部重绘Qwen_edit_优化版_2100396043715309569.json、图片生成/图生图/局部重绘Qwen_edit_优化版_2100486266654650369.json、图片生成/图生图/局部重绘Qwen_edit_优化版_2110205341303656449.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `Get resolution [Crystools]`
- `GrowMaskWithBlur`
- `INPAINT_MaskedBlur`
- `INPAINT_MaskedFill`
- `Image Comparer (rgthree)`
- `ImageCropByMaskAndResize`
- `ImageScale`
- `ImageToMask`
- `ImageUncropByMask`
- `JoinStrings`
- `KSampler`
- `LayerMask: MaskPreview`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `StringConstantMultiline`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageCompositeMasked` —— 4/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 8 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 8，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
