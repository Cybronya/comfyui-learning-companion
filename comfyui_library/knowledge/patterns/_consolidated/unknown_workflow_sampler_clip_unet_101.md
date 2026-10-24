---
name: unknown_workflow_sampler_clip_unet_101
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8596
common_nodes: [CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 klein9b自动溶图重新打光_2058190559239565313.json, 图片生成/图生图/Flux2-Klein _单图编辑_2041331757047357442.json, 图片生成/图生图/Flux2-Klein 单图编辑版_2015381602594983938.json, 图片生成/图生图/Flux2-Klein 多图编辑版_2015361031995924482.json, 图片生成/图生图/Flux2-Klein-9B 真人转2.5D插画风格_2049825292977487873.json, 图片生成/图生图/Flux2-Klein-9B-写实细节-完美洗图_2035439475463032834.json, 图片生成/图生图/Flux2-klein局部重绘_扩图_移除_2015367193973760002.json, 图片生成/图生图/Flux2-klein局部重绘_扩图_移除_2028122775256305666.json, 图片生成/图生图/Flux2-klein局部重绘_扩图_移除_2054741458850205697.json, 图片生成/图生图/Flux2-klein局部重绘_扩图_移除_2054837030131126273.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_101

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Flux2 klein9b自动溶图重新打光_2058190559239565313.json、图片生成/图生图/Flux2-Klein _单图编辑_2041331757047357442.json、图片生成/图生图/Flux2-Klein 单图编辑版_2015381602594983938.json、图片生成/图生图/Flux2-Klein 多图编辑版_2015361031995924482.json、图片生成/图生图/Flux2-Klein-9B 真人转2.5D插画风格_2049825292977487873.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `CFGGuider` —— 9/10 个有
- `ConditioningZeroOut` —— 9/10 个有
- `EmptyFlux2LatentImage` —— 9/10 个有
- `PreviewImage` —— 8/10 个有
- `GetImageSize` —— 7/10 个有
- `Image Comparer (rgthree)` —— 7/10 个有
- `ColorMatch` —— 6/10 个有
- `ImageConcanate` —— 5/10 个有
- `Int` —— 5/10 个有
- `DrawMaskOnImage` —— 4/10 个有
- `GrowMaskWithBlur` —— 4/10 个有
- `ImagePadForOutpaint` —— 4/10 个有
- `ImageMaskSwitch` —— 3/10 个有
- `ImpactSwitch` —— 3/10 个有
- `LayerUtility: ImageReel` —— 3/10 个有
- `LayerUtility: ImageReelComposit` —— 3/10 个有
- `LoraLoaderModelOnly` —— 3/10 个有
- `MultiTextConcatenate` —— 2/10 个有
- `MuyeTextEditOutput` —— 2/10 个有
- `PreviewAny` —— 2/10 个有
- `RH_Captioner_Pro` —— 2/10 个有
- `BasicGuider` —— 1/10 个有
- `TT_img_enc_v2` —— 1/10 个有
- `TwoWaySwitch` —— 1/10 个有
- `easy positive` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
