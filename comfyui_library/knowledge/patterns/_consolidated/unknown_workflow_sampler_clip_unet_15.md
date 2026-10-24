---
name: unknown_workflow_sampler_clip_unet_15
type: Unknown Workflow
frequency: 29
level: moderate
coverage: 0.897586
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/krea2 i2i 一键洗图 图生图+洗图工作流_2090754065042067457.json, 图片生成/图生图/krea2 i2i 一键洗图 图生图+洗图工作流_2104751982484484098.json, 图片生成/图生图/krea2 i2i 一键洗图 快速生图_2091873720318124033.json, 图片生成/图生图/krea2 i2i 一键洗图工作流 图生图_2096205084123287553.json, 图片生成/图生图/krea2 i2i 一键洗图工作流 图生图_2105994124833943553.json, 图片生成/图生图/krea2 i2i 一键洗图工作流 图生图_2106023301272399873.json, 图片生成/图生图/krea2 i2i 一键洗图工作流_2091857020520591361.json, 图片生成/图生图/krea2 i2i 图生图+洗图工作流_2083858292392153089.json, 图片生成/图生图/krea2 i2i 图生图+洗图工作流_2087522709961011202.json, 图片生成/图生图/krea2 i2i 图生图+洗图工作流_2089309377919545345.json, 图片生成/图生图/krea2 i2i 图生图+洗图工作流_2096201820833144834.json, 图片生成/图生图/krea2 turbo图生图_2070403435148693505.json, 图片生成/图生图/krea2 turbo图生图_2070410400897781762.json, 图片生成/图生图/krea2 turbo图生图_2082371403587866626.json, 图片生成/图生图/krea2 turbo图生图_2083452651290849282.json, 图片生成/图生图/krea2 turbo图生图洗图_2070372340764078082.json, 图片生成/图生图/krea2 turbo图生图洗图_2070424965035421697.json, 图片生成/图生图/krea2_i2i_图生图+洗图工作流_2088256007804903425.json, 图片生成/图生图/krea2自用图生图_2090088764180885505.json, 图片生成/图生图/krea视频洗图工作流_2075031802141564930.json, 图片生成/图生图/图生图+洗图=krea2 i2i！艾橘溪_2083189890023518210.json, 图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2100409782829150209.json, 图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2101262934214275074.json, 图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2108737708976852993.json, 图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2108741957932642306.json, 图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2112736624135196673.json, 图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2112738893312380929.json, 图片生成/文生图/krea turbo洗图+seedvr2高清放大_2070404592160043010.json, 数字人/数字人/高清放大洗图krea2 +SeedVR+放大+图生图 直出4K_2088859290869264386.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_15

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（图片生成/图生图/krea2 i2i 一键洗图 图生图+洗图工作流_2090754065042067457.json、图片生成/图生图/krea2 i2i 一键洗图 图生图+洗图工作流_2104751982484484098.json、图片生成/图生图/krea2 i2i 一键洗图 快速生图_2091873720318124033.json、图片生成/图生图/krea2 i2i 一键洗图工作流 图生图_2096205084123287553.json、图片生成/图生图/krea2 i2i 一键洗图工作流 图生图_2105994124833943553.json…）

- **类型**：Unknown Workflow
- **样本数**：29
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 29 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 28/29 个有
- `LoadImage` —— 28/29 个有
- `PrimitiveInt` —— 28/29 个有
- `ImageResizeKJv2` —— 19/29 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/29 个有
- `Image Comparer (rgthree)` —— 8/29 个有
- `SeedVR2LoadDiTModel` —— 2/29 个有
- `SeedVR2LoadVAEModel` —— 2/29 个有
- `SeedVR2VideoUpscaler` —— 2/29 个有
- `ImageScaleToTotalPixels` —— 1/29 个有
- `Int` —— 1/29 个有
- `LayerUtility: PurgeVRAM V2` —— 1/29 个有
- `LoraLoaderModelOnly` —— 1/29 个有
- `RBGImageStitchPlus` —— 1/29 个有
- `RepeatLatentBatch` —— 1/29 个有
- `VHS_LoadVideo` —— 1/29 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
