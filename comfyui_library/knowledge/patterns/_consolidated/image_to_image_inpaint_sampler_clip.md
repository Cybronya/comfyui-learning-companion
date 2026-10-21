---
name: image_to_image_inpaint_sampler_clip
type: Image To Image
frequency: 4
level: strong
coverage: 0.6455
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, DownloadAndLoadFlorence2Model, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Florence2Run, Flux2Scheduler, GetImageSize, GrowMaskWithBlur, INTConstant, Image Comparer (rgthree), ImageScaleToTotalPixels, InpaintModelConditioning, JWStringConcat, KSampler, KSamplerSelect, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, PreviewImage, Qwen3_VQA, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, Text Multiline, CR Prompt Text, LayerMask: MaskPreview, easy promptLine]
members: [图片生成/图生图/2050427161806426114.json, 图片生成/图生图/2093305986097442818.json, 图片生成/文生图/FLUX-Klein超强分镜流 一致性超强九宫格_2052922333702180866.json, 图片生成/文生图/FLUX-Klein超强分镜流 一致性超强九宫格_2054763247810686977.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2050427161806426114.json、图片生成/图生图/2093305986097442818.json、图片生成/文生图/FLUX-Klein超强分镜流 一致性超强九宫格_2052922333702180866.json、图片生成/文生图/FLUX-Klein超强分镜流 一致性超强九宫格_2054763247810686977.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 4 个 workflow 都包含：
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
| 采样步数 | 6 | 6 - 6 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Text Multiline、CR Prompt Text、LayerMask: MaskPreview、easy promptLine
