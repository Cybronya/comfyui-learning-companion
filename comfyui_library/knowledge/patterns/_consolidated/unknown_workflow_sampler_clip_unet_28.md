---
name: unknown_workflow_sampler_clip_unet_28
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.893783
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX 2 一键洗图 去水印 提升画面质感 调色融图_1994453323245817857.json, 图片生成/图生图/FLUX-2-klein-4B_精准换头LoRA_2012004120126824449.json, 图片生成/图生图/FLUX-2-klein-4b-fp8_4步9秒出图工作流_2007647082005405697.json, 图片生成/图生图/FLUX-2-klein-4b-fp8_卡通LoRA_2014135720021069826.json, 图片生成/图生图/FLUX-2-klein-9B_人物关键点图LoRA动作设计_2017766958040616962.json, 图片生成/图生图/FLUX.2 单图修改来了！支持中文改图！保持一致性_1993497390741209090.json, 图片生成/图生图/FLUX.2 双图融合_1993494554741587970.json, 图片生成/图生图/FLUX.2 最新改图模型！支持中文改图！保持一致性！_1993507040419053570.json, 图片生成/图生图/FLUX2-双图融合_1994060636019769346.json, 图片生成/图生图/Flux Klein 9b FP8 多图参考 极简工作流_2015303258776014849.json, 图片生成/图生图/Flux Klein 9b FP8 多角度参考图生成 极简工作流_2015300779183181825.json, 图片生成/图生图/Flux Klein 9b fp8 单图编辑_2012792860650774529.json, 图片生成/图生图/Flux2 Dev 单图编辑_1999318601045770242.json, 图片生成/图生图/Flux2 Dev 双图编辑_1999317364070023170.json, 图片生成/图生图/Flux2 单图编辑加速版V2（加强版）_1993502440953675777.json, 图片生成/图生图/Flux2 双图编辑加速版V1（增强版）_1993501397798895618.json, 图片生成/图生图/Flux2+电商产品换背景_1993605861067210753.json, 图片生成/图生图/Flux2+电商产品换背景_1996101439929925633.json, 图片生成/图生图/Flux2_FP8 工作流 5080可以跑_1994454939474726914.json, 图片生成/图生图/Flux2一键换脸_1993565462101508097.json, 图片生成/图生图/Flux2可控视角多角度控制V1_2006048912230064130.json, 图片生成/图生图/flux2 dev单图编辑【全能图片V1平替】_1999825664515731458.json, 图片生成/图生图/（8步加速版）Flux2 Turbo单图编辑加速版V1_2006022078891511809.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_28

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/FLUX 2 一键洗图 去水印 提升画面质感 调色融图_1994453323245817857.json、图片生成/图生图/FLUX-2-klein-4B_精准换头LoRA_2012004120126824449.json、图片生成/图生图/FLUX-2-klein-4b-fp8_4步9秒出图工作流_2007647082005405697.json、图片生成/图生图/FLUX-2-klein-4b-fp8_卡通LoRA_2014135720021069826.json、图片生成/图生图/FLUX-2-klein-9B_人物关键点图LoRA动作设计_2017766958040616962.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
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
- `FluxGuidance` —— 20/23 个有
- `ImageScaleToTotalPixels` —— 20/23 个有
- `ModelPatchTorchSettings` —— 14/23 个有
- `PathchSageAttentionKJ` —— 14/23 个有
- `CR Prompt Text` —— 9/23 个有
- `EasyCache` —— 7/23 个有
- `PrimitiveInt` —— 7/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/23 个有
- `LoraLoaderModelOnly` —— 5/23 个有
- `UnetLoaderGGUF` —— 4/23 个有
- `GetImageSize+` —— 3/23 个有
- `PreviewImage` —— 3/23 个有
- `Image Comparer (rgthree)` —— 2/23 个有
- `INTConstant` —— 1/23 个有
- `ImageConcatMulti` —— 1/23 个有
- `LayerMask: PersonMaskUltra V2` —— 1/23 个有
- `MaskColorize` —— 1/23 个有
- `QwenMultiangleCameraNode` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
