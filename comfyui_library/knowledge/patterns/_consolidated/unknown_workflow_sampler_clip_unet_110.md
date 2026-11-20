---
name: unknown_workflow_sampler_clip_unet_110
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9466
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX3 PE提示词强化加速版图像编辑_2111364166001971202.json, 图片生成/图生图/FLUX3+PE提示词强化加速版图像编辑_2111477045355180034.json, 图片生成/图生图/FLUX3加速版图像编辑_2110845040582025217.json, 图片生成/图生图/FLUX3加速版图像编辑_2111037244042727426.json, 图片生成/图生图/Flux2 dev 多图编辑工作流 - 一致性_1994746929441542145.json, 图片生成/图生图/Flux2 dev 多图编辑能力_1994452506996510722.json, 图片生成/图生图/Flux2.DEV-三角色一场景图编辑_2018937350511923202.json, 图片生成/图生图/Flux2.DEV-多图编辑【一天王者】_1994920372749393922.json, 图片生成/图生图/Flux2DEV单图编辑_1994049571294822402.json, 图片生成/图生图/👾怪獸-FLUX.2多图编辑👾_1993639173827608577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_110

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/FLUX3 PE提示词强化加速版图像编辑_2111364166001971202.json、图片生成/图生图/FLUX3+PE提示词强化加速版图像编辑_2111477045355180034.json、图片生成/图生图/FLUX3加速版图像编辑_2110845040582025217.json、图片生成/图生图/FLUX3加速版图像编辑_2111037244042727426.json、图片生成/图生图/Flux2 dev 多图编辑工作流 - 一致性_1994746929441542145.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
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
- `Flux2Scheduler` —— 6/10 个有
- `FluxGuidance` —— 6/10 个有
- `ImageScaleToTotalPixels` —— 6/10 个有
- `ImageConcanate` —— 5/10 个有
- `ManualSigmas` —— 4/10 个有
- `PDIMAGE_LongerSize` —— 4/10 个有
- `easy promptList` —— 3/10 个有
- `CR Prompt Text` —— 2/10 个有
- `Flux3PELoader` —— 2/10 个有
- `Flux3PromptEnhance` —— 2/10 个有
- `GetLatentSize` —— 2/10 个有
- `Int` —— 2/10 个有
- `PreviewAny` —— 2/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `RH_LLMAPI_NODE` —— 2/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
