---
name: unknown_workflow_inpaint_lora_sampler_24
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.898
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, GetImageSizeAndCount, ImageConcanate, InpaintModelConditioning, Int, KSampler, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/生图-单图编辑局部重绘-qwen-Edit-2511-8步_2008072169342898178.json, 图片生成/图生图/生图-双图编辑万物迁移-qwen-Edit-2511-8步_2008076301256626177.json, 图片生成/图生图/生图-图人物换发色-qwen-Edit-2511-8步_1984213663554945025.json, 图片生成/图生图/生图-图换脸-qwen-Edit-2511-8步_1984207219174555649.json, 图片生成/图生图/生图-图换脸换头-qwen-Edit-2511-8步_1984213703052640257.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/生图-单图编辑局部重绘-qwen-Edit-2511-8步_2008072169342898178.json、图片生成/图生图/生图-双图编辑万物迁移-qwen-Edit-2511-8步_2008076301256626177.json、图片生成/图生图/生图-图人物换发色-qwen-Edit-2511-8步_1984213663554945025.json、图片生成/图生图/生图-图换脸-qwen-Edit-2511-8步_1984207219174555649.json、图片生成/图生图/生图-图换脸换头-qwen-Edit-2511-8步_1984213703052640257.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/5 个有
- `DifferentialDiffusion` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `LayerMask: PersonMaskUltra V2` —— 3/5 个有
- `MaskToSEGS` —— 3/5 个有
- `SegsToCombinedMask` —— 3/5 个有
- `ModelSamplingAuraFlow` —— 2/5 个有
- `ReActorFaceSwap` —— 2/5 个有
- `ImageAndMaskPreview` —— 1/5 个有
- `Mask Invert` —— 1/5 个有
- `MaskToImage` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.7 - 1 | 5 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，5 个样本，取值集中（一致性 83%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
