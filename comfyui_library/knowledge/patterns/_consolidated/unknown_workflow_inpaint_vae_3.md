---
name: unknown_workflow_inpaint_vae_3
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.741667
common_nodes: [CV2InpaintTexture, DownloadAndLoadHy3DDelightModel, DownloadAndLoadHy3DPaintModel, EmptyImage, Hy3DApplyTexture, Hy3DBakeFromMultiview, Hy3DCameraConfig, Hy3DDelightImage, Hy3DDiffusersSchedulerConfig, Hy3DExportMesh, Hy3DGenerateMesh, Hy3DMeshUVWrap, Hy3DMeshVerticeInpaintTexture, Hy3DModelLoader, Hy3DPostprocessMesh, Hy3DRenderMultiView, Hy3DSampleMultiView, Hy3DVAEDecode, ImageCompositeMasked, ImageResize+, LayerColor: Brightness & Contrast, LayerUtility: ColorImage V2, LoadImage, MaskPreview+, Preview3D, PreviewImage, RMBG, SaveImage, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/图生多视角_三维 _ 混元3D_1902281610819952642.json, 平台全量/图生3D-带材质输出-混元3D_2003999860925865985.json, 平台全量/混元3D-图生3D模型_2002736631213879298.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_vae_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图生多视角_三维 _ 混元3D_1902281610819952642.json、平台全量/图生3D-带材质输出-混元3D_2003999860925865985.json、平台全量/混元3D-图生3D模型_2002736631213879298.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CV2InpaintTexture`
- `DownloadAndLoadHy3DDelightModel`
- `DownloadAndLoadHy3DPaintModel`
- `EmptyImage`
- `Hy3DApplyTexture`
- `Hy3DBakeFromMultiview`
- `Hy3DCameraConfig`
- `Hy3DDelightImage`
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
- `ImageCompositeMasked`
- `ImageResize+`
- `LayerColor: Brightness & Contrast`
- `LayerUtility: ColorImage V2`
- `LoadImage`
- `MaskPreview+`
- `Preview3D`
- `PreviewImage`
- `RMBG`
- `SaveImage`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CR String To Combo` —— 2/3 个有
- `ImageFromBatch` —— 2/3 个有
- `Int` —— 2/3 个有
- `Int To Bool (mtb)` —— 2/3 个有
- `InversionDemoLazyIndexSwitch` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `TextBox` —— 2/3 个有
- `easy imageConcat` —— 2/3 个有
- `easy int` —— 2/3 个有
- `easy showAnything` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
