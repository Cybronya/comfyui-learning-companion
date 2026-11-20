---
key: 平台全量/SeedVR2.5图片批量高清放大_1991406880526454785.json
name: SeedVR2.5图片批量高清放大_1991406880526454785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeedVR2.5图片批量高清放大_1991406880526454785.json
hash: e8dc5ee026d5058b
coverage: 0.833333
learned_at: 2026-11-14 00:59:35
nodes: [RHExtractImage, easy imageCount, Bjornulf_ShowInt, easy forLoopStart, PreviewImage, RHBatchImages:, easy forLoopEnd, Bjornulf_ShowInt, PreviewImage, SeedVR2ExtraArgs, SeedVR2BlockSwap, SeedVR2GGUF, RHExtractImage, easy imageSizeBySide, SimpleMath+, SaveImage, PrimitiveInt, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SaveImage, RHUploadZip, SaveImage, easy showAnything]
patterns: []
missing: []
---

# 平台全量/SeedVR2.5图片批量高清放大_1991406880526454785.json

> 来源文件 `comfyui_library/workflows/平台全量/SeedVR2.5图片批量高清放大_1991406880526454785.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（24 个）：
- `RHExtractImage`
- `easy imageCount`
- `Bjornulf_ShowInt`
- `easy forLoopStart`
- `PreviewImage`
- `RHBatchImages:`
- `easy forLoopEnd`
- `Bjornulf_ShowInt`
- `PreviewImage`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `SeedVR2GGUF`
- `RHExtractImage`
- `easy imageSizeBySide`
- `SimpleMath+`
- `SaveImage`
- `PrimitiveInt`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `RHUploadZip`
- `SaveImage`
- `easy showAnything`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`RHExtractImage`、`easy imageCount`、`Bjornulf_ShowInt`、`easy forLoopStart`、`RHBatchImages:`、`easy forLoopEnd`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`SeedVR2GGUF`、`easy imageSizeBySide`、`SimpleMath+`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`RHUploadZip`

**用到的条目**：SeedVR2BlockSwap、SeedVR2ExtraArgs、SeedVR2GGUF、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、easy imageSizeBySide、SaveImage
