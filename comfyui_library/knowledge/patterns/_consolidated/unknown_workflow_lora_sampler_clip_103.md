---
name: unknown_workflow_lora_sampler_clip_103
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.579833
common_nodes: [BasicScheduler, BerniniConditioning, CLIPLoader, CLIPTextEncode, ComfySwitchNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, SamplerCustom, SplitSigmas, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Bernini R图生图标准版_2068956525464477698.json, 图片生成/图生图/Bernini_宝藏模型_参考生图_2066852458068004866.json, 图片生成/图生图/Bernini_宝藏模型_图片编辑_2066850763221069826.json, 图片生成/图生图/Bernini_宝藏模型_图片编辑_2073695721940934658.json, 平台全量/Bernini R视频生视频标准版_2068968855644499969.json, 平台全量/Bernini视频去水印_2080319290208776194.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_103

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Bernini R图生图标准版_2068956525464477698.json、图片生成/图生图/Bernini_宝藏模型_参考生图_2066852458068004866.json、图片生成/图生图/Bernini_宝藏模型_图片编辑_2066850763221069826.json、图片生成/图生图/Bernini_宝藏模型_图片编辑_2073695721940934658.json、平台全量/Bernini R视频生视频标准版_2068968855644499969.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 6 个 workflow 都包含：
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
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 5/6 个有
- `BatchImagesNode` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `CustomCombo` —— 3/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `PreviewAny` —— 3/6 个有
- `RegexExtract` —— 3/6 个有
- `ResizeImageMaskNode` —— 3/6 个有
- `StringConcatenate` —— 3/6 个有
- `StringReplace` —— 3/6 个有
- `CreateVideo` —— 2/6 个有
- `GetVideoComponents` —— 2/6 个有
- `LoadVideo` —— 2/6 个有
- `SaveVideo` —— 2/6 个有
- `PreviewImage` —— 1/6 个有
- `SimpleComparison+` —— 1/6 个有
- `Video Slice` —— 1/6 个有
- `easy ifElse` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
