---
key: 平台全量/Hunyuan3D 2.0 多视图模型生成材质纹理版_2069669394275454978.json
name: Hunyuan3D 2.0 多视图模型生成材质纹理版_2069669394275454978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Hunyuan3D 2.0 多视图模型生成材质纹理版_2069669394275454978.json
hash: d66855885a0225e7
coverage: 0.698795
learned_at: 2026-11-14 00:32:07
nodes: [PreviewImage, PreviewImage, Hy3DDiffusersSchedulerConfig, Reroute, Hy3DDiffusersSchedulerConfig, Reroute, Reroute, Reroute, Reroute, Reroute, JoinImageWithAlpha, JoinImageWithAlpha, JoinImageWithAlpha, JoinImageWithAlpha, Note, TransparentBGSession+, Reroute, Reroute, DownloadAndLoadHy3DDelightModel, ImageCompositeMasked, BatchCount+, MaskToImage, RepeatImageBatch, SolidMask, Hy3DDelightImage, Note, PreviewImage, PrimitiveNode, LoadImage, ImageRemoveBackground+, ImageResize+, MaskPreview+, InvertMask, ImageRemoveBackground+, MaskPreview+, InvertMask, MaskPreview+, InvertMask, ImageResize+, ImageRemoveBackground+, ImageResize+, ImageRemoveBackground+, MaskPreview+, InvertMask, MarkdownNote, Hy3DModelLoader, Note, Hy3DGenerateMeshMultiView, Hy3DExportMesh, Hy3DPostprocessMesh, Hy3DRenderSingleView, Hy3DVAEDecode, PreviewImage, MaskPreview+, Note, Preview3D, Hy3DMeshUVWrap, Note, Hy3DRenderMultiView, Hy3DCameraConfig, PreviewImage, PreviewImage, PreviewImage, UpscaleModelLoader, ImageResize+, PreviewImage, Hy3DMeshVerticeInpaintTexture, CV2InpaintTexture, Note, Hy3DApplyTexture, Preview3D, Hy3DExportMesh, Note, ImageResize+, EmptyImage, SaveImage, Hy3DBakeFromMultiview, ImageUpscaleWithModel, DownloadAndLoadHy3DPaintModel, Hy3DSampleMultiView, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/Hunyuan3D 2.0 多视图模型生成材质纹理版_2069669394275454978.json

> 来源文件 `comfyui_library/workflows/平台全量/Hunyuan3D 2.0 多视图模型生成材质纹理版_2069669394275454978.json`

## 结构

**生成流程**：Model → Decode → Process → Output → Other

**节点**（83 个）：
- `PreviewImage`
- `PreviewImage`
- `Hy3DDiffusersSchedulerConfig`
- `Reroute`
- `Hy3DDiffusersSchedulerConfig`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `JoinImageWithAlpha`
- `Note`
- `TransparentBGSession+`
- `Reroute`
- `Reroute`
- `DownloadAndLoadHy3DDelightModel`
- `ImageCompositeMasked`
- `BatchCount+`
- `MaskToImage`
- `RepeatImageBatch`
- `SolidMask`
- `Hy3DDelightImage`
- `Note`
- `PreviewImage`
- `PrimitiveNode`
- `LoadImage`
- `ImageRemoveBackground+`
- `ImageResize+`
- `MaskPreview+`
- `InvertMask`
- `ImageRemoveBackground+`
- `MaskPreview+`
- `InvertMask`
- `MaskPreview+`
- `InvertMask`
- `ImageResize+`
- `ImageRemoveBackground+`
- `ImageResize+`
- `ImageRemoveBackground+`
- `MaskPreview+`
- `InvertMask`
- `MarkdownNote`
- `Hy3DModelLoader`
- `Note`
- `Hy3DGenerateMeshMultiView`
- `Hy3DExportMesh`
- `Hy3DPostprocessMesh`
- `Hy3DRenderSingleView`
- `Hy3DVAEDecode` ★核心
- `PreviewImage`
- `MaskPreview+`
- `Note`
- `Preview3D`
- `Hy3DMeshUVWrap`
- `Note`
- `Hy3DRenderMultiView`
- `Hy3DCameraConfig`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `UpscaleModelLoader`
- `ImageResize+`
- `PreviewImage`
- `Hy3DMeshVerticeInpaintTexture`
- `CV2InpaintTexture`
- `Note`
- `Hy3DApplyTexture`
- `Preview3D`
- `Hy3DExportMesh`
- `Note`
- `ImageResize+`
- `EmptyImage`
- `SaveImage`
- `Hy3DBakeFromMultiview`
- `ImageUpscaleWithModel`
- `DownloadAndLoadHy3DPaintModel`
- `Hy3DSampleMultiView`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **70%**（58/83）

**有卡**：`Hy3DDiffusersSchedulerConfig`、`JoinImageWithAlpha`、`TransparentBGSession+`、`DownloadAndLoadHy3DDelightModel`、`ImageCompositeMasked`、`BatchCount+`、`MaskToImage`、`RepeatImageBatch`、`SolidMask`、`Hy3DDelightImage`、`LoadImage`、`ImageRemoveBackground+`、`ImageResize+`、`MaskPreview+`、`InvertMask`、`Hy3DModelLoader`、`Hy3DGenerateMeshMultiView`、`Hy3DExportMesh`、`Hy3DPostprocessMesh`、`Hy3DRenderSingleView`、`Hy3DVAEDecode`、`Preview3D`、`Hy3DMeshUVWrap`、`Hy3DRenderMultiView`、`Hy3DCameraConfig`、`UpscaleModelLoader`、`Hy3DMeshVerticeInpaintTexture`、`CV2InpaintTexture`、`Hy3DApplyTexture`、`EmptyImage`、`SaveImage`、`Hy3DBakeFromMultiview`、`ImageUpscaleWithModel`、`DownloadAndLoadHy3DPaintModel`、`Hy3DSampleMultiView`

**用到的条目**：LoadImage、Hy3DVAEDecode、ImageUpscaleWithModel、UpscaleModelLoader、ImageResize+、MaskPreview+、Preview3D、SaveImage
