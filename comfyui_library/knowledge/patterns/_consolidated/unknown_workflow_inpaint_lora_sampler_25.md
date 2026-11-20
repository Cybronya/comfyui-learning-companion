---
name: unknown_workflow_inpaint_lora_sampler_25
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.94975
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageCrop, ImageGenResolutionFromImage, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ACE++_Portrait_Reface_换脸_1956950372058107905.json, 图片生成/图生图/M_ACE_Plus_LoRA_subject_refence主体一致性生成_1956725732975022081.json, 图片生成/图生图/Scepter-ace ++ 更方便地更换所有东西_1911609850827108353.json, 图片生成/图生图/服装图案迁移_1900869896836915201.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/ACE++_Portrait_Reface_换脸_1956950372058107905.json、图片生成/图生图/M_ACE_Plus_LoRA_subject_refence主体一致性生成_1956725732975022081.json、图片生成/图生图/Scepter-ace ++ 更方便地更换所有东西_1911609850827108353.json、图片生成/图生图/服装图案迁移_1900869896836915201.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageCrop`
- `ImageGenResolutionFromImage`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 3/4 个有
- `ImageConcanate` —— 3/4 个有
- `ImageResize+` —— 3/4 个有
- `ImageToMask` —— 3/4 个有
- `MaskToImage` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ImagePadForOutpaint` —— 2/4 个有
- `LoadImageFromUrl` —— 2/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `RMBG` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 23 - 28 | 4 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 23 - 28，4 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
