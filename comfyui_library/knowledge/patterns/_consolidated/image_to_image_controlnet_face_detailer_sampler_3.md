---
name: image_to_image_controlnet_face_detailer_sampler_3
type: Image To Image
frequency: 2
level: weak
coverage: 0.7155
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, FaceDetailer, GetNode, Image Comparer (rgthree), Image Filter Adjustments, ImageColorMatch+, ImageScaleBy, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: PersonMaskUltra V2, LoadImage, PreviewImage, RHHiddenNodes, SetNode, UltralyticsDetectorProvider, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/换脸-高质量_2004142400413048834.json, 图片生成/图生图/超像换脸_1988251560230699009.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_face_detailer_sampler_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/换脸-高质量_2004142400413048834.json、图片生成/图生图/超像换脸_1988251560230699009.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `FaceDetailer`
- `GetNode`
- `Image Comparer (rgthree)`
- `Image Filter Adjustments`
- `ImageColorMatch+`
- `ImageScaleBy`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `SetNode`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CR Image Border` —— 1/2 个有
- `CR Overlay Text` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `DZ_Face_Detailer` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SaveImagePlus` —— 1/2 个有
- `ZML_ColorPicker` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_sde_gpu | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.2 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde_gpu，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
