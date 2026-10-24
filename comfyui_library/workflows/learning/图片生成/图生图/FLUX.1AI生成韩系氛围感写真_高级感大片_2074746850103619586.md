---
key: 图片生成/图生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2074746850103619586.json
name: FLUX.1AI生成韩系氛围感写真_高级感大片_2074746850103619586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2074746850103619586.json
hash: 7c3c6c59215b52c1
coverage: 0.826087
learned_at: 2026-10-23 10:54:02
nodes: [SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Image Comparer (rgthree), ImageScaleBy, SaveImage, ConditioningZeroOut, VAEDecode, CLIPTextEncodeFlux, RHHiddenNodes, Lora Loader, Lora Loader, EmptyLatentImage, DualCLIPLoader, UNETLoader, Note, PrimitiveFloat, PrimitiveFloat, Lora Loader, RHHiddenNodes, VAELoader, SaveImage, RH_Translator]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1920, "width": 1080}
---

# 图片生成/图生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2074746850103619586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2074746850103619586.json`

## 结构

**生成流程**：Model → Condition → Latent → Decode → Process → Output → Other

**节点**（23 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `SaveImage`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `CLIPTextEncodeFlux` ★核心
- `RHHiddenNodes`
- `Lora Loader`
- `Lora Loader`
- `EmptyLatentImage` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `Note`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `Lora Loader`
- `RHHiddenNodes`
- `VAELoader`
- `SaveImage`
- `RH_Translator`

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`SaveImage`、`ConditioningZeroOut`、`VAEDecode`、`CLIPTextEncodeFlux`、`RHHiddenNodes`、`Lora Loader`、`EmptyLatentImage`、`DualCLIPLoader`、`UNETLoader`、`VAELoader`、`RH_Translator`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、EmptyLatentImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler
