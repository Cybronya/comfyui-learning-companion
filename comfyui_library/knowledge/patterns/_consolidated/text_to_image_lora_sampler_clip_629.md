---
name: text_to_image_lora_sampler_clip_629
type: Text To Image
frequency: 2
level: weak
coverage: 0.907
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImpactInt, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Seedance专属三视图！超级角色资产库：简单指令，万象资产_文生图_角色设计_2040049722169233409.json, 图片生成/文生图/多套文生图对比 Z-Image _ Krea2 _ Qwen-Image_ Klein2_2090635217290752001.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_629

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Seedance专属三视图！超级角色资产库：简单指令，万象资产_文生图_角色设计_2040049722169233409.json、图片生成/文生图/多套文生图对比 Z-Image _ Krea2 _ Qwen-Image_ Klein2_2090635217290752001.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImpactInt`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `PainterFluxImageEdit` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 792 | - | 2 | 91% |
| 高度 | 1300 | - | 2 | 98% |
| 采样步数 | 9.5 | - | 2 | 95% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | bong_tangent | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 792，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- 高度 中位数 1300，样本不足，未给区间，2 个样本，取值集中（一致性 98%）
- 采样步数 中位数 9.5，样本不足，未给区间，2 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 bong_tangent，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
