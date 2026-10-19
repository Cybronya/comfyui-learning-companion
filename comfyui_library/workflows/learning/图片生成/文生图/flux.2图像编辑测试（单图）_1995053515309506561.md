---
key: 图片生成/文生图/flux.2图像编辑测试（单图）_1995053515309506561.json
name: flux.2图像编辑测试（单图）_1995053515309506561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux.2图像编辑测试（单图）_1995053515309506561.json
hash: 05b7ebc1b45dae3e
coverage: 0.884615
learned_at: 2026-10-19 21:33:11
nodes: [KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, FluxGuidance, Flux2Scheduler, EmptyFlux2LatentImage, Note, RandomNoise, VAELoader, UnetLoaderGGUF, ModelPatchTorchSettings, CLIPLoader, LoadImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, PathchSageAttentionKJ, ImageScaleToTotalPixels, PrimitiveNode, PrimitiveNode, VAEDecode, CLIPTextEncode, KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, FluxGuidance, Flux2Scheduler, EmptyFlux2LatentImage, Note, RandomNoise, VAELoader, UnetLoaderGGUF, ModelPatchTorchSettings, CLIPLoader, LoadImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, PathchSageAttentionKJ, ImageScaleToTotalPixels, PrimitiveNode, PrimitiveNode, VAEDecode, KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, FluxGuidance, EmptyFlux2LatentImage, Note, RandomNoise, VAELoader, UnetLoaderGGUF, ModelPatchTorchSettings, CLIPLoader, LoadImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, PathchSageAttentionKJ, ImageScaleToTotalPixels, PrimitiveNode, PrimitiveNode, VAEDecode, KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, FluxGuidance, Flux2Scheduler, EmptyFlux2LatentImage, Note, RandomNoise, VAELoader, UnetLoaderGGUF, ModelPatchTorchSettings, CLIPLoader, LoadImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, PathchSageAttentionKJ, ImageScaleToTotalPixels, PrimitiveNode, PrimitiveNode, VAEDecode, KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, FluxGuidance, Flux2Scheduler, EmptyFlux2LatentImage, Note, RandomNoise, VAELoader, UnetLoaderGGUF, ModelPatchTorchSettings, CLIPLoader, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, PathchSageAttentionKJ, ImageScaleToTotalPixels, PrimitiveNode, PrimitiveNode, VAEDecode, KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, FluxGuidance, Flux2Scheduler, EmptyFlux2LatentImage, Note, RandomNoise, VAELoader, UnetLoaderGGUF, ModelPatchTorchSettings, CLIPLoader, LoadImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, PathchSageAttentionKJ, ImageScaleToTotalPixels, PrimitiveNode, PrimitiveNode, VAEDecode, KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, FluxGuidance, EmptyFlux2LatentImage, Note, RandomNoise, VAELoader, UnetLoaderGGUF, ModelPatchTorchSettings, CLIPLoader, LoadImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, PathchSageAttentionKJ, ImageScaleToTotalPixels, PrimitiveNode, PrimitiveNode, VAEDecode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, LoadImage, CLIPTextEncode, CLIPTextEncode, LoadImage, KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, FluxGuidance, Flux2Scheduler, EmptyFlux2LatentImage, Note, RandomNoise, VAELoader, UnetLoaderGGUF, ModelPatchTorchSettings, CLIPLoader, LoadImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, PathchSageAttentionKJ, ImageScaleToTotalPixels, PrimitiveNode, PrimitiveNode, VAEDecode, CLIPTextEncode, CLIPTextEncode, KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, FluxGuidance, Flux2Scheduler, EmptyFlux2LatentImage, Note, RandomNoise, VAELoader, UnetLoaderGGUF, ModelPatchTorchSettings, CLIPLoader, LoadImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, PathchSageAttentionKJ, ImageScaleToTotalPixels, PrimitiveNode, PrimitiveNode, VAEDecode, CLIPTextEncode, LoadImage, LoadImage, LoadImage, LoadImage, SaveImage, SaveImage, Flux2Scheduler, SaveImage, SaveImage, LoadImage, SaveImage, SaveImage, LoadImage, LoadImage, SaveImage, KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, FluxGuidance, EmptyFlux2LatentImage, Note, RandomNoise, VAELoader, UnetLoaderGGUF, ModelPatchTorchSettings, CLIPLoader, LoadImage, SamplerCustomAdvanced, VAEEncode, ReferenceLatent, PathchSageAttentionKJ, ImageScaleToTotalPixels, PrimitiveNode, PrimitiveNode, Flux2Scheduler, VAEDecode, CLIPTextEncode, ImageScaleToTotalPixels, LoadImage, SaveImage, SaveImage, Flux2Scheduler, LoadImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/文生图/flux.2图像编辑测试（单图）_1995053515309506561.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux.2图像编辑测试（单图）_1995053515309506561.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（260 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `Note`
- `RandomNoise`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `PathchSageAttentionKJ`
- `ImageScaleToTotalPixels`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `Note`
- `RandomNoise`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `PathchSageAttentionKJ`
- `ImageScaleToTotalPixels`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `EmptyFlux2LatentImage`
- `Note`
- `RandomNoise`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `PathchSageAttentionKJ`
- `ImageScaleToTotalPixels`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `Note`
- `RandomNoise`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `PathchSageAttentionKJ`
- `ImageScaleToTotalPixels`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `Note`
- `RandomNoise`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `PathchSageAttentionKJ`
- `ImageScaleToTotalPixels`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `Note`
- `RandomNoise`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `PathchSageAttentionKJ`
- `ImageScaleToTotalPixels`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `EmptyFlux2LatentImage`
- `Note`
- `RandomNoise`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `PathchSageAttentionKJ`
- `ImageScaleToTotalPixels`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `Note`
- `RandomNoise`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `PathchSageAttentionKJ`
- `ImageScaleToTotalPixels`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `Note`
- `RandomNoise`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `PathchSageAttentionKJ`
- `ImageScaleToTotalPixels`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `Flux2Scheduler`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `EmptyFlux2LatentImage`
- `Note`
- `RandomNoise`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `ModelPatchTorchSettings`
- `CLIPLoader`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `PathchSageAttentionKJ`
- `ImageScaleToTotalPixels`
- `PrimitiveNode`
- `PrimitiveNode`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `Flux2Scheduler`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **88%**（230/260）

**有卡**：`KSamplerSelect`、`BasicGuider`、`ReferenceLatent`、`VAEEncode`、`FluxGuidance`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`RandomNoise`、`VAELoader`、`UnetLoaderGGUF`、`ModelPatchTorchSettings`、`CLIPLoader`、`LoadImage`、`SamplerCustomAdvanced`、`ImageScaleToTotalPixels`、`PathchSageAttentionKJ`、`VAEDecode`、`CLIPTextEncode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
