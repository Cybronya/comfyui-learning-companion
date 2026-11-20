---
name: unknown_workflow_lora_sampler_clip_197
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.93
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/女生发型测试1.0_2025882097881194498.json, 图片生成/图生图/效果图-klein超分放大重绘_2054488672979955714.json, 图片生成/图生图/男生发型测试1.0_2028692677126000641.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_197

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/女生发型测试1.0_2025882097881194498.json、图片生成/图生图/效果图-klein超分放大重绘_2054488672979955714.json、图片生成/图生图/男生发型测试1.0_2028692677126000641.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatFromBatch` —— 2/3 个有
- `ImageListToBatch+` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LayerUtility: ImageReel` —— 2/3 个有
- `LayerUtility: ImageReelComposit` —— 2/3 个有
- `Text` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `ColorMatch` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `ResizeShortestToNode` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `WD14Tagger|pysssss` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
