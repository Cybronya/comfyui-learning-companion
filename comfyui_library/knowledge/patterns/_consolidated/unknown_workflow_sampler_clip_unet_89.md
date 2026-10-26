---
name: unknown_workflow_sampler_clip_unet_89
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.946273
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/003.FLUX.2智能综合005.提示词优化单图编辑_2035249536402202626.json, 图片生成/图生图/003.FLUX.2智能综合010.三图融合_2035260057725706241.json, 图片生成/图生图/FLUX 2 DEV 多图编辑_1993665906230362113.json, 图片生成/图生图/FLUX.2-单图编辑_1993754112938409986.json, 图片生成/图生图/FLUX2单图编辑版_1993603323286798338.json, 图片生成/图生图/FLUX2多图编辑版_1993599745228734465.json, 图片生成/图生图/FLux2-换装改图_2082637929058488322.json, 图片生成/图生图/FLux2-换装改图_2082648770222841857.json, 图片生成/图生图/🍕最强开源 FLUX2系列之单图编辑版_1993557673455140865.json, 图片生成/图生图/🍕最强开源 FLUX2系列之多图编辑版_1993566728900771842.json, 数字人/数字人/FLUX2多图编辑版-阿浩_2026896253828734978.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_89

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/003.FLUX.2智能综合005.提示词优化单图编辑_2035249536402202626.json、图片生成/图生图/003.FLUX.2智能综合010.三图融合_2035260057725706241.json、图片生成/图生图/FLUX 2 DEV 多图编辑_1993665906230362113.json、图片生成/图生图/FLUX.2-单图编辑_1993754112938409986.json、图片生成/图生图/FLUX2单图编辑版_1993603323286798338.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
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
- `ImageScaleToTotalPixels` —— 8/11 个有
- `ImpactInt` —— 8/11 个有
- `CR Text` —— 5/11 个有
- `DeepTranslatorTextNode` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/11 个有
- `Image Comparer (rgthree)` —— 3/11 个有
- `Note Plus (mtb)` —— 2/11 个有
- `TextInput_` —— 2/11 个有
- `ImageConcanate` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `LoraLoaderModelOnly` —— 1/11 个有
- `Qwen3VL_Chat` —— 1/11 个有
- `String` —— 1/11 个有
- `VAEDecodeTiled` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
