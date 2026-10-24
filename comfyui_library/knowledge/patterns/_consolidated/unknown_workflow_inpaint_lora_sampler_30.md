---
name: unknown_workflow_inpaint_lora_sampler_30
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.94425
common_nodes: [BBoxesToSAM2, CLIPLoader, CLIPTextEncode, CR Prompt Text, DownloadAndLoadQwenModel, INPAINT_ExpandMask, InpaintModelConditioning, InvertMask, KSampler, LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, MaskPreview+, ModelSamplingSD3, PathchSageAttentionKJ, QwenVLDetection, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/最强万相wan2.2图生图官方版+Qwen2.5Vl带保护洗图_1951490098238050305.json, 图片生成/文生图/(贞贞版)Qwen Image+Wan2.2文生图(文字保护版)V1_1952796766246735873.json, 图片生成/文生图/Qwen Image+Wan2.2文生图(文字保护版)V1_1953085732766289921.json, 图片生成/文生图/文生图（Qwen-Image + Wan2.1 ）文字保护_1953262749519441921.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_30

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/最强万相wan2.2图生图官方版+Qwen2.5Vl带保护洗图_1951490098238050305.json、图片生成/文生图/(贞贞版)Qwen Image+Wan2.2文生图(文字保护版)V1_1952796766246735873.json、图片生成/文生图/Qwen Image+Wan2.2文生图(文字保护版)V1_1953085732766289921.json、图片生成/文生图/文生图（Qwen-Image + Wan2.1 ）文字保护_1953262749519441921.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `BBoxesToSAM2`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `DownloadAndLoadQwenModel`
- `INPAINT_ExpandMask`
- `InpaintModelConditioning`
- `InvertMask`
- `KSampler`
- `LayerMask: LoadSAM2Model`
- `LayerMask: SAM2UltraV2`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `QwenVLDetection`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `MaskToImage` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `SeedVR2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 4 | 75% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 3.5 | 4 | 62% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 0.1 - 1 | 4 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 3.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，4 个样本，取值分散，一致性仅 50%
