---
name: unknown_workflow_upscale_sampler_clip_48
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9115
common_nodes: [AdvancedLyingSigmaSampler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageUpscaleWithModel, KSampler, KSamplerSelect, LG_Color_Match_V2, LoadImage, PainterFluxImageEdit, PreviewImage, SaveImage, UNETLoader, UltimateSDUpscaleCustomSample, Upscale Model Loader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/z-image+klein 无损放大_1993895232116817922.json, 图片生成/图生图/多角度人物角色一致性批量放大丨批量去ai感一致性衍生lora训练集_2031226327549874178.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_48

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/z-image+klein 无损放大_1993895232116817922.json、图片生成/图生图/多角度人物角色一致性批量放大丨批量去ai感一致性衍生lora训练集_2031226327549874178.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `AdvancedLyingSigmaSampler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LG_Color_Match_V2`
- `LoadImage`
- `PainterFluxImageEdit`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscaleCustomSample`
- `Upscale Model Loader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchCount+` —— 1/2 个有
- `Display Int (rgthree)` —— 1/2 个有
- `ImageBatchMultiple+` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `JWFloat` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
