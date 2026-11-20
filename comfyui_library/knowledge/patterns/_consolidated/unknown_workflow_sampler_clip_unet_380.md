---
name: unknown_workflow_sampler_clip_unet_380
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.96075
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/TUT-高清放大2K工作流[Klein+SeedVR2]-2026-09-20_2100321394654535682.json, 平台全量/ai追色工作流（klein）_2015024392371179521.json, 平台全量/klein产品换色工作流（指定颜色）_2020482071218626562.json, 平台全量/klein去除图片中的字幕_水印_1938640988111822849.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_380

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/TUT-高清放大2K工作流[Klein+SeedVR2]-2026-09-20_2100321394654535682.json、平台全量/ai追色工作流（klein）_2015024392371179521.json、平台全量/klein产品换色工作流（指定颜色）_2020482071218626562.json、平台全量/klein去除图片中的字幕_水印_1938640988111822849.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `ImageScaleToTotalPixels` —— 3/4 个有
- `ttN text` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `Text Concatenate` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `FL_ColorPicker` —— 1/4 个有
- `ImageSharpen` —— 1/4 个有
- `LayerColor: ColorAdapter` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有
- `SeedVR2ExtraArgs` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
