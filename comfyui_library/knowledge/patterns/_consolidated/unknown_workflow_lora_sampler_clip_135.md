---
name: unknown_workflow_lora_sampler_clip_135
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.919
common_nodes: [BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningConcat, DisableNoise, FlowEditGuider, FlowEditSampler, FluxGuidance, Image Comparer (rgthree), LoraLoaderModelOnly, OutFluxModelSamplingPred, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX照片转吉卜力风格Ghibli_1916495126468689921.json, 图片生成/图生图/全能图片G-4o 漫画头像转绘_1908423995211788289.json, 图片生成/图生图/吉卜力风格转绘_1912669503619301378.json, 图片生成/图生图/风格转绘（支持多人）_1937504241412149250.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_135

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX照片转吉卜力风格Ghibli_1916495126468689921.json、图片生成/图生图/全能图片G-4o 漫画头像转绘_1908423995211788289.json、图片生成/图生图/吉卜力风格转绘_1912669503619301378.json、图片生成/图生图/风格转绘（支持多人）_1937504241412149250.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningConcat`
- `DisableNoise`
- `FlowEditGuider`
- `FlowEditSampler`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly`
- `OutFluxModelSamplingPred`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConfigureModifiedFlux` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `DualCLIPLoader` —— 2/4 个有
- `DualCLIPLoaderGGUF` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LoadAndResizeImage` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `RepeatLatentBatch` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
