---
name: unknown_workflow_lora_sampler_clip_126
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.77675
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize+, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, PlaySound|pysssss, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2-Klein  强化拓图 v1_2064613123247656962.json, 图片生成/图生图/Flux2-Klein_强化局部重绘_2064609756781826049.json, 图片生成/图生图/Klein 完全体 _ 三参考图全能王 _ 卡通转真人 _ 4K 修复 _ 扩图 _ 无痕换脸_2069031336664461314.json, 图片生成/图生图/Klein_完全体_三参考图全能王_卡通转真人_4K修复_扩图_无痕换脸_2068567815745007618.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_126

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein  强化拓图 v1_2064613123247656962.json、图片生成/图生图/Flux2-Klein_强化局部重绘_2064609756781826049.json、图片生成/图生图/Klein 完全体 _ 三参考图全能王 _ 卡通转真人 _ 4K 修复 _ 扩图 _ 无痕换脸_2069031336664461314.json、图片生成/图生图/Klein_完全体_三参考图全能王_卡通转真人_4K修复_扩图_无痕换脸_2068567815745007618.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize+`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKVCache` —— 2/4 个有
- `ImageColorMatch+` —— 2/4 个有
- `ImageScaleToMaxDimension` —— 2/4 个有
- `LayerUtility: ImageReel` —— 2/4 个有
- `LayerUtility: ImageReelComposit` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `easy int` —— 2/4 个有
- `DrawMaskOnImage` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImagePadForOutpaint` —— 1/4 个有
- `InpaintCropImproved` —— 1/4 个有
- `InpaintStitchImproved` —— 1/4 个有
- `easy imageCropFromMask` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
