---
name: text_to_image_lora_sampler_clip_307
type: Text To Image
frequency: 3
level: strong
coverage: 0.910333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, PiDFinalize, PiDPrepare, PiDSample, PiDTextPrompt, RunningHub Deepcleaner, SaveImage, UNETLoader, VAEDecode, VAELoader, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Z-image-turbo D-OPSD PID文生图4K V2_2059473176723288066.json, 图片生成/文生图/Z-image-turbo D-OPSD PID文生图4K V2_2059830566836596738.json, 图片生成/文生图/Z-image-turbo D-OPSD PID文生图4K_2059544605737177089.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_307

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image-turbo D-OPSD PID文生图4K V2_2059473176723288066.json、图片生成/文生图/Z-image-turbo D-OPSD PID文生图4K V2_2059830566836596738.json、图片生成/文生图/Z-image-turbo D-OPSD PID文生图4K_2059544605737177089.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `PiDFinalize`
- `PiDPrepare`
- `PiDSample`
- `PiDTextPrompt`
- `RunningHub Deepcleaner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `MemoryCleaner` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 576 | 576 - 576 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 576，观测区间 576 - 576，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
