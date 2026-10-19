---
key: 数字人/数字人/3d模型生成_pixal3d_trellis2_image_to_model_2108827029666881538.json
name: 3d模型生成_pixal3d_trellis2_image_to_model_2108827029666881538
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/3d模型生成_pixal3d_trellis2_image_to_model_2108827029666881538.json
hash: 3b47acb5d7c06d97
coverage: 0.776119
learned_at: 2026-10-19 00:40:57
nodes: [Trellis2ShapeStage, PreviewImage, PreviewImage, PreviewImage, VAELoader, VaeDecodeTextureTrellis, CLIPVisionLoader, GetMeshInfo, RenderUVAtlas, PreviewImage, KSampler, ApplyTextureToMesh, BakeTextureFromVoxel, PrimitiveInt, MeshSmoothNormals, KSampler, PaintMesh, CFGOverride, RescaleCFG, RemoveBackground, ComfySwitchNode, PreviewImage, Preview3DAdvanced, VaeDecodeStructureTrellis2, VoxelToMesh, MeshToFile3D, KSampler, RescaleCFG, CFGOverride, ModelSamplingSD3, Note, Trellis2UpsampleStage, BakeAmbientOcclusion, BakeNormalMapFromMesh, PreviewImage, PreviewImage, RemeshMesh, DecimateMesh, UnwrapMesh, VAELoader, LoadMoGeModel, LoadBackgroundRemovalModel, MoGeInference, MoGeGeometryToFOV, Trellis2Conditioning, Pixal3DConditioning, VaeDecodeShapeTrellis, UNETLoader, Trellis2TextureStage, MeshToFile3D, MeshSmoothNormals, MeshToFile3D, EmptyTrellis2LatentStructure, KSampler, MarkdownNote, ComfySwitchNode, ComfySwitchNode, PrimitiveBoolean, MarkdownNote, ComfySwitchNode, UNETLoader, Save3DAdvanced, Preview3DAdvanced, LoadImage, MaskPreview, ImageCropToMask, SaveImage]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 7.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 12}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/3d模型生成_pixal3d_trellis2_image_to_model_2108827029666881538.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/3d模型生成_pixal3d_trellis2_image_to_model_2108827029666881538.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（67 个）：
- `Trellis2ShapeStage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `VAELoader`
- `VaeDecodeTextureTrellis` ★核心
- `CLIPVisionLoader`
- `GetMeshInfo`
- `RenderUVAtlas`
- `PreviewImage`
- `KSampler` ★核心
- `ApplyTextureToMesh`
- `BakeTextureFromVoxel`
- `PrimitiveInt`
- `MeshSmoothNormals`
- `KSampler` ★核心
- `PaintMesh`
- `CFGOverride`
- `RescaleCFG`
- `RemoveBackground`
- `ComfySwitchNode`
- `PreviewImage`
- `Preview3DAdvanced`
- `VaeDecodeStructureTrellis2` ★核心
- `VoxelToMesh`
- `MeshToFile3D`
- `KSampler` ★核心
- `RescaleCFG`
- `CFGOverride`
- `ModelSamplingSD3`
- `Note`
- `Trellis2UpsampleStage`
- `BakeAmbientOcclusion`
- `BakeNormalMapFromMesh`
- `PreviewImage`
- `PreviewImage`
- `RemeshMesh`
- `DecimateMesh`
- `UnwrapMesh`
- `VAELoader`
- `LoadMoGeModel`
- `LoadBackgroundRemovalModel`
- `MoGeInference`
- `MoGeGeometryToFOV`
- `Trellis2Conditioning`
- `Pixal3DConditioning`
- `VaeDecodeShapeTrellis` ★核心
- `UNETLoader` ★核心
- `Trellis2TextureStage`
- `MeshToFile3D`
- `MeshSmoothNormals`
- `MeshToFile3D`
- `EmptyTrellis2LatentStructure`
- `KSampler` ★核心
- `MarkdownNote`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `MarkdownNote`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `Save3DAdvanced`
- `Preview3DAdvanced`
- `LoadImage`
- `MaskPreview`
- `ImageCropToMask`
- `SaveImage`

## 关键参数

- `seed` = `42`
- `steps` = `12`
- `cfg` = `7.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（52/67）

**有卡**：`Trellis2ShapeStage`、`VAELoader`、`VaeDecodeTextureTrellis`、`CLIPVisionLoader`、`GetMeshInfo`、`RenderUVAtlas`、`KSampler`、`ApplyTextureToMesh`、`BakeTextureFromVoxel`、`MeshSmoothNormals`、`PaintMesh`、`CFGOverride`、`RescaleCFG`、`RemoveBackground`、`Preview3DAdvanced`、`VaeDecodeStructureTrellis2`、`VoxelToMesh`、`MeshToFile3D`、`ModelSamplingSD3`、`Trellis2UpsampleStage`、`BakeAmbientOcclusion`、`BakeNormalMapFromMesh`、`RemeshMesh`、`DecimateMesh`、`UnwrapMesh`、`LoadMoGeModel`、`LoadBackgroundRemovalModel`、`MoGeInference`、`MoGeGeometryToFOV`、`Trellis2Conditioning`、`Pixal3DConditioning`、`VaeDecodeShapeTrellis`、`UNETLoader`、`Trellis2TextureStage`、`EmptyTrellis2LatentStructure`、`PrimitiveBoolean`、`Save3DAdvanced`、`LoadImage`、`MaskPreview`、`ImageCropToMask`、`SaveImage`

**用到的条目**：KSampler、VAELoader、LoadImage、UNETLoader、RescaleCFG、CFGOverride、EmptyTrellis2LatentStructure、VaeDecodeShapeTrellis

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
