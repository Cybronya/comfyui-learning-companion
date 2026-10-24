---
name: unknown_workflow_sampler_clip_unet_316
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84225
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, ConditioningZeroOut, CustomCombo, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/ideogram 4 专属JSON提示词 QWEN3.5自动反推 艺术图像文生图工作流_2063594896237359106.json, 图片生成/文生图/ideogram 4 专属JSON提示词 框架编辑 +Lora 艺术图像文生图工作流_2069723100882751490.json, 图片生成/文生图/ideogram 4 专属JSON提示词 框架编辑 2合1 艺术图像文生图工作流_2063591322581299201.json, 图片生成/文生图/ideogram4 九宫格广告板_2069186094389874689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_316

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/ideogram 4 专属JSON提示词 QWEN3.5自动反推 艺术图像文生图工作流_2063594896237359106.json、图片生成/文生图/ideogram 4 专属JSON提示词 框架编辑 +Lora 艺术图像文生图工作流_2069723100882751490.json、图片生成/文生图/ideogram 4 专属JSON提示词 框架编辑 2合1 艺术图像文生图工作流_2063591322581299201.json、图片生成/文生图/ideogram4 九宫格广告板_2069186094389874689.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

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
- `Label (rgthree)` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `easy seed` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `Ideogram4PromptBuilderKJ` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `Switch any [Crystools]` —— 2/4 个有
- `easy boolean` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `llama_cpp_instruct_adv` —— 2/4 个有
- `llama_cpp_model_loader` —— 2/4 个有
- `llama_cpp_parameters` —— 2/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `Ideogram4OptimizationsKJ` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `Text` —— 1/4 个有
- `TextConcatenator` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
