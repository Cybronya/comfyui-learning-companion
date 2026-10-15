---
key: comfyui-workflow-templates-json/3d_triposplat_image_to_gaussian_splat.json
name: 3d_triposplat_image_to_gaussian_splat
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/3d_triposplat_image_to_gaussian_splat.json
hash: 25d9256b082e2eed
official: true
coverage: 0.833333
learned_at: 2026-10-15 22:24:47
nodes: [SaveGLB, CreateCameraInfo, SplatToMesh, SaveVideo, RenderSplat, CreateVideo, SaveGLB, SplatToFile3D, MarkdownNote, MarkdownNote, b64333d5-4e6f-4e99-9506-2ec4f63259fe, LoadImage]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/3d_triposplat_image_to_gaussian_splat.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/3d_triposplat_image_to_gaussian_splat.json`

## 结构

**生成流程**：Output → Other

**节点**（12 个）：
- `SaveGLB`
- `CreateCameraInfo`
- `SplatToMesh`
- `SaveVideo`
- `RenderSplat`
- `CreateVideo`
- `SaveGLB`
- `SplatToFile3D`
- `MarkdownNote`
- `MarkdownNote`
- `b64333d5-4e6f-4e99-9506-2ec4f63259fe`
- `LoadImage`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`SaveGLB`、`CreateCameraInfo`、`SplatToMesh`、`SaveVideo`、`RenderSplat`、`CreateVideo`、`SplatToFile3D`、`b64333d5-4e6f-4e99-9506-2ec4f63259fe`、`LoadImage`

**用到的条目**：LoadImage、SaveVideo、SaveGLB、CreateVideo、CreateCameraInfo、RenderSplat、SplatToFile3D、SplatToMesh
