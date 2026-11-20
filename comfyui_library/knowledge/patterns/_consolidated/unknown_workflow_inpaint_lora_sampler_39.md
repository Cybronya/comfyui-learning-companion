---
name: unknown_workflow_inpaint_lora_sampler_39
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.91925
common_nodes: [ApplyPulidFlux, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, InpaintModelConditioning, KSampler, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PulidFluxModelLoader, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/Flux+Rudex万物迁移——完美解决人设固定：A图+B图_1915275990954872833.json, 图片生成/图生图/Q-人像迁移_1955974460753018882.json, 平台全量/flux人像迁移（与闺蜜合照）_1936053225705361410.json, 平台全量/万物迁移-人物_1904722465120288770.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_39

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux+Rudex万物迁移——完美解决人设固定：A图+B图_1915275990954872833.json、图片生成/图生图/Q-人像迁移_1955974460753018882.json、平台全量/flux人像迁移（与闺蜜合照）_1936053225705361410.json、平台全量/万物迁移-人物_1904722465120288770.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PulidFluxModelLoader`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 3/4 个有
- `CropFace` —— 3/4 个有
- `FluxGuidance` —— 3/4 个有
- `InspyrenetRembg` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `PulidFluxEvaClipLoader` —— 3/4 个有
- `PulidFluxInsightFaceLoader` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Florence2ModelLoader` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `ImageCrop+` —— 2/4 个有
- `MaskPreview+` —— 2/4 个有
- `CLIPTextEncodeFlux` —— 1/4 个有
- `EcomIDEvaClipLoader` —— 1/4 个有
- `ImageCrop` —— 1/4 个有
- `InstantIDFaceAnalysis` —— 1/4 个有
- `Joy_caption_two` —— 1/4 个有
- `Joy_caption_two_load` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有
- `ttN concat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 25 - 30 | 4 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 25 - 30，4 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
