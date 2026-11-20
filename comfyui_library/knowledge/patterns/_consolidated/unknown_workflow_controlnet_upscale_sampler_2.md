---
name: unknown_workflow_controlnet_upscale_sampler_2
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.81325
common_nodes: [AILab_QwenVL, AIO_Preprocessor, BasicScheduler, CLIPLoader, CLIPTextEncode, DetailDaemonSamplerNode, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixelsX, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, SamplerCustom, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SplitSigmas, UNETLoader, VAEDecode, VAEEncode, VAELoader, ZImageFunControlnet, easy cleanGpuUsed, easy imageSizeBySide, easy positive, easy promptConcat]
problems: []
missing: []
members: [图片生成/图生图/Z-Image-电商专用洗图_2059467669958647810.json, 图片生成/图生图/z-image-turbo-服装模特图-洗图_2059176245241409538.json, 图片生成/文生图/z-image-完美文生图-婚纱摄影-批量出图_2033415203097939970.json, 图片生成/文生图/z-image-完美文生图-私房摄影-批量出图_2036973821743337474.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Z-Image-电商专用洗图_2059467669958647810.json、图片生成/图生图/z-image-turbo-服装模特图-洗图_2059176245241409538.json、图片生成/文生图/z-image-完美文生图-婚纱摄影-批量出图_2033415203097939970.json、图片生成/文生图/z-image-完美文生图-私房摄影-批量出图_2036973821743337474.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `AIO_Preprocessor`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `DetailDaemonSamplerNode`
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixelsX`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `SamplerCustom`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `ZImageFunControlnet`
- `easy cleanGpuUsed`
- `easy imageSizeBySide`
- `easy positive`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `JDCN_StringToList` —— 2/4 个有
- `LatentColorMatchSimple` —— 2/4 个有
- `LayerUtility: ColorImage V2` —— 2/4 个有
- `LayerUtility: ImageBlend` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `ProcessString` —— 2/4 个有
- `RepeatLatentBatch` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `取色器_孤海` —— 2/4 个有
- `easy ifElse` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
