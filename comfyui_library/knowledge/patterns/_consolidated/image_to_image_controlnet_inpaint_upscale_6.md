---
name: image_to_image_controlnet_inpaint_upscale_6
type: Image To Image
frequency: 3
level: strong
coverage: 0.831
common_nodes: [ApplyInstantID, BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, ControlNetLoader, CropFaces, DetectFaces, DualCLIPLoader, FaceParse(FaceParsing), FaceParsingModelLoader(FaceParsing), FaceParsingProcessorLoader(FaceParsing), FaceParsingResultsParser(FaceParsing), Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MaskComposite, MaskFastGrow, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, WarpFacesBack]
problems: []
missing: []
members: [图片生成/图生图/高清换脸+肤质提升+高级相似度_1911783224224481281.json, 图片生成/图生图/高清放大+肤质提升换脸_1900359526355300353.json, 平台全量/InstantID 换脸新技巧_1904132593380397058.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_upscale_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/高清换脸+肤质提升+高级相似度_1911783224224481281.json、图片生成/图生图/高清放大+肤质提升换脸_1900359526355300353.json、平台全量/InstantID 换脸新技巧_1904132593380397058.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyInstantID`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetLoader`
- `CropFaces`
- `DetectFaces`
- `DualCLIPLoader`
- `FaceParse(FaceParsing)`
- `FaceParsingModelLoader(FaceParsing)`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParsingResultsParser(FaceParsing)`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskComposite`
- `MaskFastGrow`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WarpFacesBack`

**可变部分**（部分 workflow 才有）：
- `GroundingDinoModelLoader (segment anything)` —— 2/3 个有
- `GroundingDinoSAMSegment (segment anything)` —— 2/3 个有
- `SAMModelLoader (segment anything)` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `Image Tiled` —— 1/3 个有
- `ImageConcanateOfUtils` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
