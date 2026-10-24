---
name: unknown_workflow_sampler_clip_unet_27
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.790957
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ComfyUI电商换装：男女装一套流搞定，全节点注释喂饭级教学_2062768387176095745.json, 图片生成/图生图/DG_Flux2-klein单图+双图编辑工作流_2012101006372376578.json, 图片生成/图生图/F.2-klein-9B一键转漫画_2016138424301916161.json, 图片生成/图生图/F.2Klein9b专业证件照人像精修_2054409238532894721.json, 图片生成/图生图/F.2Klein9b证件照AI生成专业证件照_2054205043909382146.json, 图片生成/图生图/F.2Klein9b证件照AI生成专业证件照_2054363365077725186.json, 图片生成/图生图/F.2Klein9b证件照AI生成专业证件照_2057662197085589505.json, 图片生成/图生图/F2-klein-9B 产品_人物 换背景 光源一致 图片换背景_2092964367598968834.json, 图片生成/图生图/F2-klein-9B 产品_人物 换背景 光源一致_2083502820053049346.json, 图片生成/图生图/F2-klein-9B 产品_人物 换背景 光源一致_2083532831615176705.json, 图片生成/图生图/F2-klein-9B_产品_人物_换背景_光源一致_图片换背景_2093514978438508546.json, 图片生成/图生图/F2-klein-9B万物溶图_2027384708258078721.json, 图片生成/图生图/F2-klein-9B万物迁移2.0_2025429156120498178.json, 图片生成/图生图/F2-klein-9B万物迁移2.0_2057717802529812481.json, 图片生成/图生图/F2-klein-9B产品精修2.0_2027658019277905921.json, 图片生成/图生图/F2-klein-9B换背景_2028738168064839682.json, 图片生成/图生图/F2k_9B_移除文字+高清放大_2019016429546246145.json, 图片生成/图生图/Flux2 Klein LoRA效果测试_2033882764415602689.json, 图片生成/图生图/Flux2-klein-提取服装_2023254759578279937.json, 图片生成/图生图/f2_klein_9B_真人转动漫_2025771070518726658.json, 图片生成/图生图/f2_klein_9b_胸部放大器2.0_2021777540951580673.json, 图片生成/图生图/f2k-9B-产品精修_2020706793617362946.json, 图片生成/图生图/产品精修_2072889271643623426.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_27

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/ComfyUI电商换装：男女装一套流搞定，全节点注释喂饭级教学_2062768387176095745.json、图片生成/图生图/DG_Flux2-klein单图+双图编辑工作流_2012101006372376578.json、图片生成/图生图/F.2-klein-9B一键转漫画_2016138424301916161.json、图片生成/图生图/F.2Klein9b专业证件照人像精修_2054409238532894721.json、图片生成/图生图/F.2Klein9b证件照AI生成专业证件照_2054205043909382146.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 23 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `ConditioningZeroOut` —— 22/23 个有
- `EmptyFlux2LatentImage` —— 22/23 个有
- `CR Text` —— 21/23 个有
- `LoraLoaderModelOnly` —— 21/23 个有
- `Flux2Scheduler` —— 19/23 个有
- `GetImageSize` —— 18/23 个有
- `GetNode` —— 17/23 个有
- `SetNode` —— 17/23 个有
- `LayerUtility: ImageReel` —— 16/23 个有
- `LayerUtility: ImageReelComposit` —— 16/23 个有
- `Image Comparer (rgthree)` —— 15/23 个有
- `easy imageScaleDownToSize` —— 15/23 个有
- `Fast Groups Bypasser (rgthree)` —— 14/23 个有
- `ImageScaleToTotalPixels` —— 8/23 个有
- `easy cleanGpuUsed` —— 8/23 个有
- `Int` —— 7/23 个有
- `SeedVR2LoadDiTModel` —— 6/23 个有
- `SeedVR2LoadVAEModel` —— 6/23 个有
- `SeedVR2VideoUpscaler` —— 6/23 个有
- `JWInteger` —— 5/23 个有
- `BasicScheduler` —— 4/23 个有
- `easy promptConcat` —— 4/23 个有
- `easy showAnything` —— 4/23 个有
- `CR Index` —— 1/23 个有
- `JWFloat` —— 1/23 个有
- `Text` —— 1/23 个有
- `easy anythingIndexSwitch` —— 1/23 个有
- `easy imageSize` —— 1/23 个有
- `easy int` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
