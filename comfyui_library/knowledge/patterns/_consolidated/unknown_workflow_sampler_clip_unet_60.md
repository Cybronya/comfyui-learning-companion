---
name: unknown_workflow_sampler_clip_unet_60
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.912889
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Prompt Text, Lora Loader Stack (rgthree), CR Text, CR Text Concatenate]
members: [图片生成/文生图/1923215248826748929.json, 图片生成/文生图/1923645200881602562.json, 图片生成/文生图/1923655528982245378.json, 图片生成/文生图/1926928747302166529.json, 图片生成/文生图/1927964492725141505.json, 图片生成/文生图/1937783580867084290.json, 图片生成/文生图/1965805471892443137.json, 图片生成/文生图/Flux版IP三视图角色生成_1991794796115210242.json, 图片生成/文生图/英文字体设计_2084095503633043458.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_60

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/1923215248826748929.json、图片生成/文生图/1923645200881602562.json、图片生成/文生图/1923655528982245378.json、图片生成/文生图/1926928747302166529.json、图片生成/文生图/1927964492725141505.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoader` —— 6/9 个有
- `FluxGuidance` —— 4/9 个有
- `CR Text` —— 3/9 个有
- `CR Text Concatenate` —— 3/9 个有
- `PMRF` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `Lora Loader Stack (rgthree)` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1920 | 9 | 61% |
| 高度 | 1080 | 512 - 1536 | 9 | 74% |
| LoRA 模型强度 | 0.8 | 0.4 - 1 | 6 | 68% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1920，9 个样本
- 高度 中位数 1080，观测区间 512 - 1536，9 个样本
- LoRA 模型强度 中位数 0.8，观测区间 0.4 - 1，6 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text、Lora Loader Stack (rgthree)、CR Text、CR Text Concatenate
