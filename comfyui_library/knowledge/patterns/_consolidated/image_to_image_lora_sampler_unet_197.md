---
name: image_to_image_lora_sampler_unet_197
type: Image To Image
frequency: 2
level: weak
coverage: 0.922
common_nodes: [CFGNorm, CLIPLoader, CR Image Input Switch, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/BFS QwenEdit 2509 _ 2511 换头换脸 + 換背景_2081405625912881154.json, 图片生成/图生图/BFS QwenEdit 2509 _ 2511 换头换脸_2019938986193592321.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_197

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/BFS QwenEdit 2509 _ 2511 换头换脸 + 換背景_2081405625912881154.json、图片生成/图生图/BFS QwenEdit 2509 _ 2511 换头换脸_2019938986193592321.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Image Input Switch`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `CompressImages` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `easy textSwitch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
