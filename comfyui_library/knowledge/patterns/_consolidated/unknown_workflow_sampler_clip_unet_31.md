---
name: unknown_workflow_sampler_clip_unet_31
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.706615
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, ConditioningZeroOut, DualModelGuider, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ideogram 4文生图（API调用）_2062012575637917697.json, 图片生成/文生图/Ideogram 4文生图（免费自动版）_2062732665601744898.json, 图片生成/文生图/Ideogram 4文生图（手动版）_2063099793219608578.json, 图片生成/文生图/Ideogram4 手动控制区域（KJ）_2063831079253012481.json, 图片生成/文生图/Ideogram4新开源智能JSON格式文生图_2064948644645793794.json, 图片生成/文生图/Ideogram4智能JSON格式文生图_2064134445258596354.json, 图片生成/文生图/Ideogram4美学设计全自动文生图_2063531342176014337.json, 图片生成/文生图/Ideogram4自定义文生图_超绝美感_2064900969019822082.json, 图片生成/文生图/Ideogram4（平替MJ）文生图美学大师_2067620647542542337.json, 图片生成/文生图/[Ideogram 4 系列 01] Ideogram 4 第一课：官方 ComfyUI 工作流解析_2084558233645174785.json, 图片生成/文生图/[Ideogram 4 系列 02] Prompt Builder 解析_2084481304804024321.json, 图片生成/文生图/文生图 布局可控 Ideogram4！_2063268058420039682.json, 图片生成/文生图/设计师福音 文生图精准编辑  ideogram4_2063246111061663745.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_31

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Ideogram 4文生图（API调用）_2062012575637917697.json、图片生成/文生图/Ideogram 4文生图（免费自动版）_2062732665601744898.json、图片生成/文生图/Ideogram 4文生图（手动版）_2063099793219608578.json、图片生成/文生图/Ideogram4 手动控制区域（KJ）_2063831079253012481.json、图片生成/文生图/Ideogram4新开源智能JSON格式文生图_2064948644645793794.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `DualModelGuider`
- `Ideogram4Scheduler`
- `JsonExtractString`
- `KSamplerSelect`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyFlux2LatentImage` —— 11/13 个有
- `PreviewAny` —— 8/13 个有
- `PrimitiveStringMultiline` —— 8/13 个有
- `CR Text` —— 7/13 个有
- `GetNode` —— 6/13 个有
- `SetNode` —— 6/13 个有
- `CustomCombo` —— 5/13 个有
- `Fast Groups Bypasser (rgthree)` —— 5/13 个有
- `Ideogram4PromptBuilderKJ` —— 5/13 个有
- `Int` —— 5/13 个有
- `PreviewImage` —— 5/13 个有
- `LoadImage` —— 4/13 个有
- `easy showAnything` —— 4/13 个有
- `RHLLMChatNode` —— 3/13 个有
- `TextGenerate` —— 3/13 个有
- `EmptyLatentImage` —— 2/13 个有
- `Ideogram4OptimizationsKJ` —— 2/13 个有
- `ImpactSwitch` —— 2/13 个有
- `RH_LLMAPI_NODE` —— 2/13 个有
- `easy promptLine` —— 2/13 个有
- `DeepTranslatorTextNode` —— 1/13 个有
- `StringConcatenate` —— 1/13 个有
- `取色器_孤海` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
