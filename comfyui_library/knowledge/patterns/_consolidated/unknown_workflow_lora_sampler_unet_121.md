---
name: unknown_workflow_lora_sampler_unet_121
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.802167
common_nodes: [CLIPLoader, FluxKontextImageScale, KSampler, LayerMask: MaskInvert, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveStringMultiline, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511超级扩图_2012115418680397825.json, 图片生成/图生图/Qwen-Eidt-2511人物换装，换背景_2012078904898494465.json, 图片生成/图生图/Qwen-Eidt-2511人物换装，换背景_2013902159636602881.json, 图片生成/图生图/[🛫书墨]Qwen-Edit-2511-极限扩图测试_2003854957788995586.json, 图片生成/图生图/[🛫书墨]小红书fireRed-image-edit超比例扩图_2026578402613923842.json, 图片生成/图生图/【🛫书墨】人物换装、换背景_2011647468227792898.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_121

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511超级扩图_2012115418680397825.json、图片生成/图生图/Qwen-Eidt-2511人物换装，换背景_2012078904898494465.json、图片生成/图生图/Qwen-Eidt-2511人物换装，换背景_2013902159636602881.json、图片生成/图生图/[🛫书墨]Qwen-Edit-2511-极限扩图测试_2003854957788995586.json、图片生成/图生图/[🛫书墨]小红书fireRed-image-edit超比例扩图_2026578402613923842.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextImageScale`
- `KSampler`
- `LayerMask: MaskInvert`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 5/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/6 个有
- `LayerMask: MaskPreview` —— 5/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `InpaintModelConditioning` —— 4/6 个有
- `Any Switch (rgthree)` —— 3/6 个有
- `ClothesSegment` —— 3/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `Fast Groups Muter (rgthree)` —— 3/6 个有
- `GetImageSize` —— 3/6 个有
- `LayerUtility: ExtendCanvasV2` —— 3/6 个有
- `LayerUtility: ImageRemoveAlpha` —— 3/6 个有
- `SolidMask` —— 3/6 个有
- `easy int` —— 3/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `easy imageConcat` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 512 | 512 - 512 | 5 | 100% |
| 高度 | 512 | 512 - 512 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，5 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
