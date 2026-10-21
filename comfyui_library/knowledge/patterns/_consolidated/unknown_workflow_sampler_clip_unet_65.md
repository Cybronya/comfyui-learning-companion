---
name: unknown_workflow_sampler_clip_unet_65
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.793778
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyNumberConvert, ConditioningZeroOut, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, KSamplerSelect, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ideogram 4.0 精准排版工作流（自然语言输入 + 画面分区控制）_2063868933291204609.json, 图片生成/文生图/Ideogram 4文生图8步加速最优实现_2070104035256000514.json, 图片生成/文生图/Ideogram 4文生图_2062771352070873090.json, 图片生成/文生图/Ideogram 4｜结构化视觉海报_文生图生成器_2092654375297708034.json, 图片生成/文生图/Ideogram4  KJ节点_文生图_2064149542085414914.json, 图片生成/文生图/Ideogram4  KJ节点_文生图（含案例）_2063967049952620546.json, 图片生成/文生图/Ideogram4 区域编辑文生图_2063261187504164866.json, 图片生成/文生图/Ideogram4区域编辑文生图v3_2062789448869441538.json, 图片生成/文生图/Ideogram4文生图效果对比V2（含钱包应用）_2062753547221037058.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_65

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Ideogram 4.0 精准排版工作流（自然语言输入 + 画面分区控制）_2063868933291204609.json、图片生成/文生图/Ideogram 4文生图8步加速最优实现_2070104035256000514.json、图片生成/文生图/Ideogram 4文生图_2062771352070873090.json、图片生成/文生图/Ideogram 4｜结构化视觉海报_文生图生成器_2092654375297708034.json、图片生成/文生图/Ideogram4  KJ节点_文生图_2064149542085414914.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：79%

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
- `ComfyMathExpression` —— 8/9 个有
- `Ideogram4PromptBuilderKJ` —— 8/9 个有
- `PreviewImage` —— 7/9 个有
- `ResolutionSelector` —— 6/9 个有
- `CustomCombo` —— 5/9 个有
- `PreviewAny` —— 5/9 个有
- `PrimitiveStringMultiline` —— 5/9 个有
- `CR Prompt Text` —— 4/9 个有
- `ImageConcatMulti` —— 4/9 个有
- `easy anythingIndexSwitch` —— 3/9 个有
- `AddLabel` —— 2/9 个有
- `LoadImage` —— 2/9 个有
- `RH_RhartImageG2TextToImage` —— 2/9 个有
- `RH_RhartImageNProTextToImage` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `BasicScheduler` —— 1/9 个有
- `ImageBlend` —— 1/9 个有
- `Int` —— 1/9 个有
- `JWInteger` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `ModelSamplingAuraFlow` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `SDVN Any Show` —— 1/9 个有
- `TTResolutionSelector` —— 1/9 个有
- `Text` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
