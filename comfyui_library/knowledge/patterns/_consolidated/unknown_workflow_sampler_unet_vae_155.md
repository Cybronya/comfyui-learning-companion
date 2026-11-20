---
name: unknown_workflow_sampler_unet_vae_155
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.913
common_nodes: [Anything Everywhere3, CLIPLoader, CR Text, Flux2Scheduler, GrowMaskWithBlur, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Flux.2 Klein 9B 局部重绘+换头换脸+更换服装+万能图像编辑+极速版_2023278303158738945.json, 平台全量/FLUX.2-Klein 9B 局部重绘 换头换脸 更换服装 万能图像编辑 极速版_2015613529612619777.json, 平台全量/FLUX2-klein 局部重绘 人物模特换脸 换装 万能迁移_2028284451557482498.json, 平台全量/FLUX2-klein局部重绘_2013137002941648897.json, 平台全量/FLUX2-klein无瑕图像扩展_2013643647295688705.json, 平台全量/Flux2-Klein 电商产品更换背景 人物模特换场景  产品 插画 动漫卡通人物_2028280999972446209.json, 平台全量/Flux2-Klein更换背景（不局限于产品，插画，人物）_2015983814044033025.json, 平台全量/局部重绘 换头换脸 更换服装 FLUX.2-Klein 9B  万能图像编辑 极速版_2020769671242326018.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_155

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux.2 Klein 9B 局部重绘+换头换脸+更换服装+万能图像编辑+极速版_2023278303158738945.json、平台全量/FLUX.2-Klein 9B 局部重绘 换头换脸 更换服装 万能图像编辑 极速版_2015613529612619777.json、平台全量/FLUX2-klein 局部重绘 人物模特换脸 换装 万能迁移_2028284451557482498.json、平台全量/FLUX2-klein局部重绘_2013137002941648897.json、平台全量/FLUX2-klein无瑕图像扩展_2013643647295688705.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CR Text`
- `Flux2Scheduler`
- `GrowMaskWithBlur`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `CLIPTextEncode` —— 6/8 个有
- `DifferentialDiffusion` —— 6/8 个有
- `ImageAndMaskPreview` —— 6/8 个有
- `InpaintModelConditioning` —— 6/8 个有
- `VAEEncode` —— 6/8 个有
- `CFGGuider` —— 5/8 个有
- `KOOK_SaveJPGImage` —— 5/8 个有
- `Mask Fill Holes` —— 5/8 个有
- `BasicGuider` —— 3/8 个有
- `FluxGuidance` —— 3/8 个有
- `ImagePadForOutpaint` —— 3/8 个有
- `ImitationHueNode` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `CR Text Concatenate` —— 2/8 个有
- `DeepTranslatorTextNode` —— 2/8 个有
- `MaskPreview+` —— 2/8 个有
- `PainterFluxImageEdit` —— 2/8 个有
- `Qwen3_VQA` —— 2/8 个有
- `SAM3Segment` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `RMBG` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
