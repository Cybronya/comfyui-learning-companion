---
key: 图片生成/图生图/Hunyuan3D 2.1六视图工作流_1938058287684456450.json
name: Hunyuan3D 2.1六视图工作流_1938058287684456450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Hunyuan3D 2.1六视图工作流_1938058287684456450.json
hash: c890f9a2c14b1f7f
coverage: 1
learned_at: 2026-10-23 11:03:03
nodes: [Hy3DPostprocessMesh, Hy3D21VAEDecode, Hy3DMeshUVWrap, INTConstant, StringConstant, Hy3D21VAELoader, Hy3DMeshGenerator, Hy3D21LoadImageWithTransparency, Hy3D21CameraConfig, Hy3DExportMesh, SaveImage, Hy3DMultiViewsGenerator, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/Hunyuan3D 2.1六视图工作流_1938058287684456450.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Hunyuan3D 2.1六视图工作流_1938058287684456450.json`

## 结构

**生成流程**：Model → Decode → Output → Other

**节点**（13 个）：
- `Hy3DPostprocessMesh`
- `Hy3D21VAEDecode` ★核心
- `Hy3DMeshUVWrap`
- `INTConstant`
- `StringConstant`
- `Hy3D21VAELoader`
- `Hy3DMeshGenerator`
- `Hy3D21LoadImageWithTransparency`
- `Hy3D21CameraConfig`
- `Hy3DExportMesh`
- `SaveImage`
- `Hy3DMultiViewsGenerator`
- `SaveImage`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`Hy3DPostprocessMesh`、`Hy3D21VAEDecode`、`Hy3DMeshUVWrap`、`INTConstant`、`StringConstant`、`Hy3D21VAELoader`、`Hy3DMeshGenerator`、`Hy3D21LoadImageWithTransparency`、`Hy3D21CameraConfig`、`Hy3DExportMesh`、`SaveImage`、`Hy3DMultiViewsGenerator`

**用到的条目**：Hy3D21VAEDecode、Hy3D21VAELoader、SaveImage、INTConstant、StringConstant、Hy3DExportMesh、Hy3DMeshUVWrap、Hy3DPostprocessMesh
