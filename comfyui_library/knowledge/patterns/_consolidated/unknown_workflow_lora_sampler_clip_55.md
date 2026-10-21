---
name: unknown_workflow_lora_sampler_clip_55
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.854
common_nodes: [Anything Everywhere, CFGOverride, CLIPLoader, CLIPTextEncode, CR Text Concatenate, DualModelGuider, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize, ImageSharpen, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MuyeTextEditOutput, PainterFluxImageEdit, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, workflow>Qwen3.5反推, workflow>Qwen3.5自动提示词, workflow>自定义节点]
problems: []
missing: []
members: [图片生成/文生图/Ideogram4+Klein+生图+洗图_2070340784196513793.json, 图片生成/文生图/Ideogram4+Klein+生图+洗图_2071395147308425217.json, 图片生成/文生图/Ideogram4+Klein_生图_洗图_2063994567111831553.json, 图片生成/文生图/Ideogram4+Klein_生图_洗图_2076440564509274114.json, 图片生成/文生图/Ideogram4+Klein文生图高清输出洗图_2065246912453898241.json, 图片生成/文生图/提示词反推 +高清放大  Ideogram4+Klein+文_图生图+最新洗图_2071411449490132994.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_55

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Ideogram4+Klein+生图+洗图_2070340784196513793.json、图片生成/文生图/Ideogram4+Klein+生图+洗图_2071395147308425217.json、图片生成/文生图/Ideogram4+Klein_生图_洗图_2063994567111831553.json、图片生成/文生图/Ideogram4+Klein_生图_洗图_2076440564509274114.json、图片生成/文生图/Ideogram4+Klein文生图高清输出洗图_2065246912453898241.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `Anything Everywhere`
- `CFGOverride`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `DualModelGuider`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `ImageSharpen`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `PainterFluxImageEdit`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `workflow>Qwen3.5反推`
- `workflow>Qwen3.5自动提示词`
- `workflow>自定义节点`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `Ideogram4Scheduler` —— 1/6 个有
- `Int` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 6 | 100% |
| 高度 | 1624 | 1624 - 1624 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1624，观测区间 1624 - 1624，6 个样本，取值集中（一致性 100%）
