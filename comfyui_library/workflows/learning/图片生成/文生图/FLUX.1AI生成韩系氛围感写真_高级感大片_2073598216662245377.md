---
key: 图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2073598216662245377.json
name: FLUX.1AI生成韩系氛围感写真_高级感大片_2073598216662245377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2073598216662245377.json
hash: aacb6d9e05a2c7aa
coverage: 0.76
learned_at: 2026-10-20 00:01:08
nodes: [SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), ImageScaleBy, SaveImage, ConditioningZeroOut, VAEDecode, CLIPTextEncodeFlux, RHHiddenNodes, Lora Loader, Lora Loader, EmptyLatentImage, DualCLIPLoader, UNETLoader, Note, Lora Loader, RHHiddenNodes, VAELoader, RH_Translator, PrimitiveFloat, PrimitiveFloat, MarkdownNote, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1920, "width": 1080}
---

# 图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2073598216662245377.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.1AI生成韩系氛围感写真_高级感大片_2073598216662245377.json`

## 结构

**生成流程**：Model → Condition → Latent → Decode → Process → Output → Other

**节点**（25 个）：
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
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
- `Lora Loader`
- `RHHiddenNodes`
- `VAELoader`
- `RH_Translator`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（19/25）

**有卡**：`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`ImageScaleBy`、`ConditioningZeroOut`、`VAEDecode`、`CLIPTextEncodeFlux`、`RHHiddenNodes`、`Lora Loader`、`EmptyLatentImage`、`DualCLIPLoader`、`UNETLoader`、`VAELoader`、`RH_Translator`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、EmptyLatentImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler
