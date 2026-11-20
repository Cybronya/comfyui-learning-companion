---
name: text_to_image_controlnet_inpaint_lora_8
type: Text To Image
frequency: 2
level: weak
coverage: 0.644
common_nodes: [Anything Everywhere3, ApplyInstantID, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, DifferentialDiffusion, EmptyLatentImage, GetNode, ImageSmartSharpen+, InpaintCrop, InpaintModelConditioning, InpaintStitch, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RebatchLatents, SaveImage, SetNode, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/✅Qwen_edit 一致性 分镜 单图提示指定姿势_换姿势_1958415335294713858.json, 平台全量/🈚️qwen image Edit 多图编辑_1959494640980406273.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/✅Qwen_edit 一致性 分镜 单图提示指定姿势_换姿势_1958415335294713858.json、平台全量/🈚️qwen image Edit 多图编辑_1959494640980406273.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `ApplyInstantID`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `EmptyLatentImage`
- `GetNode`
- `ImageSmartSharpen+`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RebatchLatents`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ImageBatchToList` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `ImpactMakeImageBatch` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `Text` —— 1/2 个有
- `Wan22PromptSelector` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 0.75 | - | 2 | 67% |
| 宽度 | 960 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 0.75，样本不足，未给区间，2 个样本
- 宽度 中位数 960，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（6/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
