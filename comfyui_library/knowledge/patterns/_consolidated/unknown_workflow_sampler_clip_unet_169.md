---
name: unknown_workflow_sampler_clip_unet_169
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.836
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/WH-AI-Studio（Flux2-Klein完美文生图）_2026681586271391745.json, 图片生成/文生图/flux-2-klein 文生图_2013532963312504833.json, 图片生成/文生图/flux-2-klein-9b（文生图）_2012052794068443137.json, 图片生成/文生图/flux2 klein文生图9B_2073301542874206209.json, 图片生成/文生图/flux2-klein文生图工作流_2012032539350798337.json, 图片生成/文生图/flux2_klein文生图_2051855653928480769.json, 图片生成/文生图/【阡陌】FLUX-2-Klein 9B base版文生图工作流_2016491648590553089.json, 图片生成/文生图/【阡陌】FLUX-2-Klein 9B 蒸馏版4步极速文生图工作流_2016500518138421250.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_169

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/WH-AI-Studio（Flux2-Klein完美文生图）_2026681586271391745.json、图片生成/文生图/flux-2-klein 文生图_2013532963312504833.json、图片生成/文生图/flux-2-klein-9b（文生图）_2012052794068443137.json、图片生成/文生图/flux2 klein文生图9B_2073301542874206209.json、图片生成/文生图/flux2-klein文生图工作流_2012032539350798337.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 7/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `LoadImage` —— 3/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `Int` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
