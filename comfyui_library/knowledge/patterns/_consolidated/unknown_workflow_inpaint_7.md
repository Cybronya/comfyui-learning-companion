---
name: unknown_workflow_inpaint_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.829
common_nodes: [Deep Bump (mtb), Hy3D21CameraConfig, Hy3D21ResizeImages, Hy3DBakeMultiViews, Hy3DExportMesh, Hy3DInPaint, Hy3DMultiViewsGenerator, ImageRemoveBackground+, LoadImage, NormalMapSimple, Preview3D, PreviewImage, SaveImage, TransparentBGSession+]
problems: []
missing: []
members: [平台全量/Hy3D2.1单图转3D_2050115671438180354.json, 平台全量/材质绘制_2043503374032703490.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Hy3D2.1单图转3D_2050115671438180354.json、平台全量/材质绘制_2043503374032703490.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `Deep Bump (mtb)`
- `Hy3D21CameraConfig`
- `Hy3D21ResizeImages`
- `Hy3DBakeMultiViews`
- `Hy3DExportMesh`
- `Hy3DInPaint`
- `Hy3DMultiViewsGenerator`
- `ImageRemoveBackground+`
- `LoadImage`
- `NormalMapSimple`
- `Preview3D`
- `PreviewImage`
- `SaveImage`
- `TransparentBGSession+`

**可变部分**（部分 workflow 才有）：
- `Hy3D21VAEDecode` —— 1/2 个有
- `Hy3D21VAELoader` —— 1/2 个有
- `Hy3DMeshGenerator` —— 1/2 个有
- `Hy3DPostprocessMesh` —— 1/2 个有
- `Hy3DUploadMesh` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
