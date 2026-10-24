---
name: unknown_workflow_sampler_clip_vae_26
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.842857
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Integer To String, CR Split String, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, INTConstant, Int, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, StringToInt, Text Concatenate, VAEDecode, VAEEncode, VAELoader, easy compare, easy ifElse]
problems: []
missing: []
members: [图片生成/图生图/Kontext Dev单图模式_1938266634446635009.json, 图片生成/图生图/Kontext单图编辑_1938411645796548610.json, 图片生成/图生图/Kontext用嘴改图王炸模型开源_1938368955515867137.json, 图片生成/图生图/超强模型Kontext单图编辑Nunchaku+Lora双加速版_1950218051007463425.json, 图片生成/图生图/超强模型Kontext单图编辑版_1940596276108963841.json, 图片生成/图生图/超强模型Kontext双图编辑Nunchaku+Lora双加速版_1950227095365533698.json, 图片生成/文生图/[Kontext]flux1-dev-kontext开源版本_1938374526730178562.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_26

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Kontext Dev单图模式_1938266634446635009.json、图片生成/图生图/Kontext单图编辑_1938411645796548610.json、图片生成/图生图/Kontext用嘴改图王炸模型开源_1938368955515867137.json、图片生成/图生图/超强模型Kontext单图编辑Nunchaku+Lora双加速版_1950218051007463425.json、图片生成/图生图/超强模型Kontext单图编辑版_1940596276108963841.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Integer To String`
- `CR Split String`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `INTConstant`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringToInt`
- `Text Concatenate`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy compare`
- `easy ifElse`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 5/7 个有
- `ETN_ReferenceImage` —— 4/7 个有
- `FluxResolutionNode` —— 4/7 个有
- `GetImageSize` —— 4/7 个有
- `ImageConcanate` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `RH_Translator` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `DeepTranslatorTextNode` —— 3/7 个有
- `FluxKontextImageScale` —— 3/7 个有
- `GetImageSize+` —— 3/7 个有
- `JWStringGetLine` —— 3/7 个有
- `RH_LLMAPI_NODE` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `NunchakuFluxDiTLoader` —— 2/7 个有
- `NunchakuFluxLoraLoader` —— 2/7 个有
- `CLIPVisionLoader` —— 1/7 个有
- `EmptyImage` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `StyleModelLoader` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
