---
name: image_to_image_controlnet_inpaint_lora_10
type: Image To Image
frequency: 4
level: moderate
coverage: 0.915
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, CropFaces, DetectFaces, Image Comparer (rgthree), InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LoadImage, LoraLoaderModelOnly, MaskComposite, MaskFastGrow, MaskPreview+, PreviewImage, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode, WarpFacesBack, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/匹配脸型换脸_1904734671882911745.json, 图片生成/图生图/匹配脸型换脸高相似度_1919707477808713730.json, 图片生成/图生图/匹配脸型换脸（超高相似度）_1915317225706684417.json, 平台全量/换脸_1979129706039644161.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/匹配脸型换脸_1904734671882911745.json、图片生成/图生图/匹配脸型换脸高相似度_1919707477808713730.json、图片生成/图生图/匹配脸型换脸（超高相似度）_1915317225706684417.json、平台全量/换脸_1979129706039644161.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `CropFaces`
- `DetectFaces`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskComposite`
- `MaskFastGrow`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `VAEDecode`
- `VAEEncode`
- `WarpFacesBack`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 3/4 个有
- `CropFace` —— 2/4 个有
- `GetImageSize+` —— 2/4 个有
- `ImageCompositeMasked` —— 2/4 个有
- `LayerUtility: ColorImage` —— 2/4 个有
- `SplitImageWithAlpha` —— 2/4 个有
- `easy imageRemBg` —— 2/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 25 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 0.8 | 0.5 - 0.8 | 4 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 25，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 0.8，观测区间 0.5 - 0.8，4 个样本，取值集中（一致性 82%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
