---
name: text_to_image_controlnet_inpaint_sampler_2
type: Text To Image
frequency: 3
level: strong
coverage: 0.657
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetInpaintingAliMamaApply, ControlNetLoader, DetailerForEach, DualCLIPLoader, EmptyLatentImage, ImagePadForOutpaint, InpaintPreprocessor, KSampler, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToSEGS, MathExpression|pysssss, SaveImage, ShowText|pysssss, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX自由扩图_2034618260989157377.json, 图片生成/图生图/任意方向智能完美扩图，让AI成为你的“画布魔术师”_1968677852973604866.json, 平台全量/Flux-反推重绘-扩图_1949809310090092546.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_sampler_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX自由扩图_2034618260989157377.json、图片生成/图生图/任意方向智能完美扩图，让AI成为你的“画布魔术师”_1968677852973604866.json、平台全量/Flux-反推重绘-扩图_1949809310090092546.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `DetailerForEach`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `ImagePadForOutpaint`
- `InpaintPreprocessor`
- `KSampler`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToSEGS`
- `MathExpression|pysssss`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `LayerMask: MaskPreview` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `AnySwitch` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `GroupSwitcher` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `Int` —— 1/3 个有
- `Primitive float [Crystools]` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
