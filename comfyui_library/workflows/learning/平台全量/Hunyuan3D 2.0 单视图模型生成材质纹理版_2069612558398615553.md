---
key: 平台全量/Hunyuan3D 2.0 单视图模型生成材质纹理版_2069612558398615553.json
name: Hunyuan3D 2.0 单视图模型生成材质纹理版_2069612558398615553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Hunyuan3D 2.0 单视图模型生成材质纹理版_2069612558398615553.json
hash: b56608510f47c1c6
coverage: 0.641509
learned_at: 2026-11-14 00:32:06
nodes: [ImageCompositeMasked, UpscaleModelLoader, Hy3DApplyTexture, PreviewImage, ImageUpscaleWithModel, MaskToImage, Hy3DBakeFromMultiview, Hy3DMeshVerticeInpaintTexture, ImageResize+, DownloadAndLoadHy3DPaintModel, PrimitiveNode, Note, PreviewImage, PreviewImage, PreviewImage, Hy3DSampleMultiView, Hy3DDiffusersSchedulerConfig, Hy3DDiffusersSchedulerConfig, ImageResize+, Note, Note, Reroute, Reroute, Reroute, Reroute, DownloadAndLoadHy3DDelightModel, Hy3DDelightImage, SolidMask, Note, PreviewImage, Hy3DMeshUVWrap, Hy3DRenderMultiView, Hy3DCameraConfig, PreviewImage, PreviewImage, CV2InpaintTexture, Hy3DExportMesh, Preview3D, MaskPreview+, TransparentBGSession+, ImageRemoveBackground+, Hy3DGenerateMesh, Hy3DVAEDecode, Hy3DPostprocessMesh, Hy3DExportMesh, Preview3D, Note, Note, Note, Hy3DModelLoader, EmptyImage, SaveImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/Hunyuan3D 2.0 单视图模型生成材质纹理版_2069612558398615553.json

> 来源文件 `comfyui_library/workflows/平台全量/Hunyuan3D 2.0 单视图模型生成材质纹理版_2069612558398615553.json`

## 结构

**生成流程**：Model → Decode → Process → Output → Other

**节点**（53 个）：
- `ImageCompositeMasked`
- `UpscaleModelLoader`
- `Hy3DApplyTexture`
- `PreviewImage`
- `ImageUpscaleWithModel`
- `MaskToImage`
- `Hy3DBakeFromMultiview`
- `Hy3DMeshVerticeInpaintTexture`
- `ImageResize+`
- `DownloadAndLoadHy3DPaintModel`
- `PrimitiveNode`
- `Note`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Hy3DSampleMultiView`
- `Hy3DDiffusersSchedulerConfig`
- `Hy3DDiffusersSchedulerConfig`
- `ImageResize+`
- `Note`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `DownloadAndLoadHy3DDelightModel`
- `Hy3DDelightImage`
- `SolidMask`
- `Note`
- `PreviewImage`
- `Hy3DMeshUVWrap`
- `Hy3DRenderMultiView`
- `Hy3DCameraConfig`
- `PreviewImage`
- `PreviewImage`
- `CV2InpaintTexture`
- `Hy3DExportMesh`
- `Preview3D`
- `MaskPreview+`
- `TransparentBGSession+`
- `ImageRemoveBackground+`
- `Hy3DGenerateMesh`
- `Hy3DVAEDecode` ★核心
- `Hy3DPostprocessMesh`
- `Hy3DExportMesh`
- `Preview3D`
- `Note`
- `Note`
- `Note`
- `Hy3DModelLoader`
- `EmptyImage`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **64%**（34/53）

**有卡**：`ImageCompositeMasked`、`UpscaleModelLoader`、`Hy3DApplyTexture`、`ImageUpscaleWithModel`、`MaskToImage`、`Hy3DBakeFromMultiview`、`Hy3DMeshVerticeInpaintTexture`、`ImageResize+`、`DownloadAndLoadHy3DPaintModel`、`Hy3DSampleMultiView`、`Hy3DDiffusersSchedulerConfig`、`DownloadAndLoadHy3DDelightModel`、`Hy3DDelightImage`、`SolidMask`、`Hy3DMeshUVWrap`、`Hy3DRenderMultiView`、`Hy3DCameraConfig`、`CV2InpaintTexture`、`Hy3DExportMesh`、`Preview3D`、`MaskPreview+`、`TransparentBGSession+`、`ImageRemoveBackground+`、`Hy3DGenerateMesh`、`Hy3DVAEDecode`、`Hy3DPostprocessMesh`、`Hy3DModelLoader`、`EmptyImage`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、Hy3DVAEDecode、ImageUpscaleWithModel、UpscaleModelLoader、ImageResize+、MaskPreview+、Preview3D、SaveImage
