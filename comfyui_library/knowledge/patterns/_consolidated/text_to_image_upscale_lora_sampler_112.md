---
name: text_to_image_upscale_lora_sampler_112
type: Text To Image
frequency: 2
level: weak
coverage: 0.857
common_nodes: [ApplyFBCacheOnModel, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), ImageScaleBy, ImageStitch, ImageUpscaleWithModel, KSampler, LoadAndResizeImage, LoraLoader, NunchakuFluxDiTLoader, NunchakuTextEncoderLoaderV2, ReferenceLatent, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/kontext-双nunchaku急速修复工作流_1942396650398879746.json, 图片生成/图生图/图片转精细线稿工作流_1971036122581241857.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_112

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/kontext-双nunchaku急速修复工作流_1942396650398879746.json、图片生成/图生图/图片转精细线稿工作流_1971036122581241857.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageStitch`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadAndResizeImage`
- `LoraLoader`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoaderV2`
- `ReferenceLatent`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| LoRA 模型强度 | 0.2 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
