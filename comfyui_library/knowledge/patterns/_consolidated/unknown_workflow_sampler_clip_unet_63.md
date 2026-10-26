---
name: unknown_workflow_sampler_clip_unet_63
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.872923
common_nodes: [CLIPLoader, CLIPTextEncode, Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 klein9b自动溶图重新打光_2058190559239565313.json, 图片生成/图生图/Flux2+Klein控油高清+真实系皮肤质感_2057795926776958978.json, 图片生成/图生图/Flux2+Klein电商产品精修_2052968122042331137.json, 图片生成/图生图/Flux2+Klein电商产品精修_2059467199106084865.json, 图片生成/图生图/Flux2+Klein电商产品精修_2064548916141576194.json, 图片生成/图生图/Flux2+Klein电商产品精修_2064556061675311106.json, 图片生成/图生图/Flux2+Klein电商产品精修_2093243077682089986.json, 图片生成/图生图/Flux2+Klein电商产品精修_2093514490821300225.json, 图片生成/图生图/Flux2-Klein _单图编辑_2041331757047357442.json, 图片生成/图生图/Flux2-Klein-9B 真人转2.5D插画风格_2049825292977487873.json, 图片生成/图生图/Flux2-Klein-9B-写实细节-完美洗图_2035439475463032834.json, 图片生成/图生图/Flux2-Klein9b超级皮肤质感_2022873403333545985.json, 图片生成/图生图/flux2klein9b自动溶图重新打光_2046941528681095169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_63

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Flux2 klein9b自动溶图重新打光_2058190559239565313.json、图片生成/图生图/Flux2+Klein控油高清+真实系皮肤质感_2057795926776958978.json、图片生成/图生图/Flux2+Klein电商产品精修_2052968122042331137.json、图片生成/图生图/Flux2+Klein电商产品精修_2059467199106084865.json、图片生成/图生图/Flux2+Klein电商产品精修_2064548916141576194.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
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
- `LoraLoaderModelOnly` —— 12/13 个有
- `CFGGuider` —— 11/13 个有
- `ConditioningZeroOut` —— 11/13 个有
- `EmptyFlux2LatentImage` —— 11/13 个有
- `PreviewImage` —— 9/13 个有
- `CR Prompt Text` —— 8/13 个有
- `Int` —— 6/13 个有
- `BasicGuider` —— 2/13 个有
- `GetImageSize` —— 2/13 个有
- `ImageConcanate` —— 2/13 个有
- `MultiTextConcatenate` —— 2/13 个有
- `MuyeTextEditOutput` —— 2/13 个有
- `PreviewAny` —— 2/13 个有
- `RH_Captioner_Pro` —— 2/13 个有
- `easy positive` —— 2/13 个有
- `TT_img_enc_v2` —— 1/13 个有
- `TwoWaySwitch` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
