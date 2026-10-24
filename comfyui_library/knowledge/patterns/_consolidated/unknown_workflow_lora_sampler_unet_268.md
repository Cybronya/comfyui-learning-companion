---
name: unknown_workflow_lora_sampler_unet_268
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.745
common_nodes: [Anything Everywhere, CFGNorm, CLIPLoader, CR Text, ConditioningZeroOut, EmptyLatentImage, FluxKontextMultiReferenceLatentMethod, GetNode, Image Comparer (rgthree), JjkText, JoinImageWithAlpha, KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, Mask Invert, MaskPreview+, ModelSamplingAuraFlow, SDMatteApply, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/【阿良绘】多风格内嵌改图 _ 三维_卡通_扁平_漫画_等_2015607390426636290.json, 图片生成/图生图/【阿良绘】毛毡风格化+抠图 _ 风格Lora+Light加速_2013810071653847042.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_268

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【阿良绘】多风格内嵌改图 _ 三维_卡通_扁平_漫画_等_2015607390426636290.json、图片生成/图生图/【阿良绘】毛毡风格化+抠图 _ 风格Lora+Light加速_2013810071653847042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `Image Comparer (rgthree)`
- `JjkText`
- `JoinImageWithAlpha`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `Mask Invert`
- `MaskPreview+`
- `ModelSamplingAuraFlow`
- `SDMatteApply`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `easy promptList` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 0.9 | - | 2 | 89% |
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1.25 | - | 2 | 80% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1.25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
