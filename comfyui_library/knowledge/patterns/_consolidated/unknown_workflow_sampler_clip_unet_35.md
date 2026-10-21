---
name: unknown_workflow_sampler_clip_unet_35
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.798923
common_nodes: [CFGOverride, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, DualModelGuider, EmptyFlux2LatentImage, Ideogram4Scheduler, JsonExtractString, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/ideogram4文生图_2062829306715402242.json, 图片生成/文生图/ideogram4文生图_2074082025207844866.json, 图片生成/文生图/ideogram4文生图带提示词反推_2064481432193560577.json, 图片生成/文生图/ideogram4精准定位文生图_2063313314121338882.json, 图片生成/文生图/ideogram4精准定位文生图_2063606590858678273.json, 图片生成/文生图/ideogram4精准定位文生图_2066720301649768448.json, 图片生成/文生图/ideogram_光学眼镜模特_2073959342348521473.json, 图片生成/文生图/image_ideogram4_t2i_2062711247589691394.json, 图片生成/文生图/image_ideogram4_t2i_2062872301623926785.json, 图片生成/文生图/new_image_ideogram4_t2i  文生图工作流_2062929225497268226.json, 图片生成/文生图/【开源MJ】Ideogram4美学大师_2063949376107663361.json, 图片生成/文生图/图文排版新模型-IdeoGram4_2062809092619591682.json, 图片生成/文生图/指哪打哪文生图_ideogram4_t2i_2062732159298920450.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_35

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/ideogram4文生图_2062829306715402242.json、图片生成/文生图/ideogram4文生图_2074082025207844866.json、图片生成/文生图/ideogram4文生图带提示词反推_2064481432193560577.json、图片生成/文生图/ideogram4精准定位文生图_2063313314121338882.json、图片生成/文生图/ideogram4精准定位文生图_2063606590858678273.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
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
- `ConditioningZeroOut` —— 10/13 个有
- `KSamplerSelect` —— 10/13 个有
- `ResolutionSelector` —— 10/13 个有
- `CustomCombo` —— 9/13 个有
- `PreviewAny` —— 9/13 个有
- `PrimitiveStringMultiline` —— 8/13 个有
- `Ideogram4PromptBuilderKJ` —— 5/13 个有
- `PreviewImage` —— 5/13 个有
- `ImageConcatMulti` —— 4/13 个有
- `ShowText|pysssss` —— 4/13 个有
- `StringConcatenate` —— 4/13 个有
- `TextGenerate` —— 4/13 个有
- `SamplerEulerAncestral` —— 3/13 个有
- `CR Text` —— 2/13 个有
- `AILab_ImagePreview` —— 1/13 个有
- `DeepTranslatorTextNode` —— 1/13 个有
- `Display Int (rgthree)` —— 1/13 个有
- `ImageBlend` —— 1/13 个有
- `LoraLoaderModelOnly` —— 1/13 个有
- `RHLLMChatNode` —— 1/13 个有
- `SeedVR2` —— 1/13 个有
- `SeedVR2BlockSwap` —— 1/13 个有
- `SeedVR2ExtraArgs` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
