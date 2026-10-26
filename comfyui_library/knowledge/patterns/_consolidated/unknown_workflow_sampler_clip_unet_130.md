---
name: unknown_workflow_sampler_clip_unet_130
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.937556
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux--Klein--产品精修高清放大_2054921194004074498.json, 图片生成/图生图/Flux-Klein-产品精修-高清放大_2055848149163495425.json, 图片生成/图生图/Flux-Klein产品精修高清放大（爆显用plus模式）_2055471694915096578.json, 图片生成/图生图/Flux2-Klein-9B-人物换头_2012775113048989698.json, 图片生成/图生图/Flux2-Klein-9B-材质替换_2012772305113456641.json, 图片生成/图生图/Flux2-Klein-9B衣服迁移(偏色修正版)_2012342283487678465.json, 图片生成/图生图/PS高阶一键换脸_1903274591681421314.json, 图片生成/图生图/产品图与美妆精修_2053373828482519041.json, 图片生成/图生图/老孙AI 产品精修V3_2090318488920477697.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_130

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux--Klein--产品精修高清放大_2054921194004074498.json、图片生成/图生图/Flux-Klein-产品精修-高清放大_2055848149163495425.json、图片生成/图生图/Flux-Klein产品精修高清放大（爆显用plus模式）_2055471694915096578.json、图片生成/图生图/Flux2-Klein-9B-人物换头_2012775113048989698.json、图片生成/图生图/Flux2-Klein-9B-材质替换_2012772305113456641.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
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
- `FluxKontextImageScale` —— 5/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `DF_Integer` —— 4/9 个有
- `JWInteger` —— 4/9 个有
- `SeedVR2` —— 4/9 个有
- `SeedVR2BlockSwap` —— 4/9 个有
- `SimpleMath+` —— 4/9 个有
- `easy cleanGpuUsed` —— 4/9 个有
- `easy imageScaleDownToSize` —— 4/9 个有
- `AILab_QwenVL` —— 3/9 个有
- `SeedVR2ExtraArgs` —— 3/9 个有
- `YC Color Match` —— 3/9 个有
- `CR Text` —— 1/9 个有
- `ImageResize+` —— 1/9 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `SeedVR2LoadDiTModel` —— 1/9 个有
- `SeedVR2LoadVAEModel` —— 1/9 个有
- `SeedVR2VideoUpscaler` —— 1/9 个有
- `TTP_Image_Assy` —— 1/9 个有
- `TTP_Image_Tile_Batch` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
