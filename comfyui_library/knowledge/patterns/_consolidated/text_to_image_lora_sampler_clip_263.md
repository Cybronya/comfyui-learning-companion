---
name: text_to_image_lora_sampler_clip_263
type: Text To Image
frequency: 4
level: strong
coverage: 0.665
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, CR Text Concatenate, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, ImpactSwitch, Int, KSampler, LoadImage, LoraLoaderModelOnly, PreviewAny, SaveImage, SetNode, Switch any [Crystools], TTResolutionSelector, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy convertAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-文生图-可切换参考风格_2071220949994786817.json, 图片生成/文生图/Krea2-文生图-可切换参考风格_2072500761992458242.json, 图片生成/文生图/Krea2-文生图-可切换参考风格_2072857163869020162.json, 图片生成/文生图/Krea2-文生图-智能扩写+风格参考_2072514453173792770.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_263

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2-文生图-可切换参考风格_2071220949994786817.json、图片生成/文生图/Krea2-文生图-可切换参考风格_2072500761992458242.json、图片生成/文生图/Krea2-文生图-可切换参考风格_2072857163869020162.json、图片生成/文生图/Krea2-文生图-智能扩写+风格参考_2072514453173792770.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `SaveImage`
- `SetNode`
- `Switch any [Crystools]`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy convertAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `ZML_BooleanSwitch` —— 3/4 个有
- `easy boolean` —— 1/4 个有
- `忽略多组孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
