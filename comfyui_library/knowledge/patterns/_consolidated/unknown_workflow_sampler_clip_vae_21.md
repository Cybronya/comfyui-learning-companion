---
name: unknown_workflow_sampler_clip_vae_21
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7532
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [Label (rgthree), CR Text Input Switch (4 way)]
members: [图片生成/文生图/1912796321265217537.json, 图片生成/文生图/1917393981133754370.json, 图片生成/文生图/1920028263266324482.json, 图片生成/文生图/1938488997612027905.json, 图片生成/文生图/1940662965035233282.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_21

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1912796321265217537.json、图片生成/文生图/1917393981133754370.json、图片生成/文生图/1920028263266324482.json、图片生成/文生图/1938488997612027905.json、图片生成/文生图/1940662965035233282.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 4/5 个有
- `JjkText` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `TextCombinerTwo` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `CR Text Input Switch (4 way)` —— 3/5 个有
- `RH_Prompter` —— 3/5 个有
- `LoraLoader` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `ArgosTranslateTextNode` —— 1/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `ShowText` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1280 | 1280 - 1536 | 5 | 92% |
| LoRA 模型强度 | 1.1 | - | 2 | 91% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1536，5 个样本，取值集中（一致性 92%）
- LoRA 模型强度 中位数 1.1，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、CR Text Input Switch (4 way)
