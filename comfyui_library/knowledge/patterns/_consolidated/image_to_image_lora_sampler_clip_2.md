---
name: image_to_image_lora_sampler_clip_2
type: Image To Image
frequency: 4
level: moderate
coverage: 0.8265
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, Mask Fill Holes]
members: [comfyui-workflow-templates-json/image_qwen_image_controlnet_patch.json, 图片生成/图生图/2061789555824615425.json, 图片生成/图生图/2069046278197174274.json, 图片生成/图生图/2078101582297788417.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/image_qwen_image_controlnet_patch.json、图片生成/图生图/2061789555824615425.json、图片生成/图生图/2069046278197174274.json、图片生成/图生图/2078101582297788417.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AnimaLLLiteApply` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `SetLatentNoiseMask` —— 3/4 个有
- `Mask Fill Holes` —— 2/4 个有
- `Canny` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `MaskFillHoles` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `QwenImageDiffsynthControlnet` —— 1/4 个有
- `ToriiGateT8_GroundingBuilder` —— 1/4 个有
- `ToriiGateT8_LlamaCppVisionGenerate` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 4 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | er_sde | - | 4 | 75% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 er_sde，4 个样本，一致性 75%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、Mask Fill Holes
