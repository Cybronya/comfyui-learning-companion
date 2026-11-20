---
name: unknown_workflow_sampler_unet_vae_224
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.81375
common_nodes: [ApplyTextureToMesh, BakeAmbientOcclusion, BakeNormalMapFromMesh, BakeTextureFromVoxel, CFGOverride, CLIPVisionLoader, DecimateMesh, EmptyTrellis2LatentStructure, GetMeshInfo, ImageCropToMask, KSampler, LoadBackgroundRemovalModel, LoadImage, MeshSmoothNormals, MeshToFile3D, ModelSamplingSD3, PaintMesh, Preview3DAdvanced, PreviewImage, PrimitiveInt, RemeshMesh, RemoveBackground, RenderUVAtlas, RescaleCFG, Save3DAdvanced, Trellis2ShapeStage, Trellis2TextureStage, Trellis2UpsampleStage, UNETLoader, UnwrapMesh, VAELoader, VaeDecodeShapeTrellis, VaeDecodeStructureTrellis2, VaeDecodeTextureTrellis, VoxelToMesh]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [comfyui-workflow-templates-json/3d_pixal3d_multi_views.json, comfyui-workflow-templates-json/3d_pixal3d_trellis2_image_to_model.json, 数字人/数字人/3d_pixal3d_multi_views四视图生成模型_2108829641850056706.json, 数字人/数字人/3d模型生成_pixal3d_trellis2_image_to_model_2108827029666881538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_224

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/3d_pixal3d_multi_views.json、comfyui-workflow-templates-json/3d_pixal3d_trellis2_image_to_model.json、数字人/数字人/3d_pixal3d_multi_views四视图生成模型_2108829641850056706.json、数字人/数字人/3d模型生成_pixal3d_trellis2_image_to_model_2108827029666881538.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
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
- `MeshToFile3D`
- `ModelSamplingSD3`
- `PaintMesh`
- `Preview3DAdvanced`
- `PreviewImage`
- `PrimitiveInt`
- `RemeshMesh`
- `RemoveBackground`
- `RenderUVAtlas`
- `RescaleCFG`
- `Save3DAdvanced`
- `Trellis2ShapeStage`
- `Trellis2TextureStage`
- `Trellis2UpsampleStage`
- `UNETLoader`
- `UnwrapMesh`
- `VAELoader`
- `VaeDecodeShapeTrellis`
- `VaeDecodeStructureTrellis2`
- `VaeDecodeTextureTrellis`
- `VoxelToMesh`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/4 个有
- `LoadMoGeModel` —— 2/4 个有
- `MaskPreview` —— 2/4 个有
- `MoGeGeometryToFOV` —— 2/4 个有
- `MoGeInference` —— 2/4 个有
- `Pixal3DConditioning` —— 2/4 个有
- `Pixal3DMultiViewConditioning` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `SaveImageAdvanced` —— 2/4 个有
- `Trellis2Conditioning` —— 2/4 个有
- `ImageCropV2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 12 - 20 | 4 | 75% |
| Prompt 约束强度(CFG) | 7.5 | 7.5 - 7.5 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 4/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 12，观测区间 12 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 7.5，观测区间 7.5 - 7.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：发现KSampler但没有VAEDecode
