---
name: image_to_image_inpaint_sampler_clip
type: Image To Image
frequency: 2
level: weak
coverage: 0.597
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, DownloadAndLoadFlorence2Model, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Florence2Run, Flux2Scheduler, GetImageSize, GrowMaskWithBlur, INTConstant, Image Comparer (rgthree), ImageScaleToTotalPixels, InpaintModelConditioning, JWStringConcat, KSampler, KSamplerSelect, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, PreviewImage, Qwen3_VQA, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Multiline, CR Prompt Text, LayerMask: MaskPreview, easy promptLine]
members: [图片生成/图生图/2050427161806426114.json, 图片生成/图生图/2093305986097442818.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2050427161806426114.json、图片生成/图生图/2093305986097442818.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `DownloadAndLoadFlorence2Model`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `Flux2Scheduler`
- `GetImageSize`
- `GrowMaskWithBlur`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `JWStringConcat`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `PreviewImage`
- `Qwen3_VQA`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Text Multiline、CR Prompt Text、LayerMask: MaskPreview、easy promptLine
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
