---
name: image_to_image_inpaint_sampler_clip_4
type: Image To Image
frequency: 4
level: strong
coverage: 0.90725
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, DifferentialDiffusion, INPAINT_ExpandMask, ImageCompositeMasked, ImageResizeKJv2, InpaintModelConditioning, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX2-Klein局部重绘（参考图）_2042643462075453441.json, 图片生成/图生图/Klein-m2i_2080076136222117890.json, 图片生成/图生图/flux-2-klein全家桶系列-3（ 内补式-局部重绘）_2042479068276334593.json, 图片生成/图生图/▶flux-2-klein-局部重绘流_2017054515127652354.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX2-Klein局部重绘（参考图）_2042643462075453441.json、图片生成/图生图/Klein-m2i_2080076136222117890.json、图片生成/图生图/flux-2-klein全家桶系列-3（ 内补式-局部重绘）_2042479068276334593.json、图片生成/图生图/▶flux-2-klein-局部重绘流_2017054515127652354.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `INPAINT_ExpandMask`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `ImageAndMaskPreview` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `MaskFillHoles` —— 2/4 个有
- `PlaySound|pysssss` —— 2/4 个有
- `CLIPLoaderGGUF` —— 1/4 个有
- `DrawMaskOnImage` —— 1/4 个有
- `EasySizeSimpleImage` —— 1/4 个有
- `EmptyFlux2LatentImage` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `MemoryCleaner` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有
- `Text` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `easy imageSizeBySide` —— 1/4 个有
- `图像缩放V2_孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 4 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
