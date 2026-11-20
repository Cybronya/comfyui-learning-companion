---
name: unknown_workflow_sampler_clip_unet_28
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.8965
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/提取服装_2034842540221927426.json, 图片生成/图生图/最新Flux 2.0多图编辑工作流（支持直接输入中文提示词）_1993527135818235906.json, 图片生成/图生图/黑森林Flux2单图编辑_1993598436635246593.json, 图片生成/图生图/黑森林Flux2双图编辑_1993606631697088514.json, 图片生成/图生图/（8步加速版）Flux2 Turbo单图编辑加速版V1_2006022078891511809.json, 图片生成/图生图/👾怪獸-FLUX.2单图编辑👾_1993647875032891394.json, 图片生成/图生图/👾怪獸-FLUX.2双图编辑👾_1993647975433961474.json, 图片生成/图生图/🦖Flux2DEV多图编辑_2007631030517239810.json, 图片生成/文生图/3D人物编辑器应用系列之二——FLUX-2-klein-9B文生图_2020299327251423234.json, 图片生成/文生图/FLUX-2-klein-9B_动作精准设计之二工作流_2016865671568691202.json, 图片生成/文生图/FLUX-2-klein-9b_动作精准设计之一工作流_2013405319954702338.json, 图片生成/文生图/FLUX.2 Turbo_2006076343817084929.json, 图片生成/文生图/FLUX2 Dev FP8 8步加速 文生图_图片编辑_2073296125880262657.json, 图片生成/文生图/Flux.2 单图编辑 用嘴改图官方工作流_1998219021541629954.json, 图片生成/文生图/Flux2 单图编辑_1993603003697610753.json, 图片生成/文生图/Flux2 官方文_图生视频_1993512866739322882.json, 图片生成/文生图/Flux2 文生图_1986239618842578945.json, 图片生成/文生图/Flux2-Turbo加速生图_2005931616717467650.json, 图片生成/文生图/Flux2DEV多图编辑_1993501443036479490.json, 图片生成/文生图/Flux2DEV文生图_1993507322504953858.json, 图片生成/文生图/flux2-Timestep Distillation（步级蒸馏）_2061782953197391873.json, 图片生成/文生图/加速优化！Flux.2 基础文生图+多图编辑_图像参考多合一工作流_2058209151062462465.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_28

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/提取服装_2034842540221927426.json、图片生成/图生图/最新Flux 2.0多图编辑工作流（支持直接输入中文提示词）_1993527135818235906.json、图片生成/图生图/黑森林Flux2单图编辑_1993598436635246593.json、图片生成/图生图/黑森林Flux2双图编辑_1993606631697088514.json、图片生成/图生图/（8步加速版）Flux2 Turbo单图编辑加速版V1_2006022078891511809.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 22 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
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
- `FluxGuidance` —— 21/22 个有
- `LoraLoaderModelOnly` —— 6/22 个有
- `Int` —— 5/22 个有
- `PrimitiveInt` —— 5/22 个有
- `CR Prompt Text` —— 4/22 个有
- `ImageConcanate` —— 4/22 个有
- `ModelPatchTorchSettings` —— 4/22 个有
- `PathchSageAttentionKJ` —— 4/22 个有
- `easy promptList` —— 3/22 个有
- `1hew_AnySwitchSelect` —— 1/22 个有
- `Anything Everywhere` —— 1/22 个有
- `CR Text` —— 1/22 个有
- `EasyCache` —— 1/22 个有
- `GetImageSize` —— 1/22 个有
- `GetNode` —— 1/22 个有
- `SetNode` —— 1/22 个有
- `Text` —— 1/22 个有
- `easy imageRemBg` —— 1/22 个有
- `easy seed` —— 1/22 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
