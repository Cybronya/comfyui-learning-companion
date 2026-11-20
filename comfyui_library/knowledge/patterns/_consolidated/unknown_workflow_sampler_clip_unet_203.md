---
name: unknown_workflow_sampler_clip_unet_203
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9005
common_nodes: [CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux2图像修复_2064329697353359361.json, 图片生成/文生图/flux2基础_文生图_图生图_迁移_1993562025060139010.json, 图片生成/文生图/image_flux2_1999252927225229314.json, 图片生成/文生图/动作编辑器应用系列之一__FLUX-2-klein-9b_文生图_2022474573257641985.json, 平台全量/Flux2 三图编辑_1993517500014985218.json, 平台全量/flux.2图像编辑_1995497834998857729.json, 平台全量/一键生成电影九宫格分镜_2039964366426083329.json, 视频生成/图生视频/Flux2单图+双图编辑工作流_2014254176355753986.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_203

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/flux2图像修复_2064329697353359361.json、图片生成/文生图/flux2基础_文生图_图生图_迁移_1993562025060139010.json、图片生成/文生图/image_flux2_1999252927225229314.json、图片生成/文生图/动作编辑器应用系列之一__FLUX-2-klein-9b_文生图_2022474573257641985.json、平台全量/Flux2 三图编辑_1993517500014985218.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `EmptyFlux2LatentImage` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 7/8 个有
- `BasicGuider` —— 6/8 个有
- `FluxGuidance` —— 6/8 个有
- `GetImageSize` —— 3/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `CFGGuider` —— 2/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `PiDTextPrompt` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `image_scale_pixel_v2` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
