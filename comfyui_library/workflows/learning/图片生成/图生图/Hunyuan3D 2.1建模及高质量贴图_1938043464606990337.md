---
key: 图片生成/图生图/Hunyuan3D 2.1建模及高质量贴图_1938043464606990337.json
name: Hunyuan3D 2.1建模及高质量贴图_1938043464606990337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Hunyuan3D 2.1建模及高质量贴图_1938043464606990337.json
hash: 7634bcb35b1d3428
coverage: 0.833333
learned_at: 2026-10-23 11:03:03
nodes: [Hy3DPostprocessMesh, Hy3DExportMesh, Hy3DMultiViewsGenerator, Hy3DBakeMultiViews, Hy3DInPaint, Preview3D, INTConstant, StringConstant, Hy3D21LoadImageWithTransparency, PreviewImage, PreviewImage, PreviewImage, Hy3DMeshGenerator, Hy3D21VAELoader, Hy3D21VAEDecode, SaveImage, Hy3DMeshUVWrap, Hy3D21CameraConfig]
patterns: []
missing: []
---

# 图片生成/图生图/Hunyuan3D 2.1建模及高质量贴图_1938043464606990337.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Hunyuan3D 2.1建模及高质量贴图_1938043464606990337.json`

## 结构

**生成流程**：Model → Decode → Output → Other

**节点**（18 个）：
- `Hy3DPostprocessMesh`
- `Hy3DExportMesh`
- `Hy3DMultiViewsGenerator`
- `Hy3DBakeMultiViews`
- `Hy3DInPaint`
- `Preview3D`
- `INTConstant`
- `StringConstant`
- `Hy3D21LoadImageWithTransparency`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Hy3DMeshGenerator`
- `Hy3D21VAELoader`
- `Hy3D21VAEDecode` ★核心
- `SaveImage`
- `Hy3DMeshUVWrap`
- `Hy3D21CameraConfig`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`Hy3DPostprocessMesh`、`Hy3DExportMesh`、`Hy3DMultiViewsGenerator`、`Hy3DBakeMultiViews`、`Hy3DInPaint`、`Preview3D`、`INTConstant`、`StringConstant`、`Hy3D21LoadImageWithTransparency`、`Hy3DMeshGenerator`、`Hy3D21VAELoader`、`Hy3D21VAEDecode`、`SaveImage`、`Hy3DMeshUVWrap`、`Hy3D21CameraConfig`

**用到的条目**：Hy3D21VAEDecode、Hy3D21VAELoader、SaveImage、Preview3D、INTConstant、StringConstant、Hy3DExportMesh、Hy3DMeshUVWrap
