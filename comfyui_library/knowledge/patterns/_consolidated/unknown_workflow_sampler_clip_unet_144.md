---
name: unknown_workflow_sampler_clip_unet_144
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.876375
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX-Klein版 电商产品可控构图换背景+融图_2013853557090426881.json, 图片生成/图生图/FLUX2 KLEIN True-V2底模升级-单图编辑_2049082691332612097.json, 图片生成/图生图/FLUX2 Klein 多图编辑工作流_2091477521320734722.json, 图片生成/图生图/FLUX2+KLEIN+True-V2-单图编辑_2050236956377923586.json, 图片生成/图生图/Flux2 Klein Multi-Image Edit_2018198139378864129.json, 图片生成/图生图/Flux2 Klein 编辑多合一版  多图保持人物一致性丨产品光影融合_2022519193781936129.json, 图片生成/图生图/Klein 编辑多合一版  多图保持人物一致性丨产品光影融合 林耀_2014020601354133505.json, 图片生成/文生图/Klein 编辑多合一版_2073302428295983105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_144

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FLUX-Klein版 电商产品可控构图换背景+融图_2013853557090426881.json、图片生成/图生图/FLUX2 KLEIN True-V2底模升级-单图编辑_2049082691332612097.json、图片生成/图生图/FLUX2 Klein 多图编辑工作流_2091477521320734722.json、图片生成/图生图/FLUX2+KLEIN+True-V2-单图编辑_2050236956377923586.json、图片生成/图生图/Flux2 Klein Multi-Image Edit_2018198139378864129.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `GetImageSize` —— 5/8 个有
- `ImageScaleToTotalPixels` —— 5/8 个有
- `AIO_Preprocessor` —— 4/8 个有
- `FastCanvas` —— 4/8 个有
- `FastCanvasTool` —— 4/8 个有
- `LayerMask: BiRefNetUltraV2` —— 4/8 个有
- `LayerMask: LoadBiRefNetModelV2` —— 4/8 个有
- `LayerUtility: PurgeVRAM` —— 4/8 个有
- `SeedVR2LoadDiTModel` —— 4/8 个有
- `SeedVR2LoadVAEModel` —— 4/8 个有
- `SeedVR2VideoUpscaler` —— 4/8 个有
- `AILab_QwenVL` —— 3/8 个有
- `CR Prompt List` —— 3/8 个有
- `ColorMatch` —— 3/8 个有
- `DrawMaskOnImage` —— 3/8 个有
- `ImagePadForOutpaint` —— 3/8 个有
- `PlaySound|pysssss` —— 3/8 个有
- `PreviewImage` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `Image Padding` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `LoaderGGUF` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
