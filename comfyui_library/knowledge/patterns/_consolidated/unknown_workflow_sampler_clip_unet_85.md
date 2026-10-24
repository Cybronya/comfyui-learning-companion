---
name: unknown_workflow_sampler_clip_unet_85
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.914455
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/换装-人物换装-flux2-dev-fp8_1993947236568678401.json, 图片生成/图生图/提取服装_2034842540221927426.json, 图片生成/图生图/最新Flux 2.0多图编辑工作流（支持直接输入中文提示词）_1993527135818235906.json, 图片生成/图生图/黑森林Flux2单图编辑_1993598436635246593.json, 图片生成/图生图/黑森林Flux2双图编辑_1993606631697088514.json, 图片生成/图生图/🦖Flux2DEV多图编辑_2007631030517239810.json, 图片生成/文生图/Flux.2 单图编辑 用嘴改图官方工作流_1998219021541629954.json, 图片生成/文生图/Flux.2-支持中文-文生图_1993529170808471553.json, 图片生成/文生图/Flux2DEV多图编辑_1993501443036479490.json, 图片生成/文生图/Flux2DEV文生图_1993507322504953858.json, 图片生成/文生图/最新Flux 2.0文生图工作流（支持直接输入中文提示词）_1993538099806404610.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_85

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/换装-人物换装-flux2-dev-fp8_1993947236568678401.json、图片生成/图生图/提取服装_2034842540221927426.json、图片生成/图生图/最新Flux 2.0多图编辑工作流（支持直接输入中文提示词）_1993527135818235906.json、图片生成/图生图/黑森林Flux2单图编辑_1993598436635246593.json、图片生成/图生图/黑森林Flux2双图编辑_1993606631697088514.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
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
- `FluxGuidance` —— 10/11 个有
- `ImageScaleToTotalPixels` —— 10/11 个有
- `ImageConcanate` —— 5/11 个有
- `Int` —— 4/11 个有
- `easy promptList` —— 4/11 个有
- `CR Text` —— 2/11 个有
- `GetNode` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `AddLabel` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `ModelPatchTorchSettings` —— 1/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `WanVideoImageResizeToClosest` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
