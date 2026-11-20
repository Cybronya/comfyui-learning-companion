---
name: unknown_workflow_sampler_clip_unet_129
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.972444
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX.2-KLEIN-单图编辑-高清直出_2019989626764664833.json, 图片生成/图生图/FLUX.2-KLEIN-双图编辑-高清直出_2019989419784146946.json, 图片生成/图生图/FLUX2-Klein Flux-2-Klein-9B 多图编辑  电商产品场景 万能迁移 光影一致_2025034756479524865.json, 图片生成/图生图/Flux 2 klein 4b 强力换头_2038542238401171457.json, 图片生成/图生图/Flux 2 klein 4b 换头工作流_2012867203107917825.json, 图片生成/图生图/Flux 2 klein 9b 100% 只换脸工作流_2016484736058793986.json, 图片生成/图生图/Flux 2 klein 9b 换脸非换头工作流_2017157128376557570.json, 图片生成/图生图/Flux klein100%换脸工作流（不改发型）_2030855449922248705.json, 图片生成/图生图/亚秒级40秒100%换脸工作流 V1.00404_2040329795237584898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_129

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FLUX.2-KLEIN-单图编辑-高清直出_2019989626764664833.json、图片生成/图生图/FLUX.2-KLEIN-双图编辑-高清直出_2019989419784146946.json、图片生成/图生图/FLUX2-Klein Flux-2-Klein-9B 多图编辑  电商产品场景 万能迁移 光影一致_2025034756479524865.json、图片生成/图生图/Flux 2 klein 4b 强力换头_2038542238401171457.json、图片生成/图生图/Flux 2 klein 4b 换头工作流_2012867203107917825.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
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
- `ImageScaleToTotalPixels` —— 7/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `LayerColor: Brightness & Contrast` —— 4/9 个有
- `LayerUtility: CropByMask V2` —— 4/9 个有
- `MaskPreview` —— 3/9 个有
- `ycFaceMaskCreator` —— 3/9 个有
- `CustomAddLabel` —— 2/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `SeedVR2` —— 2/9 个有
- `Text` —— 2/9 个有
- `FaceToMask` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
