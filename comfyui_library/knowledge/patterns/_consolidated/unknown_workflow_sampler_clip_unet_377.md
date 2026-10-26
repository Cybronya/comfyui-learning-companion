---
name: unknown_workflow_sampler_clip_unet_377
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.733
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/2030050170984992770.json, 图片生成/文生图/flux klein9B 工作流批量跑 浮云1.20_2013513081648848897.json, 图片生成/文生图/节点系列07-Add Label节点添加标签-已发布_2012172737220976641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_377

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/2030050170984992770.json、图片生成/文生图/flux klein9B 工作流批量跑 浮云1.20_2013513081648848897.json、图片生成/文生图/节点系列07-Add Label节点添加标签-已发布_2012172737220976641.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Seed (rgthree)` —— 2/3 个有
- `easy batchAnything` —— 2/3 个有
- `easy forLoopEnd` —— 2/3 个有
- `easy forLoopStart` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `Int` —— 1/3 个有
- `Int2String` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `ProcessString` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `Text` —— 1/3 个有
- `YANC.ConcatStrings` —— 1/3 个有
- `easy convertAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
