---
name: unknown_workflow_inpaint_vae_2
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7805
common_nodes: [CV2InpaintTexture, DownloadAndLoadHy3DPaintModel, Hy3DApplyTexture, Hy3DBakeFromMultiview, Hy3DCameraConfig, Hy3DDiffusersSchedulerConfig, Hy3DExportMesh, Hy3DGenerateMesh, Hy3DMeshUVWrap, Hy3DMeshVerticeInpaintTexture, Hy3DModelLoader, Hy3DPostprocessMesh, Hy3DRenderMultiView, Hy3DSampleMultiView, Hy3DVAEDecode, ImageRemoveBackground+, ImageResize+, LoadImage, Preview3D, PreviewImage, SaveImage, TransparentBGSession+]
problems: []
missing: []
members: [平台全量/末影zp自用_2097715430239588353.json, 平台全量/混元 Hunyuan3D-TEXTRUE-贴图优化版_2041683785745436674.json, 平台全量/腾讯混元3D白膜和带纹理混元3D模型_1896880829044301825.json, 视频生成/文生视频/3D模型 图片转3D模型  （可导出glb、obj、stl格式）_2107673452059652098.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_vae_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/末影zp自用_2097715430239588353.json、平台全量/混元 Hunyuan3D-TEXTRUE-贴图优化版_2041683785745436674.json、平台全量/腾讯混元3D白膜和带纹理混元3D模型_1896880829044301825.json、视频生成/文生视频/3D模型 图片转3D模型  （可导出glb、obj、stl格式）_2107673452059652098.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `CV2InpaintTexture`
- `DownloadAndLoadHy3DPaintModel`
- `Hy3DApplyTexture`
- `Hy3DBakeFromMultiview`
- `Hy3DCameraConfig`
- `Hy3DDiffusersSchedulerConfig`
- `Hy3DExportMesh`
- `Hy3DGenerateMesh`
- `Hy3DMeshUVWrap`
- `Hy3DMeshVerticeInpaintTexture`
- `Hy3DModelLoader`
- `Hy3DPostprocessMesh`
- `Hy3DRenderMultiView`
- `Hy3DSampleMultiView`
- `Hy3DVAEDecode`
- `ImageRemoveBackground+`
- `ImageResize+`
- `LoadImage`
- `Preview3D`
- `PreviewImage`
- `SaveImage`
- `TransparentBGSession+`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadHy3DDelightModel` —— 2/4 个有
- `Hy3DDelightImage` —— 2/4 个有
- `ImageCompositeMasked` —— 2/4 个有
- `MaskPreview+` —— 2/4 个有
- `MaskToImage` —— 2/4 个有
- `SolidMask` —— 2/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `SaveGLB` —— 1/4 个有
- `TrimeshToMESH` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
