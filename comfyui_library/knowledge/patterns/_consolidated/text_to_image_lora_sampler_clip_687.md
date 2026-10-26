---
name: text_to_image_lora_sampler_clip_687
type: Text To Image
frequency: 2
level: weak
coverage: 0.908
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt List, Color Correct (mtb), ColorMatch, ConditioningZeroOut, Convert Color Space, EmptyLatentImage, Get Image Size, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImpactInt, ImpactMinMax, KSampler, LayerColor: ColorBalance, LoraLoader, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, String Literal, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Zimage+seedVR2 放大+双lora修复质感增强_1996864875378921474.json, 图片生成/文生图/【4K超清出片】Zimage+双lora&bf16修复+seedVR2放大_1994787830675202049.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_687

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Zimage+seedVR2 放大+双lora修复质感增强_1996864875378921474.json、图片生成/文生图/【4K超清出片】Zimage+双lora&bf16修复+seedVR2放大_1994787830675202049.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt List`
- `Color Correct (mtb)`
- `ColorMatch`
- `ConditioningZeroOut`
- `Convert Color Space`
- `EmptyLatentImage`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactInt`
- `ImpactMinMax`
- `KSampler`
- `LayerColor: ColorBalance`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `String Literal`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1280 | - | 2 | 100% |
| 高度 | 720 | - | 2 | 100% |
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 50% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 0.15 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.15，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
