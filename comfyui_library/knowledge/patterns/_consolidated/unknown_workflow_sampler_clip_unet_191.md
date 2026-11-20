---
name: unknown_workflow_sampler_clip_unet_191
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9475
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1_2023028109125099521.json, 平台全量/Flux-2-Klein-9B 多图编辑 写实自然 保持人物一致 王炸登场！_2015348302610440194.json, 平台全量/Flux-2-Klein-9B+多图编辑 电商产品展示+写实自然+保持人物一致+王炸登场！_2021417987793752066.json, 平台全量/Flux2 Klein 单图编辑9B版_2013622163370151938.json, 平台全量/flux.2 klein 只转人物，不转背景，控制人物角度_2011896495527694337.json, 平台全量/双图编辑版（全能编辑模型 VS flux.2klein）_2019336417431789570.json, 平台全量/增强现实Flux2 Klein_2028749023439495170.json, 平台全量/室内设计风格迁移_2082479153508605953.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_191

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1_2023028109125099521.json、平台全量/Flux-2-Klein-9B 多图编辑 写实自然 保持人物一致 王炸登场！_2015348302610440194.json、平台全量/Flux-2-Klein-9B+多图编辑 电商产品展示+写实自然+保持人物一致+王炸登场！_2021417987793752066.json、平台全量/Flux2 Klein 单图编辑9B版_2013622163370151938.json、平台全量/flux.2 klein 只转人物，不转背景，控制人物角度_2011896495527694337.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
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
- `CR Text` —— 7/8 个有
- `GetImageSize` —— 7/8 个有
- `ConditioningZeroOut` —— 6/8 个有
- `ImageScaleToTotalPixels` —— 6/8 个有
- `LayerUtility: ImageReel` —— 6/8 个有
- `LayerUtility: ImageReelComposit` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `ImageResize+` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `PrimitiveInt` —— 2/8 个有
- `QwenMultiangleCameraNode` —— 2/8 个有
- `RH_Captioner` —— 2/8 个有
- `RH_Nano_Banana2_Image2Image` —— 2/8 个有
- `StringFunction|pysssss` —— 2/8 个有
- `Get Image Size` —— 1/8 个有
- `ImageStitch` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
