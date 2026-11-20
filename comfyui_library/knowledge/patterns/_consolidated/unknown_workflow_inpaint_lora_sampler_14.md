---
name: unknown_workflow_inpaint_lora_sampler_14
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.945
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageCrop, ImageGenResolutionFromImage, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ACE++_Portrait_Reface_换脸_1956950372058107905.json, 图片生成/图生图/M_ACE_Plus_LoRA_subject_refence主体一致性生成_1956725732975022081.json, 图片生成/图生图/Scepter-ace ++ 更方便地更换所有东西_1911609850827108353.json, 图片生成/图生图/服装图案迁移_1900869896836915201.json, 平台全量/ACE++_1900446190285090817.json, 平台全量/ACE++换脸物品迁移文字交互_1914492547505553410.json, 平台全量/Ace指定物品指定场景迁移【AI小王子】_1915597965904515074.json, 平台全量/Scepter-ACE Plus ++ replaces everything_1888054181469511681.json, 平台全量/一键超自然换脸 脸部遮罩迁移 flux portrait  高还原度 一键脸部超自然迁移_1999664835598184450.json, 平台全量/服装图案迁移工作流（Flux Fill+Ace++）_1964876963393490946.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/ACE++_Portrait_Reface_换脸_1956950372058107905.json、图片生成/图生图/M_ACE_Plus_LoRA_subject_refence主体一致性生成_1956725732975022081.json、图片生成/图生图/Scepter-ace ++ 更方便地更换所有东西_1911609850827108353.json、图片生成/图生图/服装图案迁移_1900869896836915201.json、平台全量/ACE++_1900446190285090817.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
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
- `EmptyImage` —— 9/10 个有
- `ImageConcanate` —— 9/10 个有
- `ImageResize+` —— 9/10 个有
- `ImageToMask` —— 9/10 个有
- `MaskToImage` —— 9/10 个有
- `PreviewImage` —— 8/10 个有
- `ImagePadForOutpaint` —— 5/10 个有
- `RMBG` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `LoadImageFromUrl` —— 2/10 个有
- `Note Plus (mtb)` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `DeepTranslatorTextNode` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `ImageScale` —— 1/10 个有
- `SUPIR_Upscale` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 20 - 50 | 10 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | normal | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 20 - 50，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 normal，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
