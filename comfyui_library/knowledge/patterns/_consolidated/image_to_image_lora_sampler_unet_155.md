---
name: image_to_image_lora_sampler_unet_155
type: Image To Image
frequency: 5
level: strong
coverage: 0.8416
common_nodes: [CLIPLoader, CannyEdgePreprocessor, ConditioningZeroOut, DepthAnythingPreprocessor, Flux2KleinEditTextEncode_EditUtils, Image Comparer (rgthree), ImagePadForOutpaint, ImageScaleToTotalPixels, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskPreview+, OpenposePreprocessor, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键产品加背景Flux2-Klein9b_2022471499424210945.json, 图片生成/图生图/一键产品加背景Flux2Klein9b_2045169051529383937.json, 图片生成/图生图/加背景Flux2Klein9b，根据产品匹配场景_2045285134584254466.json, 平台全量/一键产品加背景 Flux2-Klein9b 白底产品换背景换场景_2022854738689134594.json, 平台全量/白底产品换场景 换背景 一键产品加背景 Flux2-Klein9b_2022590881399836673.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_155

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一键产品加背景Flux2-Klein9b_2022471499424210945.json、图片生成/图生图/一键产品加背景Flux2Klein9b_2045169051529383937.json、图片生成/图生图/加背景Flux2Klein9b，根据产品匹配场景_2045285134584254466.json、平台全量/一键产品加背景 Flux2-Klein9b 白底产品换背景换场景_2022854738689134594.json、平台全量/白底产品换场景 换背景 一键产品加背景 Flux2-Klein9b_2022590881399836673.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CannyEdgePreprocessor`
- `ConditioningZeroOut`
- `DepthAnythingPreprocessor`
- `Flux2KleinEditTextEncode_EditUtils`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `OpenposePreprocessor`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/5 个有
- `ReferenceLatent` —— 3/5 个有
- `CFGNorm` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | dpmpp_2s_ancestral | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2s_ancestral，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
