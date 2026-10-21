---
name: unknown_workflow_sampler_clip_unet_67
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.813111
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyNumberConvert, ConditioningZeroOut, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ideogram_4+Prompt_Builder_中文提示词自动文生图_2069068754293710850.json, 图片生成/文生图/Ideogram_4｜结构化视觉海报_文生图生成器_2094723434193448962.json, 图片生成/文生图/Ideogram_4｜结构化视觉海报_文生图生成器_2098917767268360194.json, 图片生成/文生图/Ideogram强势开源支持自然语言极简输入_2064195567823183874.json, 图片生成/文生图/Ideogram自然语文生图_2064911052713844737.json, 图片生成/文生图/ideogram 4 专属JSON提示词 QWEN3.5自动反推 艺术图像文生图工作流_2063594896237359106.json, 图片生成/文生图/ideogram 4 专属JSON提示词 框架编辑 +Lora 艺术图像文生图工作流_2069723100882751490.json, 图片生成/文生图/ideogram 4 专属JSON提示词 框架编辑 2合1 艺术图像文生图工作流_2063591322581299201.json, 视频生成/图生视频/Ideogram+4+Prompt+Builder+中文提示词自动文生图_2089969723621593090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_67

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Ideogram_4+Prompt_Builder_中文提示词自动文生图_2069068754293710850.json、图片生成/文生图/Ideogram_4｜结构化视觉海报_文生图生成器_2094723434193448962.json、图片生成/文生图/Ideogram_4｜结构化视觉海报_文生图生成器_2098917767268360194.json、图片生成/文生图/Ideogram强势开源支持自然语言极简输入_2064195567823183874.json、图片生成/文生图/Ideogram自然语文生图_2064911052713844737.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `ComfyMathExpression` —— 7/9 个有
- `CustomCombo` —— 7/9 个有
- `ResolutionSelector` —— 7/9 个有
- `PrimitiveStringMultiline` —— 6/9 个有
- `llama_cpp_instruct_adv` —— 5/9 个有
- `llama_cpp_model_loader` —— 5/9 个有
- `llama_cpp_parameters` —— 5/9 个有
- `PreviewAny` —— 4/9 个有
- `easy showAnything` —— 4/9 个有
- `Label (rgthree)` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `Text Multiline` —— 3/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `easy seed` —— 3/9 个有
- `Ideogram4PromptBuilderKJ` —— 2/9 个有
- `JjkText` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `Switch any [Crystools]` —— 2/9 个有
- `easy boolean` —— 2/9 个有
- `easy saveText` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
