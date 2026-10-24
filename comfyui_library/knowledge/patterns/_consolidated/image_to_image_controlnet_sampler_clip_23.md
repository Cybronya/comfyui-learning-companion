---
name: image_to_image_controlnet_sampler_clip_23
type: Image To Image
frequency: 2
level: weak
coverage: 0.9425
common_nodes: [ApplyInstantID, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/极速换脸xl-30秒_2039384765387771905.json, 图片生成/文生图/换脸&换装_1995666844927328257.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/极速换脸xl-30秒_2039384765387771905.json、图片生成/文生图/换脸&换装_1995666844927328257.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyInstantID`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `FaceAnalysisModels` —— 1/2 个有
- `FaceBoundingBox` —— 1/2 个有
- `FeatherMask` —— 1/2 个有
- `ImageRandomTransform+` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral_cfg_pp | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.475 | - | 2 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral_cfg_pp，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.475，样本不足，未给区间，2 个样本
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
