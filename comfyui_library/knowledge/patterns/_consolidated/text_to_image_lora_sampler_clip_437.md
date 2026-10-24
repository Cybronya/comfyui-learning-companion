---
name: text_to_image_lora_sampler_clip_437
type: Text To Image
frequency: 4
level: weak
coverage: 0.554
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, PreviewAny, PrimitiveBoolean, PrimitiveStringMultiline, ResolutionSelector, SaveImage, StringConcatenate, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 Turbo 微调文生图 (内)_2073841889299750914.json, 图片生成/文生图/Krea2 Turbo微调文生图，人像写真创意形象内测版_2110785893324910593.json, 图片生成/文生图/Krea2_Turbo_微调文生图_(内)_2111636038694293505.json, 图片生成/文生图/krea2-turbo文生图fp8版｜低显存快速出图好上手_2111062930363084801.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_437

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2 Turbo 微调文生图 (内)_2073841889299750914.json、图片生成/文生图/Krea2 Turbo微调文生图，人像写真创意形象内测版_2110785893324910593.json、图片生成/文生图/Krea2_Turbo_微调文生图_(内)_2111636038694293505.json、图片生成/文生图/krea2-turbo文生图fp8版｜低显存快速出图好上手_2111062930363084801.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `StringConcatenate`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `RHHiddenNodes` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `ZML_IntegerFloatConverter` —— 3/4 个有
- `easy prompt` —— 3/4 个有
- `JjkText` —— 2/4 个有
- `solarL_SaveImagesToZip` —— 2/4 个有
- `孤海注释` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 552 | 80 - 1024 | 4 | 14% |
| 高度 | 552 | 80 - 1024 | 4 | 14% |
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 4 | 36% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 552，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 14%
- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
