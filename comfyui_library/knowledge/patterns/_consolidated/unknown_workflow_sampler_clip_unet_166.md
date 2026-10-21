---
name: unknown_workflow_sampler_clip_unet_166
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.834
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, ConditioningZeroOut, CustomCombo, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/ideogram4 九宫格广告板_2069186094389874689.json, 图片生成/文生图/ideogram4 文生图 精准写实摄影 数字人_2065236680147296257.json, 图片生成/文生图/ideogram4 自用版_2067414472725192705.json, 图片生成/文生图/ideogram4_t2i文生图_2064543465328963586.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_166

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/ideogram4 九宫格广告板_2069186094389874689.json、图片生成/文生图/ideogram4 文生图 精准写实摄影 数字人_2065236680147296257.json、图片生成/文生图/ideogram4 自用版_2067414472725192705.json、图片生成/文生图/ideogram4_t2i文生图_2064543465328963586.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `CustomCombo`
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
- `Ideogram4PromptBuilderKJ` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `Text` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `llama_cpp_instruct_adv` —— 2/4 个有
- `llama_cpp_model_loader` —— 2/4 个有
- `llama_cpp_parameters` —— 2/4 个有
- `CLIPLoaderGGUF` —— 1/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Ideogram4OptimizationsKJ` —— 1/4 个有
- `InversionDemoLazySwitch` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SimpleToggleNode` —— 1/4 个有
- `StringConcatenate` —— 1/4 个有
- `StringSplitSelect` —— 1/4 个有
- `TextConcatenator` —— 1/4 个有
- `TextGenerate` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
