---
key: 图片生成/图生图/超自然发型设计_Super Natural Hair Design_1921735094384410625.json
name: 超自然发型设计_Super Natural Hair Design_1921735094384410625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/超自然发型设计_Super Natural Hair Design_1921735094384410625.json
hash: b3e9f588c68977f0
coverage: 0.596491
learned_at: 2026-10-23 13:29:47
nodes: [PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, Fast Groups Bypasser (rgthree), LayerStyle: DropShadow, Masks Subtract, MaskToImage, MaskToImage, LayerUtility: ImageBlendAdvance, Convert Masks to Images, MaskToImage, PreviewImage, ToBasicPipe, PreviewImage, Convert Masks to Images, MaskToImage, IPAdapterFaceID, PerturbedAttentionGuidance, PreviewImage, PreviewImage, IPAdapterUnifiedLoaderFaceID, LayerMask: PersonMaskUltra V2, LayerMask: MaskEdgeUltraDetail V2, easy showAnything, easy showAnything, Note, Note, Note, PreviewImage, PreviewImage, Note, PatchModelAddDownscale, PreviewImage, Note, LayerMask: SegmentAnythingUltra V2, String Literal, LayerUtility: SimpleTextImage, MaskToSEGS, ToBinaryMask, ImpactDilateMask, LayerMask: PersonMaskUltra V2, GrowMask, SmoothMask, EmptyImage, JWImageResizeByLongerSide, String Literal, easy stylesSelector, CR Text Concatenate, Efficient Loader, PreviewImage, DetailerForEachPipe, JjkText, SaveImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/超自然发型设计_Super Natural Hair Design_1921735094384410625.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/超自然发型设计_Super Natural Hair Design_1921735094384410625.json`

## 结构

**生成流程**：Model → Control → Process → Output → Other

**节点**（57 个）：
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `LayerStyle: DropShadow`
- `Masks Subtract`
- `MaskToImage`
- `MaskToImage`
- `LayerUtility: ImageBlendAdvance`
- `Convert Masks to Images`
- `MaskToImage`
- `PreviewImage`
- `ToBasicPipe`
- `PreviewImage`
- `Convert Masks to Images`
- `MaskToImage`
- `IPAdapterFaceID`
- `PerturbedAttentionGuidance`
- `PreviewImage`
- `PreviewImage`
- `IPAdapterUnifiedLoaderFaceID`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: MaskEdgeUltraDetail V2`
- `easy showAnything`
- `easy showAnything`
- `Note`
- `Note`
- `Note`
- `PreviewImage`
- `PreviewImage`
- `Note`
- `PatchModelAddDownscale`
- `PreviewImage`
- `Note`
- `LayerMask: SegmentAnythingUltra V2`
- `String Literal`
- `LayerUtility: SimpleTextImage`
- `MaskToSEGS`
- `ToBinaryMask`
- `ImpactDilateMask`
- `LayerMask: PersonMaskUltra V2`
- `GrowMask`
- `SmoothMask`
- `EmptyImage`
- `JWImageResizeByLongerSide`
- `String Literal`
- `easy stylesSelector`
- `CR Text Concatenate`
- `Efficient Loader`
- `PreviewImage`
- `DetailerForEachPipe`
- `JjkText`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **60%**（34/57）

**有卡**：`LayerStyle: DropShadow`、`Masks Subtract`、`MaskToImage`、`LayerUtility: ImageBlendAdvance`、`Convert Masks to Images`、`ToBasicPipe`、`IPAdapterFaceID`、`PerturbedAttentionGuidance`、`IPAdapterUnifiedLoaderFaceID`、`LayerMask: PersonMaskUltra V2`、`LayerMask: MaskEdgeUltraDetail V2`、`PatchModelAddDownscale`、`LayerMask: SegmentAnythingUltra V2`、`String Literal`、`LayerUtility: SimpleTextImage`、`MaskToSEGS`、`ToBinaryMask`、`ImpactDilateMask`、`GrowMask`、`SmoothMask`、`EmptyImage`、`JWImageResizeByLongerSide`、`easy stylesSelector`、`CR Text Concatenate`、`Efficient Loader`、`DetailerForEachPipe`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、PerturbedAttentionGuidance、easy stylesSelector、LayerStyle: DropShadow、IPAdapterFaceID、IPAdapterUnifiedLoaderFaceID、JWImageResizeByLongerSide、SaveImage
