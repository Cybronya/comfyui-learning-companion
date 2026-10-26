---
name: unknown_workflow_sampler_clip_unet_62
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.789385
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 单图编辑 测试_2013477246534684674.json, 图片生成/图生图/Flux2 Klein 多图编辑 加速版_1993654949070520322.json, 图片生成/图生图/Flux2 Klein全新一键换装加速版_2046867468991336449.json, 图片生成/图生图/Flux2Klein模特换装加速版_2058009325561540609.json, 图片生成/图生图/klein_SU模型图直接渲染效果图+高清放大_2015800051087450114.json, 图片生成/图生图/全新换装 Flux2 Klein 加速版_2019046680485695490.json, 图片生成/图生图/全新换装 Flux2 Klein 加速版！B站艾橘溪_2015984915837362177.json, 图片生成/图生图/庭院效果图洗图-高清放大_2055964480579874817.json, 图片生成/图生图/强行换装_2044612462158286849.json, 图片生成/图生图/模特换装 Flux2 Klein 加速版_2022514742631342082.json, 图片生成/图生图/模特换装Flux2Klein加速版_2050601223795032065.json, 图片生成/图生图/解说漫-Klein角色编辑_2070829957756047362.json, 图片生成/图生图/超强换装加速版_2057401238215553026.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_62

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 单图编辑 测试_2013477246534684674.json、图片生成/图生图/Flux2 Klein 多图编辑 加速版_1993654949070520322.json、图片生成/图生图/Flux2 Klein全新一键换装加速版_2046867468991336449.json、图片生成/图生图/Flux2Klein模特换装加速版_2058009325561540609.json、图片生成/图生图/klein_SU模型图直接渲染效果图+高清放大_2015800051087450114.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
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
- `ConditioningZeroOut` —— 12/13 个有
- `EmptyFlux2LatentImage` —— 12/13 个有
- `Int` —— 11/13 个有
- `GetNode` —— 10/13 个有
- `JjkText` —— 10/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/13 个有
- `SetNode` —— 10/13 个有
- `ImageConcanate` —— 8/13 个有
- `easy imageRemBg` —— 8/13 个有
- `ImageScaleToTotalPixels` —— 7/13 个有
- `SeedVR2LoadDiTModel` —— 7/13 个有
- `SeedVR2LoadVAEModel` —— 7/13 个有
- `SeedVR2VideoUpscaler` —— 7/13 个有
- `PreviewImage` —— 4/13 个有
- `Image Comparer (rgthree)` —— 2/13 个有
- `CustomAddLabel` —— 1/13 个有
- `GetImageSize` —— 1/13 个有
- `ImageConcatMulti` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `Seed (rgthree)` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
