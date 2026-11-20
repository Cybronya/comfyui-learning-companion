---
name: unknown_workflow_sampler_unet_vae_148
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.843
common_nodes: [CFGGuider, CLIPLoader, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux.2 Klein 9B一键换装_2066148887555039234.json, 图片生成/图生图/Flux.2 Klein 身份一致性引导 单图参考工作流（图生图）简化版_2055121040795283457.json, 图片生成/图生图/Flux.2 Klein助力电商实现AI模特换装自由_ComfyUI工作流_2021893743644778498.json, 图片生成/图生图/Flux2 Klein 单图编辑 加速版 提示词P图_1993505563980087297.json, 图片生成/图生图/一键扩图！Flux2 klein 加速版！艾橘溪_2017423026056339458.json, 图片生成/图生图/全新Flux2 Klein 9B一键换装_2066832444266991617.json, 数字人/数字人/Flux2 Klein 多图编辑 加速版_2012172771391971330.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_148

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux.2 Klein 9B一键换装_2066148887555039234.json、图片生成/图生图/Flux.2 Klein 身份一致性引导 单图参考工作流（图生图）简化版_2055121040795283457.json、图片生成/图生图/Flux.2 Klein助力电商实现AI模特换装自由_ComfyUI工作流_2021893743644778498.json、图片生成/图生图/Flux2 Klein 单图编辑 加速版 提示词P图_1993505563980087297.json、图片生成/图生图/一键扩图！Flux2 klein 加速版！艾橘溪_2017423026056339458.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `SaveImage` —— 6/7 个有
- `CLIPTextEncode` —— 5/7 个有
- `GetNode` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `Int` —— 4/7 个有
- `JjkText` —— 3/7 个有
- `CLIPTextEncodeBREAK` —— 2/7 个有
- `ImageConcanate` —— 2/7 个有
- `Float` —— 1/7 个有
- `GetImageSizeAndCount` —— 1/7 个有
- `IdentityFeatureTransferV3` —— 1/7 个有
- `Image Size to Number` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `LayerUtility: SaveImagePlusV2` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `PrimitiveString` —— 1/7 个有
- `easy globalSeed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
