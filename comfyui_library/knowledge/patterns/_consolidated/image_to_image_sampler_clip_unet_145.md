---
name: image_to_image_sampler_clip_unet_145
type: Image To Image
frequency: 4
level: strong
coverage: 0.875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein-9b图像编辑工作流_2022269747924049922.json, 图片生成/图生图/Flux2-klein-9b 人物换装_2015968151225245698.json, 图片生成/图生图/Flux2-klein-9b 局部重绘-万物迁移_2015984171918827522.json, 平台全量/flux klein多合一全能编辑工作流-局部重绘、万物迁移、多图编辑、扩图等_2013986790549495810.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_145

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein-9b图像编辑工作流_2022269747924049922.json、图片生成/图生图/Flux2-klein-9b 人物换装_2015968151225245698.json、图片生成/图生图/Flux2-klein-9b 局部重绘-万物迁移_2015984171918827522.json、平台全量/flux klein多合一全能编辑工作流-局部重绘、万物迁移、多图编辑、扩图等_2013986790549495810.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Anything Everywhere` —— 2/4 个有
- `GrowMaskWithBlur` —— 2/4 个有
- `ImageCompositeMasked` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `LayerMask: MaskPreview` —— 2/4 个有
- `Mask Fill Holes` —— 2/4 个有
- `Mask To Image (mtb)` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ColorMatch` —— 1/4 个有
- `DualCLIPLoader` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Float` —— 1/4 个有
- `FluxGuidance` —— 1/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `FluxResolutionNode` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageListToImageBatch` —— 1/4 个有
- `ImagePadForOutpaint` —— 1/4 个有
- `InvertMask` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `TTP_Image_Assy` —— 1/4 个有
- `TTP_Image_Tile_Batch` —— 1/4 个有
- `TTP_Tile_image_size` —— 1/4 个有
- `easy imageBatchToImageList` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
