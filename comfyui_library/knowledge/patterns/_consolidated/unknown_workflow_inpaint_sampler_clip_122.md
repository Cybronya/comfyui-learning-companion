---
name: unknown_workflow_inpaint_sampler_clip_122
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6915
common_nodes: [Any Switch (rgthree), Anything Everywhere3, CLIPTextEncode, CM_IntToNumber, CM_NumberToInt, CM_NumberUnaryOperation, CheckpointLoaderSimple, ColorMatch, ConditioningZeroOut, DF_Float, DF_Image_scale_to_side, DF_Integer, DF_Text, DualCLIPLoader, Fast Groups Bypasser (rgthree), Florence2ModelLoader, Florence2Run, GrowMaskWithBlur, INPAINT_ApplyFooocusInpaint, INPAINT_LoadFooocusInpaint, INPAINT_VAEEncodeInpaintConditioning, Image Comparer (rgthree), ImageAndMaskPreview, ImageResizeKJ, ImageToMask, InpaintModelConditioning, Int, KSampler, LayerUtility: CropByMask, LayerUtility: RestoreCropBox, LoadImage, Mask Fill Holes, MaskToImage, PreviewImage, ResizeMask, SaveImage, SimpleCondition+, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageSize, easy isMaskEmpty, easy mathInt, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/XL-Flux万物消除工作流，元素消除_1929815311917203457.json, 平台全量/一键消除_1930147445211086849.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_122

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/XL-Flux万物消除工作流，元素消除_1929815311917203457.json、平台全量/一键消除_1930147445211086849.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CM_IntToNumber`
- `CM_NumberToInt`
- `CM_NumberUnaryOperation`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ConditioningZeroOut`
- `DF_Float`
- `DF_Image_scale_to_side`
- `DF_Integer`
- `DF_Text`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Florence2ModelLoader`
- `Florence2Run`
- `GrowMaskWithBlur`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_VAEEncodeInpaintConditioning`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerUtility: CropByMask`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewImage`
- `ResizeMask`
- `SaveImage`
- `SimpleCondition+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy isMaskEmpty`
- `easy mathInt`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BRIA_RMBG_ModelLoader_Zho` —— 1/2 个有
- `BRIA_RMBG_Zho` —— 1/2 个有
- `BiRefNet_ModelLoader_Zho` —— 1/2 个有
- `BiRefNet_Zho` —— 1/2 个有
- `InspyrenetRembgAdvanced` —— 1/2 个有
- `LamaRemover` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/2 个有
- `LayerUtility: LaMa` —— 1/2 个有
- `Load Image Batch` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy positive` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1.5 | - | 2 | 67% |
| 采样算法 | dpmpp_sde | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 0.525 | - | 2 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1.5，样本不足，未给区间，2 个样本
- 采样算法 最常用 dpmpp_sde，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 0.525，样本不足，未给区间，2 个样本
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
