---
name: text_to_image_lora_sampler_clip_268
type: Text To Image
frequency: 4
level: strong
coverage: 0.82675
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImpactSwitch, Int, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen-艺术字体设计_1998994186022084610.json, 图片生成/文生图/创意卡通logo设计-Qwen image_2015701697498193921.json, 图片生成/文生图/创意卡通logo设计-Qwen image_2082720895461838850.json, 图片生成/文生图/艺术字体设计_1990698733262311426.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_268

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen-艺术字体设计_1998994186022084610.json、图片生成/文生图/创意卡通logo设计-Qwen image_2015701697498193921.json、图片生成/文生图/创意卡通logo设计-Qwen image_2082720895461838850.json、图片生成/文生图/艺术字体设计_1990698733262311426.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_NODE` —— 3/4 个有
- `AILab_QwenVL` —— 2/4 个有
- `Image Levels Adjustment` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LayerColor: Brightness & Contrast` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `Text` —— 2/4 个有
- `TextCombinerTwo` —— 2/4 个有
- `easy showAnything` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 3.5 - 3.5 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 3.5 - 3.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
