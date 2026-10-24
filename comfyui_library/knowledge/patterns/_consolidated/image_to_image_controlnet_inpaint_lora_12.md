---
name: image_to_image_controlnet_inpaint_lora_12
type: Image To Image
frequency: 3
level: strong
coverage: 0.931667
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, CropFaces, DetectFaces, Image Comparer (rgthree), InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LoadImage, LoraLoaderModelOnly, MaskComposite, MaskFastGrow, MaskPreview+, PreviewImage, SaveImage, SetLatentNoiseMask, VAEDecode, VAEEncode, WarpFacesBack, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/匹配脸型换脸_1904734671882911745.json, 图片生成/图生图/匹配脸型换脸高相似度_1919707477808713730.json, 图片生成/图生图/匹配脸型换脸（超高相似度）_1915317225706684417.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_12

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/匹配脸型换脸_1904734671882911745.json、图片生成/图生图/匹配脸型换脸高相似度_1919707477808713730.json、图片生成/图生图/匹配脸型换脸（超高相似度）_1915317225706684417.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
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
- `CropFace` —— 2/3 个有
- `GetImageSize+` —— 2/3 个有
- `ImageCompositeMasked` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `LayerUtility: ColorImage` —— 2/3 个有
- `SplitImageWithAlpha` —— 2/3 个有
- `easy imageRemBg` —— 2/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.8 | 0.8 - 0.8 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
