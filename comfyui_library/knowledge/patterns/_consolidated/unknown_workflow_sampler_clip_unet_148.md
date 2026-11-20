---
name: unknown_workflow_sampler_clip_unet_148
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.773333
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, PrimitiveStringMultiline, ReferenceMultiLatent, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX 3 Image Klein 图像编辑_2111121518007767042.json, 图片生成/图生图/FLUX 3 Klein 图生图 6图参考_2115366986241892354.json, 图片生成/图生图/Flux3 Image Klein distill t2i加速图生图_2110971174585978882.json, 图片生成/图生图/Flux3 Klein 图生图局部编辑标准版_2113475197054570497.json, 图片生成/图生图/Flux3_klein_图像编辑_2111983712979210242.json, 图片生成/图生图/flux3_image_klein多图编辑_2111134357867028482.json, 图片生成/文生图/flux3_image_klein多图编辑_2011011965199589378.json, 平台全量/FLUX3 Klein_IMAGE_EDIT 图像编辑工作流_2117237762117165058.json, 平台全量/Flux3 Klein-像素_色彩修复_图片精准编辑_2117839203160641538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_148

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FLUX 3 Image Klein 图像编辑_2111121518007767042.json、图片生成/图生图/FLUX 3 Klein 图生图 6图参考_2115366986241892354.json、图片生成/图生图/Flux3 Image Klein distill t2i加速图生图_2110971174585978882.json、图片生成/图生图/Flux3 Klein 图生图局部编辑标准版_2113475197054570497.json、图片生成/图生图/Flux3_klein_图像编辑_2111983712979210242.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ReferenceMultiLatent`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 8/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `EmptyFlux2LatentImage` —— 6/9 个有
- `PreviewAny` —— 6/9 个有
- `ComfySwitchNode` —— 5/9 个有
- `CreateBoundingBoxes` —— 3/9 个有
- `Flux3LayoutPrompt` —— 3/9 个有
- `Image Comparer (rgthree)` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `ImageCompare` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `PrimitiveBoolean` —— 2/9 个有
- `EasyBatchImages` —— 1/9 个有
- `EasyLoadImage` —— 1/9 个有
- `GetImageSize` —— 1/9 个有
- `KleinEditComposite` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `ResizeImageMaskNode` —— 1/9 个有
- `ResolutionSelector` —— 1/9 个有
- `easy seed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | 16 - 50 | 9 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.2 | 9 | 94% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 0.97 - 1 | 9 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16，观测区间 16 - 50，9 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.2，9 个样本，取值集中（一致性 94%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.97 - 1，9 个样本，取值集中（一致性 99%）
