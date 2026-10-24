---
name: text_to_image_lora_sampler_clip_653
type: Text To Image
frequency: 2
level: weak
coverage: 0.8905
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, DapaoImageRatioLimitNode, DapaoRandomPromptLineCombineNode, DapaoRandomPromptLineExtractNode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, Note Plus (mtb), SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/🦁Z-image 随机提示词选择+优化VAE 2025-12-29_2005889109249982465.json, 图片生成/文生图/🦁国产之光 Qwen-image2512震撼来袭【随机提示词】_2007451112839843842.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_653

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/🦁Z-image 随机提示词选择+优化VAE 2025-12-29_2005889109249982465.json、图片生成/文生图/🦁国产之光 Qwen-image2512震撼来袭【随机提示词】_2007451112839843842.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `DapaoImageRatioLimitNode`
- `DapaoRandomPromptLineCombineNode`
- `DapaoRandomPromptLineExtractNode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `Note Plus (mtb)`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DapaoSafeSaveImage` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10.5 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1280 | - | 2 | 40% |
| 高度 | 1280 | - | 2 | 40% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10.5，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
