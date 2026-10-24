---
name: unknown_workflow_sampler_clip_unet_374
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.819
common_nodes: [CLIPLoader, CLIPTextEncode, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ideogram4--文生图_2063818428254875650.json, 图片生成/文生图/Ideogram4_开源平面设计工作流_2063995698990899201.json, 图片生成/文生图/【遇见AI】ideogram4 文生图，支持json结构化提示词，精准控图，电商海报专用_2063182834180911105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_374

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Ideogram4--文生图_2063818428254875650.json、图片生成/文生图/Ideogram4_开源平面设计工作流_2063995698990899201.json、图片生成/文生图/【遇见AI】ideogram4 文生图，支持json结构化提示词，精准控图，电商海报专用_2063182834180911105.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `Ideogram4Scheduler`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `Ideogram4PromptBuilderKJ` —— 2/3 个有
- `CFGOverride` —— 1/3 个有
- `DuckHideNode` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `SplitSigmas` —— 1/3 个有
- `StringConstantMultiline` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
