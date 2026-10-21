---
name: image_to_image_lora_sampler_clip_19
type: Image To Image
frequency: 2
level: weak
coverage: 0.6805
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [LayerMask: LoadFlorence2Model, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: Florence2Image2Prompt]
members: [图片生成/文生图/1956293805874008065.json, 图片生成/文生图/28.tonnie-Wan2.2文生图、洗图工作流_2001258902077534210.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1956293805874008065.json、图片生成/文生图/28.tonnie-Wan2.2文生图、洗图工作流_2001258902077534210.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanVideo15Latent` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerMask: LoadFlorence2Model` —— 1/2 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | bong_tangent | - | 2 | 50% |
| 重绘幅度 | 0.3 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 bong_tangent，2 个样本，一致性 50%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: LoadFlorence2Model、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: Florence2Image2Prompt
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
