---
name: unknown_workflow_sampler_clip_unet_122
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.815556
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, ConditioningZeroOut, DualModelGuider, EmptyFlux2LatentImage, Ideogram4PromptBuilderKJ, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Ideogram4一键图生图_2066102111875719170.json, 图片生成/文生图/Ideogram 4 + KJ Prompt Builder可视化构图导演_2062786765001412609.json, 图片生成/文生图/Ideogram 4 内部使用版本_2071291697438478337.json, 图片生成/文生图/Ideogram 4 文生图最优实现_2070104029690159105.json, 图片生成/文生图/Ideogram 4文生图8步加速最优实现_2070104035256000514.json, 图片生成/文生图/Ideogram4 文生图-写实摄影专用工作流_2066088865739399169.json, 图片生成/文生图/Ideogram4自定义文生图_超绝美感_2064900969019822082.json, 图片生成/文生图/ideogram4 文生图 精准写实摄影 数字人_2065236680147296257.json, 图片生成/文生图/ideogram4 文生图_1943017003487543298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_122

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Ideogram4一键图生图_2066102111875719170.json、图片生成/文生图/Ideogram 4 + KJ Prompt Builder可视化构图导演_2062786765001412609.json、图片生成/文生图/Ideogram 4 内部使用版本_2071291697438478337.json、图片生成/文生图/Ideogram 4 文生图最优实现_2070104029690159105.json、图片生成/文生图/Ideogram 4文生图8步加速最优实现_2070104035256000514.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `Ideogram4PromptBuilderKJ`
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
- `CustomCombo` —— 5/9 个有
- `CR Text` —— 4/9 个有
- `LoraLoaderModelOnly` —— 4/9 个有
- `BasicScheduler` —— 3/9 个有
- `ModelSamplingAuraFlow` —— 3/9 个有
- `CR Prompt Text` —— 1/9 个有
- `GetObjectFromJson` —— 1/9 个有
- `GetTextFromJson` —— 1/9 个有
- `LayerColor: BrightnessContrastV2` —— 1/9 个有
- `Light-Tool: DeserializeJsonString` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_Translator` —— 1/9 个有
- `StringConstantMultiline` —— 1/9 个有
- `easy showAnything` —— 1/9 个有
- `孤海注释` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
