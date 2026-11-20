---
name: text_to_image_upscale_sampler_clip_33
type: Text To Image
frequency: 4
level: moderate
coverage: 0.90225
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/国漫cg风格-Z-image_2046874150148509697.json, 图片生成/文生图/女装工作流_2009116986424430593.json, 图片生成/文生图/最新文生图，使用简单，不用担心不会写提示词_2046452778989522945.json, 图片生成/文生图/绅士美学 文生图Z-image_2038118307076775937.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/国漫cg风格-Z-image_2046874150148509697.json、图片生成/文生图/女装工作流_2009116986424430593.json、图片生成/文生图/最新文生图，使用简单，不用担心不会写提示词_2046452778989522945.json、图片生成/文生图/绅士美学 文生图Z-image_2038118307076775937.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageSharpen` —— 2/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `scale` —— 2/4 个有
- `CR Prompt List` —— 1/4 个有
- `Int` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `ProcessString` —— 1/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有
- `easy forLoopEnd` —— 1/4 个有
- `easy forLoopStart` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 9 | 4 | 0% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.85 | - | 2 | 94% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1052 | 1024 - 1440 | 4 | 85% |
| 高度 | 1728 | 1536 - 1920 | 4 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 9，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 1024 - 1440，4 个样本，取值集中（一致性 85%）
- 高度 中位数 1728，观测区间 1536 - 1920，4 个样本，取值集中（一致性 89%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
