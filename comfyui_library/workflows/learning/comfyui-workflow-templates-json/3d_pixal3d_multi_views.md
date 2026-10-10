---
key: comfyui-workflow-templates-json/3d_pixal3d_multi_views.json
name: 3d_pixal3d_multi_views
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/3d_pixal3d_multi_views.json
hash: eb448b03a96a477a
official: true
coverage: 0.852941
learned_at: 2026-10-10 22:43:02
nodes: [Trellis2ShapeStage, PreviewImage, PreviewImage, PreviewImage, VAELoader, VaeDecodeTextureTrellis, CLIPVisionLoader, GetMeshInfo, RenderUVAtlas, PreviewImage, KSampler, ApplyTextureToMesh, BakeTextureFromVoxel, PrimitiveInt, MeshSmoothNormals, KSampler, PaintMesh, CFGOverride, RescaleCFG, RemoveBackground, Preview3DAdvanced, VaeDecodeStructureTrellis2, VoxelToMesh, MeshToFile3D, KSampler, RescaleCFG, CFGOverride, ModelSamplingSD3, Note, Trellis2UpsampleStage, BakeAmbientOcclusion, BakeNormalMapFromMesh, PreviewImage, PreviewImage, RemeshMesh, DecimateMesh, UnwrapMesh, VAELoader, LoadBackgroundRemovalModel, VaeDecodeShapeTrellis, Trellis2TextureStage, MeshToFile3D, MeshSmoothNormals, MeshToFile3D, EmptyTrellis2LatentStructure, KSampler, ImageCropToMask, UNETLoader, Preview3DAdvanced, Pixal3DMultiViewConditioning, ImageCropV2, SaveImageAdvanced, ImageCropV2, ImageCropV2, SaveImageAdvanced, SaveImageAdvanced, ImageCropV2, SaveImageAdvanced, RemoveBackground, ImageCropToMask, ImageCropToMask, RemoveBackground, ImageCropToMask, RemoveBackground, LoadImage, Save3DAdvanced, MarkdownNote, MarkdownNote]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 7.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 12}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# comfyui-workflow-templates-json/3d_pixal3d_multi_views.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/3d_pixal3d_multi_views.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
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
- `LoadBackgroundRemovalModel`
- `VaeDecodeShapeTrellis` ★核心
- `Trellis2TextureStage`
- `MeshToFile3D`
- `MeshSmoothNormals`
- `MeshToFile3D`
- `EmptyTrellis2LatentStructure`
- `KSampler` ★核心
- `ImageCropToMask`
- `UNETLoader` ★核心
- `Preview3DAdvanced`
- `Pixal3DMultiViewConditioning`
- `ImageCropV2`
- `SaveImageAdvanced`
- `ImageCropV2`
- `ImageCropV2`
- `SaveImageAdvanced`
- `SaveImageAdvanced`
- `ImageCropV2`
- `SaveImageAdvanced`
- `RemoveBackground`
- `ImageCropToMask`
- `ImageCropToMask`
- `RemoveBackground`
- `ImageCropToMask`
- `RemoveBackground`
- `LoadImage`
- `Save3DAdvanced`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `seed` = `42`
- `steps` = `12`
- `cfg` = `7.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（58/68）

**有卡**：`Trellis2ShapeStage`、`VAELoader`、`VaeDecodeTextureTrellis`、`CLIPVisionLoader`、`GetMeshInfo`、`RenderUVAtlas`、`KSampler`、`ApplyTextureToMesh`、`BakeTextureFromVoxel`、`MeshSmoothNormals`、`PaintMesh`、`CFGOverride`、`RescaleCFG`、`RemoveBackground`、`Preview3DAdvanced`、`VaeDecodeStructureTrellis2`、`VoxelToMesh`、`MeshToFile3D`、`ModelSamplingSD3`、`Trellis2UpsampleStage`、`BakeAmbientOcclusion`、`BakeNormalMapFromMesh`、`RemeshMesh`、`DecimateMesh`、`UnwrapMesh`、`LoadBackgroundRemovalModel`、`VaeDecodeShapeTrellis`、`Trellis2TextureStage`、`EmptyTrellis2LatentStructure`、`ImageCropToMask`、`UNETLoader`、`Pixal3DMultiViewConditioning`、`ImageCropV2`、`SaveImageAdvanced`、`LoadImage`、`Save3DAdvanced`

**用到的条目**：KSampler、VAELoader、LoadImage、UNETLoader、RescaleCFG、CFGOverride、EmptyTrellis2LatentStructure、VaeDecodeShapeTrellis

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
