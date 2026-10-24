---
name: unknown_workflow_sampler_clip_unet_153
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.814875
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyNumberConvert, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ideogram4-文生图_2062877551839760386.json, 图片生成/文生图/Ideogram 4.0 精准排版工作流（自然语言输入 + 画面分区控制）_2063868933291204609.json, 图片生成/文生图/Ideogram 4文生图_2062771352070873090.json, 图片生成/文生图/Ideogram 4｜结构化视觉海报_文生图生成器_2092654375297708034.json, 图片生成/文生图/Ideogram4  KJ节点_文生图_2064149542085414914.json, 图片生成/文生图/Ideogram4  KJ节点_文生图（含案例）_2063967049952620546.json, 图片生成/文生图/Ideogram4 区域编辑文生图_2063261187504164866.json, 图片生成/文生图/ideogram4_t2i文生图+Ideogram 4 Prompt Builder KJ_2064175389697724418.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_153

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/ideogram4-文生图_2062877551839760386.json、图片生成/文生图/Ideogram 4.0 精准排版工作流（自然语言输入 + 画面分区控制）_2063868933291204609.json、图片生成/文生图/Ideogram 4文生图_2062771352070873090.json、图片生成/文生图/Ideogram 4｜结构化视觉海报_文生图生成器_2092654375297708034.json、图片生成/文生图/Ideogram4  KJ节点_文生图_2064149542085414914.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyNumberConvert`
- `DualModelGuider`
- `EmptyFlux2LatentImage`
- `Ideogram4Scheduler`
- `JsonExtractString`
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
- `KSamplerSelect` —— 7/8 个有
- `Ideogram4PromptBuilderKJ` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `CustomCombo` —— 5/8 个有
- `ResolutionSelector` —— 5/8 个有
- `PreviewAny` —— 4/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `ShowText|pysssss` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `LoadImage` —— 2/8 个有
- `easy anythingIndexSwitch` —— 2/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `ImageBlend` —— 1/8 个有
- `Int` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `SDVN Any Show` —— 1/8 个有
- `SamplerEulerAncestral` —— 1/8 个有
- `TTResolutionSelector` —— 1/8 个有
- `Text` —— 1/8 个有
- `easy ifElse` —— 1/8 个有
- `llama_cpp_instruct_adv` —— 1/8 个有
- `llama_cpp_model_loader` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
