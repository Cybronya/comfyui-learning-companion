---
name: unknown_workflow_inpaint_lora_sampler_2
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.817
common_nodes: [BBoxesToSAM2, CLIPLoader, CLIPTextEncode, CR Prompt Text, DownloadAndLoadQwenModel, EmptySD3LatentImage, INPAINT_ExpandMask, InpaintModelConditioning, InvertMask, JWInteger, KSampler, LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, MaskPreview+, ModelSamplingAuraFlow, ModelSamplingSD3, PathchSageAttentionKJ, QwenVLDetection, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: [LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, CR Prompt Text, MaskPreview+]
members: [图片生成/文生图/(贞贞版)Qwen Image+Wan2.2文生图(文字保护版)V1_1952796766246735873.json, 图片生成/文生图/1953085732766289921.json, 图片生成/文生图/1953262749519441921.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/(贞贞版)Qwen Image+Wan2.2文生图(文字保护版)V1_1952796766246735873.json、图片生成/文生图/1953085732766289921.json、图片生成/文生图/1953262749519441921.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `BBoxesToSAM2`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `DownloadAndLoadQwenModel`
- `EmptySD3LatentImage`
- `INPAINT_ExpandMask`
- `InpaintModelConditioning`
- `InvertMask`
- `JWInteger`
- `KSampler`
- `LayerMask: LoadSAM2Model`
- `LayerMask: SAM2UltraV2`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `QwenVLDetection`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `PreviewImage` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: LoadSAM2Model、LayerMask: SAM2UltraV2、LayerUtility: PurgeVRAM、CR Prompt Text、MaskPreview+
