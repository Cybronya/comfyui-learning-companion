---
name: text_to_image_controlnet_inpaint_upscale_3
type: Text To Image
frequency: 2
level: weak
coverage: 0.9295
common_nodes: [ApplyInstantID, CLIPTextEncode, CR Batch Images From List, CR Text, CheckpointLoaderSimple, ColorMatch, ControlNetLoader, CropFaces, DetectFaces, EmptyLatentImage, FaceDetailer, ImageScaleBy, ImageUpscaleWithModel, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LoadImage, LoraLoaderModelOnly, MaskFastGrow, PreviewImage, SaveImage, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, VAEEncode, WarpFacesBack]
problems: []
missing: []
members: [图片生成/图生图/F1高清细节修复放大极致重绘_1920447051887214593.json, 图片生成/图生图/高清细节修复放大极致重绘_1914935568353165313.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_upscale_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/F1高清细节修复放大极致重绘_1920447051887214593.json、图片生成/图生图/高清细节修复放大极致重绘_1914935568353165313.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CR Batch Images From List`
- `CR Text`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetLoader`
- `CropFaces`
- `DetectFaces`
- `EmptyLatentImage`
- `FaceDetailer`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskFastGrow`
- `PreviewImage`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `WarpFacesBack`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 0.615 | - | 2 | 37% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.615，样本不足，未给区间，2 个样本，取值分散，一致性仅 37%
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
