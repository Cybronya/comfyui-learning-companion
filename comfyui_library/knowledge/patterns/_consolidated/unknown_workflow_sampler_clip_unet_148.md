---
name: unknown_workflow_sampler_clip_unet_148
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.718375
common_nodes: [CFGOverride, CLIPTextEncode, ComfyNumberConvert, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, PreviewAny, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Ideogram+开源支持语言简洁文生图_2066708942339796993.json, 图片生成/图生图/ideogram4.0最新开源模型_2063994332616683521.json, 图片生成/文生图/Ideogram 4 KJ Prompt Builder 风格参考+自动文生图_2065368278498889730.json, 图片生成/文生图/Ideogram 4 出图官流_2062772528212439042.json, 图片生成/文生图/Ideogram 4 洗图结构化 JSON 重组_2064321335798620162.json, 图片生成/文生图/Ideogram 图生图参考潜空间重构_2064321322360074241.json, 图片生成/文生图/Ideogram_4+Prompt_Builder_中文提示词自动文生图_2069068754293710850.json, 视频生成/图生视频/Ideogram+4+Prompt+Builder+中文提示词自动文生图_2089969723621593090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_148

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Ideogram+开源支持语言简洁文生图_2066708942339796993.json、图片生成/图生图/ideogram4.0最新开源模型_2063994332616683521.json、图片生成/文生图/Ideogram 4 KJ Prompt Builder 风格参考+自动文生图_2065368278498889730.json、图片生成/文生图/Ideogram 4 出图官流_2062772528212439042.json、图片生成/文生图/Ideogram 4 洗图结构化 JSON 重组_2064321335798620162.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGOverride`
- `CLIPTextEncode`
- `ComfyNumberConvert`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `Ideogram4Scheduler`
- `JsonExtractString`
- `KSamplerSelect`
- `PreviewAny`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 7/8 个有
- `ConditioningZeroOut` —— 7/8 个有
- `PrimitiveStringMultiline` —— 7/8 个有
- `CLIPLoader` —— 6/8 个有
- `easy showAnything` —— 6/8 个有
- `ResolutionSelector` —— 5/8 个有
- `llama_cpp_instruct_adv` —— 5/8 个有
- `llama_cpp_model_loader` —— 5/8 个有
- `LoadImage` —— 4/8 个有
- `Ideogram4PromptBuilderKJ` —— 3/8 个有
- `RHLLMChatNode` —— 3/8 个有
- `llama_cpp_parameters` —— 3/8 个有
- `CLIPLoaderGGUF` —— 2/8 个有
- `CustomCombo` —— 2/8 个有
- `DisTorchPurgeVRAMV2` —— 2/8 个有
- `Float` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `easy saveText` —— 2/8 个有
- `image_scale_pixel_v2` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `Ideogram4OptimizationsKJ` —— 1/8 个有
- `ImageScale` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `SplitSigmasDenoise` —— 1/8 个有
- `VAEEncode` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
