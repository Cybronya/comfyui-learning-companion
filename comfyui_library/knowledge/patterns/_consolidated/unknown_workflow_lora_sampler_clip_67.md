---
name: unknown_workflow_lora_sampler_clip_67
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.693571
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, Fast Groups Bypasser (rgthree), Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, FluxKontextMultiReferenceLatentMethod, GetNode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, QwenEditConfigPreparer, ReferenceLatent, SaveImage, Switch any [Crystools], TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader, ZML_BooleanSwitch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【CQ808】局部重绘_擦除-2511+Klein去掉路人（加遮罩）_2058837262137389058.json, 图片生成/图生图/动漫转真人_2039329521362542594.json, 图片生成/图生图/局部重绘_擦除-2511+Klein去掉路人（加遮罩）_2054762420068986882.json, 图片生成/图生图/局部重绘_擦除-2511+Klein去掉路人（加遮罩）_2054837099660095490.json, 图片生成/图生图/局部重绘_擦除——2511+Klein裁剪贴回_2030234811285118978.json, 图片生成/图生图/局部重绘_擦除——2511+Klein裁剪贴回_2078684161610706946.json, 图片生成/图生图/局部重绘_擦除——2511+Klein裁剪贴回_2083555609470914561.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_67

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/【CQ808】局部重绘_擦除-2511+Klein去掉路人（加遮罩）_2058837262137389058.json、图片生成/图生图/动漫转真人_2039329521362542594.json、图片生成/图生图/局部重绘_擦除-2511+Klein去掉路人（加遮罩）_2054762420068986882.json、图片生成/图生图/局部重绘_擦除-2511+Klein去掉路人（加遮罩）_2054837099660095490.json、图片生成/图生图/局部重绘_擦除——2511+Klein裁剪贴回_2030234811285118978.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `Fast Groups Bypasser (rgthree)`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `ReferenceLatent`
- `SaveImage`
- `Switch any [Crystools]`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `ZML_BooleanSwitch`

**可变部分**（部分 workflow 才有）：
- `CropWithPadInfo` —— 6/7 个有
- `HAIGC_SaveImagesToZip` —— 6/7 个有
- `InpaintCrop` —— 6/7 个有
- `InpaintStitch` —— 6/7 个有
- `Int` —— 6/7 个有
- `LayerUtility: PurgeVRAM V2` —— 6/7 个有
- `QwenEditOutputExtractor` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `TextEncodeQwenImageEdit` —— 6/7 个有
- `easy positive` —— 6/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `MuyeTextEditOutput` —— 1/7 个有
- `QwenEditOutputExtractor_EditUtils` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy imageSizeByLongerSide` —— 1/7 个有
- `easy promptConcat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 6 - 9 | 7 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler_ancestral | - | 7 | 86% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 6 - 9，7 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（11/7 个样本）：Steps较低可能导致细节不足
