---
name: unknown_workflow_controlnet_inpaint_lora_5
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.899333
common_nodes: [AutoCropFaces, CFGNorm, CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), ImageStitch, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image Edit 2511全自动换脸_2029484088595324930.json, 图片生成/图生图/QwenEdit2509自动换脸_2003655192228864001.json, 图片生成/图生图/QwenEdit2511全自动换脸工作流_2003037133550043137.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit 2511全自动换脸_2029484088595324930.json、图片生成/图生图/QwenEdit2509自动换脸_2003655192228864001.json、图片生成/图生图/QwenEdit2511全自动换脸工作流_2003037133550043137.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `AutoCropFaces`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageStitch`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.65 | 0.6 - 0.65 | 3 | 96% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.65，观测区间 0.6 - 0.65，3 个样本，取值集中（一致性 96%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
