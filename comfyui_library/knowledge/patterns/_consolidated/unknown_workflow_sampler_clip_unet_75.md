---
name: unknown_workflow_sampler_clip_unet_75
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.695875
common_nodes: [CFGOverride, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, ConditioningZeroOut, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text]
members: [图片生成/文生图/1943017003487543298.json, 图片生成/文生图/Ideogram 4 + KJ Prompt Builder可视化构图导演_2062786765001412609.json, 图片生成/文生图/Ideogram 4 KJ Prompt Builder 风格参考+自动文生图_2065368278498889730.json, 图片生成/文生图/Ideogram 4 内部使用版本_2071291697438478337.json, 图片生成/文生图/Ideogram 4 出图官流_2062772528212439042.json, 图片生成/文生图/Ideogram 4 文生图最优实现_2070104029690159105.json, 图片生成/文生图/Ideogram 4 洗图结构化 JSON 重组_2064321335798620162.json, 图片生成/文生图/Ideogram 图生图参考潜空间重构_2064321322360074241.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_75

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1943017003487543298.json、图片生成/文生图/Ideogram 4 + KJ Prompt Builder可视化构图导演_2062786765001412609.json、图片生成/文生图/Ideogram 4 KJ Prompt Builder 风格参考+自动文生图_2065368278498889730.json、图片生成/文生图/Ideogram 4 内部使用版本_2071291697438478337.json、图片生成/文生图/Ideogram 4 出图官流_2062772528212439042.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGOverride`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `Ideogram4Scheduler`
- `JsonExtractString`
- `KSamplerSelect`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Ideogram4PromptBuilderKJ` —— 7/8 个有
- `CLIPLoader` —— 6/8 个有
- `ResolutionSelector` —— 6/8 个有
- `PreviewAny` —— 4/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `LoadImage` —— 3/8 个有
- `RHLLMChatNode` —— 3/8 个有
- `BasicScheduler` —— 2/8 个有
- `CLIPLoaderGGUF` —— 2/8 个有
- `DisTorchPurgeVRAMV2` —— 2/8 个有
- `Float` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `ModelSamplingAuraFlow` —— 2/8 个有
- `image_scale_pixel_v2` —— 2/8 个有
- `llama_cpp_instruct_adv` —— 2/8 个有
- `llama_cpp_model_loader` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `CustomCombo` —— 1/8 个有
- `ImageScale` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `SplitSigmasDenoise` —— 1/8 个有
- `VAEEncode` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
