---
name: unknown_workflow_inpaint_vae
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.820571
common_nodes: [CV2InpaintTexture, DownloadAndLoadHy3DPaintModel, Hy3DApplyTexture, Hy3DBakeFromMultiview, Hy3DCameraConfig, Hy3DDiffusersSchedulerConfig, Hy3DExportMesh, Hy3DGenerateMesh, Hy3DMeshUVWrap, Hy3DMeshVerticeInpaintTexture, Hy3DModelLoader, Hy3DPostprocessMesh, Hy3DRenderMultiView, Hy3DSampleMultiView, Hy3DVAEDecode, ImageRemoveBackground+, ImageResize+, LoadImage, Preview3D, SaveImage, TransparentBGSession+]
problems: []
missing: []
members: [图片生成/反推提示词/583D(tidai)_2054051475474657281.json, 图片生成/反推提示词/58moxin3d_2051519618098974721.json, 图片生成/图生图/3D模型 图片转3D模型 hunyuan3D_2052093287670001666.json, 图片生成/图生图/hunyuan3D-图片转3D模型_2045107253841235970.json, 图片生成/图生图/图片一键转3D模型_2044680361459851265.json, 图片生成/图生图/超好用🔥图片转3D模型-最新_2052597152983076866.json, 视频生成/文生视频/3D模型 图片转3D模型  （可导出glb、obj、stl格式）_2107673452059652098.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_vae

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/583D(tidai)_2054051475474657281.json、图片生成/反推提示词/58moxin3d_2051519618098974721.json、图片生成/图生图/3D模型 图片转3D模型 hunyuan3D_2052093287670001666.json、图片生成/图生图/hunyuan3D-图片转3D模型_2045107253841235970.json、图片生成/图生图/图片一键转3D模型_2044680361459851265.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
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
- `SaveImage`
- `TransparentBGSession+`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadHy3DDelightModel` —— 6/7 个有
- `Hy3DDelightImage` —— 6/7 个有
- `ImageCompositeMasked` —— 6/7 个有
- `MaskToImage` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `SolidMask` —— 6/7 个有
- `MaskPreview+` —— 4/7 个有
- `LayerMask: MaskPreview` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
