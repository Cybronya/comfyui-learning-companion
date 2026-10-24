---
name: unknown_workflow_sampler_clip_unet_32
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.8702
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 单图编辑 测试_2013477246534684674.json, 图片生成/图生图/Flux2 Klein 多图编辑 加速版_1993654949070520322.json, 图片生成/图生图/Flux2 Klein全新一键换装加速版_2046867468991336449.json, 图片生成/图生图/Flux2+Klein_9b最强动漫转写实真人_2023680510127513601.json, 图片生成/图生图/Flux2+Klein控油高清+真实系皮肤质感_2057795926776958978.json, 图片生成/图生图/Flux2+Klein电商产品精修_2052968122042331137.json, 图片生成/图生图/Flux2+Klein电商产品精修_2059467199106084865.json, 图片生成/图生图/Flux2+Klein电商产品精修_2064548916141576194.json, 图片生成/图生图/Flux2+Klein电商产品精修_2064556061675311106.json, 图片生成/图生图/Flux2+Klein电商产品精修_2093243077682089986.json, 图片生成/图生图/Flux2+Klein电商产品精修_2093514490821300225.json, 图片生成/图生图/Flux2-Klein9b超级皮肤质感_2022873403333545985.json, 图片生成/图生图/Flux2Klein9b最强动漫转写实真人_2044631862445875202.json, 图片生成/图生图/Flux2Klein模特换装加速版_2058009325561540609.json, 图片生成/图生图/klein9b白底生背景家具美式中古风格支持_2055473199701348354.json, 图片生成/图生图/klein9b白底自动匹配背景家具美式风_2059563878874439681.json, 图片生成/图生图/全新换装 Flux2 Klein 加速版_2019046680485695490.json, 图片生成/图生图/模特换装 Flux2 Klein 加速版_2022514742631342082.json, 图片生成/图生图/模特换装Flux2Klein加速版_2050601223795032065.json, 图片生成/图生图/蒜香卡普klein9b白底生背景家具美式中古风格支持2048px_2051843695250554881.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_32

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 单图编辑 测试_2013477246534684674.json、图片生成/图生图/Flux2 Klein 多图编辑 加速版_1993654949070520322.json、图片生成/图生图/Flux2 Klein全新一键换装加速版_2046867468991336449.json、图片生成/图生图/Flux2+Klein_9b最强动漫转写实真人_2023680510127513601.json、图片生成/图生图/Flux2+Klein控油高清+真实系皮肤质感_2057795926776958978.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
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
- `ConditioningZeroOut` —— 19/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 18/20 个有
- `PreviewImage` —— 14/20 个有
- `LoraLoaderModelOnly` —— 13/20 个有
- `Int` —— 12/20 个有
- `Image Comparer (rgthree)` —— 11/20 个有
- `CR Prompt Text` —— 10/20 个有
- `JjkText` —— 7/20 个有
- `SeedVR2LoadDiTModel` —— 7/20 个有
- `SeedVR2LoadVAEModel` —— 7/20 个有
- `SeedVR2VideoUpscaler` —— 7/20 个有
- `GetNode` —— 6/20 个有
- `SetNode` —— 6/20 个有
- `ImageConcanate` —— 5/20 个有
- `easy imageRemBg` —— 5/20 个有
- `ImageScaleToTotalPixels` —— 4/20 个有
- `Fast Groups Bypasser (rgthree)` —— 3/20 个有
- `LoraLoader` —— 3/20 个有
- `PlaySound|pysssss` —— 3/20 个有
- `PrimitiveStringMultiline` —— 3/20 个有
- `CustomAddLabel` —— 1/20 个有
- `ImageConcatMulti` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
