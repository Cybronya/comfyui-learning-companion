---
name: image_to_image_lora_sampler_clip_12
type: Image To Image
frequency: 2
level: weak
coverage: 0.697
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy imageInsetCrop, LayerUtility: ImageReel, LayerUtility: ImageReelComposit]
members: [图片生成/图生图/1962753115034370050.json, 图片生成/文生图/1939535808275857410.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/1962753115034370050.json、图片生成/文生图/1939535808275857410.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowStringText` —— 1/2 个有
- `CropFace` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `easy imageInsetCrop` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | - | 2 | 83% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy imageInsetCrop、LayerUtility: ImageReel、LayerUtility: ImageReelComposit
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
