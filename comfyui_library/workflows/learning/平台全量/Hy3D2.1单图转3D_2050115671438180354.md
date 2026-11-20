---
key: 平台全量/Hy3D2.1单图转3D_2050115671438180354.json
name: Hy3D2.1单图转3D_2050115671438180354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Hy3D2.1单图转3D_2050115671438180354.json
hash: 061671e77a2d33e4
coverage: 0.84
learned_at: 2026-11-14 00:32:08
nodes: [Hy3D21VAEDecode, Hy3DMeshGenerator, Hy3DBakeMultiViews, Hy3DMultiViewsGenerator, TransparentBGSession+, ImageRemoveBackground+, Preview3D, Hy3DPostprocessMesh, Hy3D21CameraConfig, PreviewImage, Hy3D21ResizeImages, Hy3D21ResizeImages, Hy3DInPaint, PreviewImage, Hy3DExportMesh, NormalMapSimple, SaveImage, Deep Bump (mtb), SaveImage, PreviewImage, PreviewImage, LoadImage, Preview3D, Hy3DExportMesh, Hy3D21VAELoader]
patterns: []
missing: []
---

# 平台全量/Hy3D2.1单图转3D_2050115671438180354.json

> 来源文件 `comfyui_library/workflows/平台全量/Hy3D2.1单图转3D_2050115671438180354.json`

## 结构

**生成流程**：Model → Decode → Process → Output → Other

**节点**（25 个）：
- `Hy3D21VAEDecode` ★核心
- `Hy3DMeshGenerator`
- `Hy3DBakeMultiViews`
- `Hy3DMultiViewsGenerator`
- `TransparentBGSession+`
- `ImageRemoveBackground+`
- `Preview3D`
- `Hy3DPostprocessMesh`
- `Hy3D21CameraConfig`
- `PreviewImage`
- `Hy3D21ResizeImages`
- `Hy3D21ResizeImages`
- `Hy3DInPaint`
- `PreviewImage`
- `Hy3DExportMesh`
- `NormalMapSimple`
- `SaveImage`
- `Deep Bump (mtb)`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `Preview3D`
- `Hy3DExportMesh`
- `Hy3D21VAELoader`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`Hy3D21VAEDecode`、`Hy3DMeshGenerator`、`Hy3DBakeMultiViews`、`Hy3DMultiViewsGenerator`、`TransparentBGSession+`、`ImageRemoveBackground+`、`Preview3D`、`Hy3DPostprocessMesh`、`Hy3D21CameraConfig`、`Hy3D21ResizeImages`、`Hy3DInPaint`、`Hy3DExportMesh`、`NormalMapSimple`、`SaveImage`、`Deep Bump (mtb)`、`LoadImage`、`Hy3D21VAELoader`

**用到的条目**：LoadImage、Hy3D21VAEDecode、Hy3D21VAELoader、Hy3D21ResizeImages、Preview3D、SaveImage、Deep Bump (mtb)、Hy3D21CameraConfig
