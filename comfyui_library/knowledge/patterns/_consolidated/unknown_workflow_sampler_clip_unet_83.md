---
name: unknown_workflow_sampler_clip_unet_83
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.834
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, ConditioningZeroOut, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text]
members: [图片生成/文生图/1943017003487543298.json, 图片生成/文生图/ideogram_光学眼镜模特_2073959342348521473.json, 视频生成/图生视频/Ideogram+4+Prompt+Builder+中文提示词自动文生图_2089969723621593090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_83

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1943017003487543298.json、图片生成/文生图/ideogram_光学眼镜模特_2073959342348521473.json、视频生成/图生视频/Ideogram+4+Prompt+Builder+中文提示词自动文生图_2089969723621593090.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
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
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `CustomCombo` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `Ideogram4PromptBuilderKJ` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy saveText` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
