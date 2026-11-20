---
name: image_to_image_lora_sampler_clip_124
type: Image To Image
frequency: 2
level: weak
coverage: 0.8235
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, EasyCache, FluxGuidance, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ReferenceLatent, RunningHub USO Loader, RunningHub USO Sampler, SaveImage, UNETLoader, USOStyleReference, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/36.tonnie-USO风格迁移(效果不好)_2003831545192431618.json, 图片生成/图生图/USO加速版CF原版和RH开源版对比_1963876116412993538.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_124

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/36.tonnie-USO风格迁移(效果不好)_2003831545192431618.json、图片生成/图生图/USO加速版CF原版和RH开源版对比_1963876116412993538.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EasyCache`
- `FluxGuidance`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ReferenceLatent`
- `RunningHub USO Loader`
- `RunningHub USO Sampler`
- `SaveImage`
- `UNETLoader`
- `USOStyleReference`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AnyLineArtPreprocessor_aux` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Seed Everywhere` —— 1/2 个有
- `easy imagePixelPerfect` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16.5 | - | 2 | 48% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.75 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 16.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
