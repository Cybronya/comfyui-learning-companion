---
name: unknown_workflow_lora_sampler_clip_73
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.838
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CheckpointLoaderSimple, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [CR String To Combo, Primitive string [Crystools], Text Multiline]
members: [图片生成/文生图/1952911676233478146.json, 图片生成/文生图/1955200823770976258.json, 图片生成/文生图/美食类游戏蛋糕_1866768530052988929.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1952911676233478146.json、图片生成/文生图/1955200823770976258.json、图片生成/文生图/美食类游戏蛋糕_1866768530052988929.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `TextCombinerTwo` —— 2/3 个有
- `CR String To Combo` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `Primitive string [Crystools]` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1280 | 1280 - 1536 | 3 | 91% |
| LoRA 模型强度 | 1 | 0.45 - 1 | 3 | 68% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1536，3 个样本，取值集中（一致性 91%）
- LoRA 模型强度 中位数 1，观测区间 0.45 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR String To Combo、Primitive string [Crystools]、Text Multiline
