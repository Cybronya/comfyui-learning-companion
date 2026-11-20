---
name: unknown_workflow_vae_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [Hy3D21CameraConfig, Hy3D21LoadImageWithTransparency, Hy3D21VAEDecode, Hy3D21VAELoader, Hy3DExportMesh, Hy3DMeshGenerator, Hy3DMeshUVWrap, Hy3DMultiViewsGenerator, Hy3DPostprocessMesh, INTConstant, SaveImage, StringConstant]
problems: []
missing: []
members: [图片生成/图生图/Hunyuan3D 2.1六视图工作流_1938058287684456450.json, 图片生成/图生图/Hunyuan3D 2.1建模及高质量贴图_1938043464606990337.json]
source: knowledge_consolidation
---

# unknown_workflow_vae_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Hunyuan3D 2.1六视图工作流_1938058287684456450.json、图片生成/图生图/Hunyuan3D 2.1建模及高质量贴图_1938043464606990337.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `Hy3D21CameraConfig`
- `Hy3D21LoadImageWithTransparency`
- `Hy3D21VAEDecode`
- `Hy3D21VAELoader`
- `Hy3DExportMesh`
- `Hy3DMeshGenerator`
- `Hy3DMeshUVWrap`
- `Hy3DMultiViewsGenerator`
- `Hy3DPostprocessMesh`
- `INTConstant`
- `SaveImage`
- `StringConstant`

**可变部分**（部分 workflow 才有）：
- `Hy3DBakeMultiViews` —— 1/2 个有
- `Hy3DInPaint` —— 1/2 个有
- `Preview3D` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
