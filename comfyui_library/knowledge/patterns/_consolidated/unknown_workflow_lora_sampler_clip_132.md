---
name: unknown_workflow_lora_sampler_clip_132
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.56875
common_nodes: [BasicScheduler, BerniniConditioning, CLIPLoader, CLIPTextEncode, ComfySwitchNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, SamplerCustom, SaveImage, SplitSigmas, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Bernini R图生图标准版_2068956525464477698.json, 图片生成/图生图/Bernini_宝藏模型_参考生图_2066852458068004866.json, 图片生成/图生图/Bernini_宝藏模型_图片编辑_2066850763221069826.json, 图片生成/图生图/Bernini_宝藏模型_图片编辑_2073695721940934658.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_132

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Bernini R图生图标准版_2068956525464477698.json、图片生成/图生图/Bernini_宝藏模型_参考生图_2066852458068004866.json、图片生成/图生图/Bernini_宝藏模型_图片编辑_2066850763221069826.json、图片生成/图生图/Bernini_宝藏模型_图片编辑_2073695721940934658.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SamplerCustom`
- `SaveImage`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `ResizeImageMaskNode` —— 3/4 个有
- `BatchImagesNode` —— 2/4 个有
- `CustomCombo` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RegexExtract` —— 1/4 个有
- `SimpleComparison+` —— 1/4 个有
- `StringConcatenate` —— 1/4 个有
- `StringReplace` —— 1/4 个有
- `easy ifElse` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
