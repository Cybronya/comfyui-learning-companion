---
name: image_to_image_controlnet_lora_sampler
type: Image To Image
frequency: 2
level: weak
coverage: 0.778
common_nodes: [AIO_Preprocessor, CFGNorm, CLIPLoader, ControlNetApplySD3, ControlNetLoader, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, OpenposePreprocessor, PreviewImage, SaveImage, SetUnionControlNetType, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/文生图/1962818248989360130.json, 图片生成/文生图/1963114897561333762.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1962818248989360130.json、图片生成/文生图/1963114897561333762.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CFGNorm`
- `CLIPLoader`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `OpenposePreprocessor`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | - | 2 | 100% |
| 高度 | 720 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 1.5 | - | 2 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1.5，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
