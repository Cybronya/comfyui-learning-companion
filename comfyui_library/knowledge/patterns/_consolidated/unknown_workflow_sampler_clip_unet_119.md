---
name: unknown_workflow_sampler_clip_unet_119
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.828333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux klein9B 工作流批量跑 浮云1.20_2013513081648848897.json, 图片生成/文生图/flux-2-klein 文生图_2013532963312504833.json, 图片生成/文生图/flux2 klein文生图9B_2073301542874206209.json, 图片生成/文生图/flux2-Klein-文生图（9B）_2012016556003303426.json, 图片生成/文生图/flux2-klein文生图工作流_2012032539350798337.json, 视频生成/文生视频/flux klein4B 工作流 浮云1.17_2012350472430034946.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_119

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/flux klein9B 工作流批量跑 浮云1.20_2013513081648848897.json、图片生成/文生图/flux-2-klein 文生图_2013532963312504833.json、图片生成/文生图/flux2 klein文生图9B_2073301542874206209.json、图片生成/文生图/flux2-Klein-文生图（9B）_2012016556003303426.json、图片生成/文生图/flux2-klein文生图工作流_2012032539350798337.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
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
- `PrimitiveInt` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `Label (rgthree)` —— 1/6 个有
- `ProcessString` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `easy int` —— 1/6 个有
- `easy promptLine` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
