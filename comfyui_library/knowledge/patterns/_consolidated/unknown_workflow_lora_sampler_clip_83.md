---
name: unknown_workflow_lora_sampler_clip_83
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.848167
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/效果图-klein超分放大重绘_2054488672979955714.json, 图片生成/图生图/渲染级产品精修V5 +自动白底 +细节增强_2084924306483666945.json, 图片生成/图生图/老孙AI 零偏移溶图_2094232856351563777.json, 图片生成/图生图/黑鹤-0色差0位移放大-小志lord_2095493334134517761.json, 图片生成/图生图/黑鹤-0色差0位移放大-小志lord_2101693603444781057.json, 图片生成/文生图/二次元老婆秒变真人！ComfyUI动漫转写实，脸不变质感拉满_2059589704609255426.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_83

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/效果图-klein超分放大重绘_2054488672979955714.json、图片生成/图生图/渲染级产品精修V5 +自动白底 +细节增强_2084924306483666945.json、图片生成/图生图/老孙AI 零偏移溶图_2094232856351563777.json、图片生成/图生图/黑鹤-0色差0位移放大-小志lord_2095493334134517761.json、图片生成/图生图/黑鹤-0色差0位移放大-小志lord_2101693603444781057.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `Seed (rgthree)` —— 5/6 个有
- `easy int` —— 5/6 个有
- `ImageSmartSharpen+` —— 4/6 个有
- `LayerUtility: PurgeVRAM V2` —— 4/6 个有
- `CR Prompt Text` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `GetImageSize` —— 2/6 个有
- `easy imageColorMatch` —— 2/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `CR Text Input Switch (4 way)` —— 1/6 个有
- `ColorMatch` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `ResizeShortestToNode` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `WD14Tagger|pysssss` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
