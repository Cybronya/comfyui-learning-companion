---
name: text_to_image_lora_sampler_clip_305
type: Text To Image
frequency: 3
level: strong
coverage: 0.845333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Seed, CR Text, ConditioningZeroOut, EmptyLatentImage, KSampler, LoraLoaderModelOnly, RH_LLMAPI_Pro_Node, SaveImage, Text Concatenate, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Z-image 文生图-细节增强器工作流_1995383488809512962.json, 图片生成/文生图/Z-image-渔网丝袜网红批量产图，提示词智能扩写_1995497624583208962.json, 图片生成/文生图/Z-image-网红批量产图，提示词扩写LorA版_1995322387870756865.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_305

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image 文生图-细节增强器工作流_1995383488809512962.json、图片生成/文生图/Z-image-渔网丝袜网红批量产图，提示词智能扩写_1995497624583208962.json、图片生成/文生图/Z-image-网红批量产图，提示词扩写LorA版_1995322387870756865.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Seed`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `MuyeTextEditOutput` —— 2/3 个有
- `ProcessString` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `Image Compare (mtb)` —— 1/3 个有
- `easy float` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 3 | 100% |
| 高度 | 1480 | 1480 - 1920 | 3 | 87% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1480，观测区间 1480 - 1920，3 个样本，取值集中（一致性 87%）
