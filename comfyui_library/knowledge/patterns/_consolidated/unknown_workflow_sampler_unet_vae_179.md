---
name: unknown_workflow_sampler_unet_vae_179
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.787
common_nodes: [ApplyTextureToMesh, BakeAmbientOcclusion, BakeNormalMapFromMesh, BakeTextureFromVoxel, CFGOverride, CLIPVisionLoader, DecimateMesh, EmptyTrellis2LatentStructure, GetMeshInfo, ImageCropToMask, KSampler, LoadBackgroundRemovalModel, LoadImage, MeshSmoothNormals, ModelSamplingSD3, PreviewImage, PrimitiveInt, RemeshMesh, RemoveBackground, RenderUVAtlas, RescaleCFG, Trellis2ShapeStage, Trellis2TextureStage, Trellis2UpsampleStage, UNETLoader, UnwrapMesh, VAELoader, VaeDecodeShapeTrellis, VaeDecodeStructureTrellis2, VaeDecodeTextureTrellis]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [comfyui-workflow-templates-json/3d_pixal3d_multi_views.json, comfyui-workflow-templates-json/3d_pixal3d_trellis2_image_to_model.json, 平台全量/Pixal3D Trellis2 参考图生成3D模型标准版_2108057333803868161.json, 平台全量/Pixal3D Trellis2 参考图生成3D模型简化版_2108058889227956226.json, 平台全量/vibe-AI生成3d模型_2105167198208745474.json, 数字人/数字人/3d_pixal3d_multi_views四视图生成模型_2108829641850056706.json, 数字人/数字人/3d模型生成_pixal3d_trellis2_image_to_model_2108827029666881538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_179

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（comfyui-workflow-templates-json/3d_pixal3d_multi_views.json、comfyui-workflow-templates-json/3d_pixal3d_trellis2_image_to_model.json、平台全量/Pixal3D Trellis2 参考图生成3D模型标准版_2108057333803868161.json、平台全量/Pixal3D Trellis2 参考图生成3D模型简化版_2108058889227956226.json、平台全量/vibe-AI生成3d模型_2105167198208745474.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
- `ApplyTextureToMesh`
- `BakeAmbientOcclusion`
- `BakeNormalMapFromMesh`
- `BakeTextureFromVoxel`
- `CFGOverride`
- `CLIPVisionLoader`
- `DecimateMesh`
- `EmptyTrellis2LatentStructure`
- `GetMeshInfo`
- `ImageCropToMask`
- `KSampler`
- `LoadBackgroundRemovalModel`
- `LoadImage`
- `MeshSmoothNormals`
- `ModelSamplingSD3`
- `PreviewImage`
- `PrimitiveInt`
- `RemeshMesh`
- `RemoveBackground`
- `RenderUVAtlas`
- `RescaleCFG`
- `Trellis2ShapeStage`
- `Trellis2TextureStage`
- `Trellis2UpsampleStage`
- `UNETLoader`
- `UnwrapMesh`
- `VAELoader`
- `VaeDecodeShapeTrellis`
- `VaeDecodeStructureTrellis2`
- `VaeDecodeTextureTrellis`

**可变部分**（部分 workflow 才有）：
- `PaintMesh` —— 6/7 个有
- `VoxelToMesh` —— 6/7 个有
- `ComfySwitchNode` —— 5/7 个有
- `LoadMoGeModel` —— 5/7 个有
- `MaskPreview` —— 5/7 个有
- `MoGeGeometryToFOV` —— 5/7 个有
- `MoGeInference` —— 5/7 个有
- `Pixal3DConditioning` —— 5/7 个有
- `PrimitiveBoolean` —— 5/7 个有
- `SaveImage` —— 5/7 个有
- `Trellis2Conditioning` —— 5/7 个有
- `MeshToFile3D` —— 4/7 个有
- `Preview3DAdvanced` —— 4/7 个有
- `Save3DAdvanced` —— 4/7 个有
- `SaveGLB` —— 3/7 个有
- `Pixal3DMultiViewConditioning` —— 2/7 个有
- `SaveImageAdvanced` —— 2/7 个有
- `ImageCropV2` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 12 - 20 | 7 | 79% |
| Prompt 约束强度(CFG) | 7.5 | 7.5 - 7.5 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 7/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 12，观测区间 12 - 20，7 个样本
- Prompt 约束强度(CFG) 中位数 7.5，观测区间 7.5 - 7.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：发现KSampler但没有VAEDecode
