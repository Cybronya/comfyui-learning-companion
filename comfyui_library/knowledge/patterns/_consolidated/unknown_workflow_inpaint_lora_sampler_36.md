---
name: unknown_workflow_inpaint_lora_sampler_36
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.936
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, GetImageSize+, Image Comparer (rgthree), ImageConcanate, ImageCrop+, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, KSamplerAdvanced, LayerMask: MaskStroke, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MaskToImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageInsetCrop, easy imageRemBg, easy imageSize, easy makeImageForICLora]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX高精度万物迁移_1985765112948695042.json, 图片生成/图生图/换内衣改，只上传涂抹，不要动其他的_2096872904851021825.json, 图片生成/图生图/新完美迁移服装 内衣_1963438376848396289.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX高精度万物迁移_1985765112948695042.json、图片生成/图生图/换内衣改，只上传涂抹，不要动其他的_2096872904851021825.json、图片生成/图生图/新完美迁移服装 内衣_1963438376848396289.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageCrop+`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `KSamplerAdvanced`
- `LayerMask: MaskStroke`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageInsetCrop`
- `easy imageRemBg`
- `easy imageSize`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `BaiduTranslateNode` —— 1/3 个有
- `CR Latent Batch Size` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `easy ifElse` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 20 | 3 | 0% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 20，3 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
