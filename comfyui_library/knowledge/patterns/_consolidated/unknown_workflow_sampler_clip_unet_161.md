---
name: unknown_workflow_sampler_clip_unet_161
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.730625
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ideogram 4文生图（API调用）_2062012575637917697.json, 图片生成/文生图/Ideogram 4文生图（免费自动版）_2062732665601744898.json, 图片生成/文生图/Ideogram 4文生图（手动版）_2063099793219608578.json, 图片生成/文生图/Ideogram4 手动控制区域（KJ）_2063831079253012481.json, 图片生成/文生图/Ideogram4新开源智能JSON格式文生图_2064948644645793794.json, 图片生成/文生图/Ideogram4智能JSON格式文生图_2064134445258596354.json, 图片生成/文生图/VividMuse Ideogram4 workflow_2064337095640047618.json, 图片生成/文生图/ideogram4 自用版_2067414472725192705.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_161

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Ideogram 4文生图（API调用）_2062012575637917697.json、图片生成/文生图/Ideogram 4文生图（免费自动版）_2062732665601744898.json、图片生成/文生图/Ideogram 4文生图（手动版）_2063099793219608578.json、图片生成/文生图/Ideogram4 手动控制区域（KJ）_2063831079253012481.json、图片生成/文生图/Ideogram4新开源智能JSON格式文生图_2064948644645793794.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `Ideogram4Scheduler`
- `JsonExtractString`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `CR Text` —— 5/8 个有
- `TextGenerate` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `GetNode` —— 4/8 个有
- `Int` —— 4/8 个有
- `LoadImage` —— 4/8 个有
- `PreviewAny` —— 4/8 个有
- `SetNode` —— 4/8 个有
- `Ideogram4PromptBuilderKJ` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `StringConcatenate` —— 2/8 个有
- `CLIPLoaderGGUF` —— 1/8 个有
- `CustomCombo` —— 1/8 个有
- `DeepTranslatorTextNode` —— 1/8 个有
- `ImpactSwitch` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `RHLLMChatNode` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `Text` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy promptList` —— 1/8 个有
- `取色器_孤海` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
