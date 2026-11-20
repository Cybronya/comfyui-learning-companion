---
name: image_to_image_lora_sampler_clip_143
type: Image To Image
frequency: 2
level: weak
coverage: 0.955
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, PreviewImage, SaveImage, UNETLoader, USOStyleReference, VAEDecode, VAEEncode, VAELoader, workflow>USO]
problems: []
missing: []
members: [图片生成/图生图/flux-uso画风迁移+高清放大_1965773609602035713.json, 图片生成/图生图/风格迁移，画风迁移，USO-flux_1965685261780795394.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_143

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux-uso画风迁移+高清放大_1965773609602035713.json、图片生成/图生图/风格迁移，画风迁移，USO-flux_1965685261780795394.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `USOStyleReference`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `workflow>USO`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 1/2 个有
- `ImageScaleToMaxDimension` —— 1/2 个有
- `LayerFilter: GaussianBlur` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
