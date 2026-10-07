---
key: comfyui-workflow-templates-json/3d_pixal3d_trellis2_image_to_model.json
name: 3d_pixal3d_trellis2_image_to_model
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/3d_pixal3d_trellis2_image_to_model.json
hash: 628844750e64fb13
official: true
coverage: 0.772727
learned_at: 2026-10-07 21:33:13
nodes: [Trellis2ShapeStage, PreviewImage, PreviewImage, PreviewImage, VAELoader, VaeDecodeTextureTrellis, CLIPVisionLoader, GetMeshInfo, RenderUVAtlas, PreviewImage, KSampler, ApplyTextureToMesh, BakeTextureFromVoxel, PrimitiveInt, MeshSmoothNormals, KSampler, PaintMesh, CFGOverride, RescaleCFG, RemoveBackground, ComfySwitchNode, MaskPreview, PreviewImage, Preview3DAdvanced, VaeDecodeStructureTrellis2, VoxelToMesh, MeshToFile3D, KSampler, RescaleCFG, CFGOverride, ModelSamplingSD3, Note, Trellis2UpsampleStage, BakeAmbientOcclusion, BakeNormalMapFromMesh, PreviewImage, PreviewImage, RemeshMesh, DecimateMesh, UnwrapMesh, VAELoader, LoadMoGeModel, LoadBackgroundRemovalModel, MoGeInference, MoGeGeometryToFOV, Trellis2Conditioning, Pixal3DConditioning, VaeDecodeShapeTrellis, UNETLoader, Trellis2TextureStage, MeshToFile3D, MeshSmoothNormals, MeshToFile3D, EmptyTrellis2LatentStructure, KSampler, LoadImage, ImageCropToMask, MarkdownNote, ComfySwitchNode, ComfySwitchNode, PrimitiveBoolean, MarkdownNote, ComfySwitchNode, UNETLoader, Save3DAdvanced, Preview3DAdvanced]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 7.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 12}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/3d_pixal3d_trellis2_image_to_model.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/3d_pixal3d_trellis2_image_to_model.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（66 个）：
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
- `MaskPreview`
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
- `LoadImage`
- `ImageCropToMask`
- `MarkdownNote`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `MarkdownNote`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `Save3DAdvanced`
- `Preview3DAdvanced`

## 关键参数

- `seed` = `42`
- `steps` = `12`
- `cfg` = `7.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（51/66）

**有卡**：`Trellis2ShapeStage`、`VAELoader`、`VaeDecodeTextureTrellis`、`CLIPVisionLoader`、`GetMeshInfo`、`RenderUVAtlas`、`KSampler`、`ApplyTextureToMesh`、`BakeTextureFromVoxel`、`MeshSmoothNormals`、`PaintMesh`、`CFGOverride`、`RescaleCFG`、`RemoveBackground`、`MaskPreview`、`Preview3DAdvanced`、`VaeDecodeStructureTrellis2`、`VoxelToMesh`、`MeshToFile3D`、`ModelSamplingSD3`、`Trellis2UpsampleStage`、`BakeAmbientOcclusion`、`BakeNormalMapFromMesh`、`RemeshMesh`、`DecimateMesh`、`UnwrapMesh`、`LoadMoGeModel`、`LoadBackgroundRemovalModel`、`MoGeInference`、`MoGeGeometryToFOV`、`Trellis2Conditioning`、`Pixal3DConditioning`、`VaeDecodeShapeTrellis`、`UNETLoader`、`Trellis2TextureStage`、`EmptyTrellis2LatentStructure`、`LoadImage`、`ImageCropToMask`、`PrimitiveBoolean`、`Save3DAdvanced`

**用到的条目**：KSampler、VAELoader、LoadImage、UNETLoader、RescaleCFG、CFGOverride、EmptyTrellis2LatentStructure、VaeDecodeShapeTrellis

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
