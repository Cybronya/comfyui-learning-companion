---
name: unknown_workflow_sampler_unet_vae_107
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.822667
common_nodes: [CFGGuider, CLIPLoader, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux.2 Klein 9B一键换装_2066148887555039234.json, 图片生成/图生图/Flux.2 Klein 身份一致性引导 单图参考工作流（图生图）简化版_2055121040795283457.json, 图片生成/图生图/Flux.2 Klein助力电商实现AI模特换装自由_ComfyUI工作流_2021893743644778498.json, 图片生成/图生图/Flux2 Klein 单图编辑 加速版 提示词P图_1993505563980087297.json, 图片生成/图生图/一键扩图！Flux2 klein 加速版！艾橘溪_2017423026056339458.json, 图片生成/图生图/全新Flux2 Klein 9B一键换装_2066832444266991617.json, 图片生成/图生图/全新换装 Flux2 Klein 加速版！B站艾橘溪_2015984915837362177.json, 图片生成/图生图/强行换装_2044612462158286849.json, 图片生成/图生图/超强换装加速版_2057401238215553026.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_107

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux.2 Klein 9B一键换装_2066148887555039234.json、图片生成/图生图/Flux.2 Klein 身份一致性引导 单图参考工作流（图生图）简化版_2055121040795283457.json、图片生成/图生图/Flux.2 Klein助力电商实现AI模特换装自由_ComfyUI工作流_2021893743644778498.json、图片生成/图生图/Flux2 Klein 单图编辑 加速版 提示词P图_1993505563980087297.json、图片生成/图生图/一键扩图！Flux2 klein 加速版！艾橘溪_2017423026056339458.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
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
- `ConditioningZeroOut` —— 8/9 个有
- `CLIPTextEncode` —— 7/9 个有
- `GetNode` —— 7/9 个有
- `SetNode` —— 7/9 个有
- `Int` —— 6/9 个有
- `ImageConcanate` —— 5/9 个有
- `JjkText` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `easy imageRemBg` —— 3/9 个有
- `CLIPTextEncodeBREAK` —— 2/9 个有
- `Float` —— 1/9 个有
- `GetImageSizeAndCount` —— 1/9 个有
- `IdentityFeatureTransferV3` —— 1/9 个有
- `Image Size to Number` —— 1/9 个有
- `ImageResize+` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `PrimitiveString` —— 1/9 个有
- `easy globalSeed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
