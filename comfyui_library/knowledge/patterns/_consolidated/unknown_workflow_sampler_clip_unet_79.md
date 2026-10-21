---
name: unknown_workflow_sampler_clip_unet_79
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.80625
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, KSamplerSelect, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ideogram4 文生图-写实摄影专用工作流_2066088865739399169.json, 图片生成/文生图/Ideogram4 精准定位文生图（平面设计_海报设计_角色场景设计）_2063567041306652673.json, 图片生成/文生图/Ideogram4_int8文生图_2080489687994687490.json, 图片生成/文生图/Ideogram4全新玩法-指哪改哪_2064533560844967938.json, 图片生成/文生图/Ideogram4动漫文生图_2071282232492388353.json, 图片生成/文生图/Ideogram4文生图_2064974101588045825.json, 图片生成/文生图/Ideogram4文生图工作流_2085587398561456129.json, 图片生成/文生图/Ideogram4文生图自然语言LLM生成官方提示词版_2073724732792459266.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_79

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Ideogram4 文生图-写实摄影专用工作流_2066088865739399169.json、图片生成/文生图/Ideogram4 精准定位文生图（平面设计_海报设计_角色场景设计）_2063567041306652673.json、图片生成/文生图/Ideogram4_int8文生图_2080489687994687490.json、图片生成/文生图/Ideogram4全新玩法-指哪改哪_2064533560844967938.json、图片生成/文生图/Ideogram4动漫文生图_2071282232492388353.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `Ideogram4Scheduler`
- `KSamplerSelect`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyNumberConvert` —— 7/8 个有
- `CustomCombo` —— 7/8 个有
- `JsonExtractString` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `StringReplace` —— 7/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `Ideogram4PromptBuilderKJ` —— 4/8 个有
- `PreviewAny` —— 4/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `DuckHideNode` —— 1/8 个有
- `LayerColor: BrightnessContrastV2` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `ModelSamplingAuraFlow` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `TextGenerate` —— 1/8 个有
- `easy imageChooser` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
