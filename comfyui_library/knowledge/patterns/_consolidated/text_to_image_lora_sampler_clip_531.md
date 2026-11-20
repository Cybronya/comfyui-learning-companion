---
name: text_to_image_lora_sampler_clip_531
type: Text To Image
frequency: 3
level: strong
coverage: 0.786667
common_nodes: [AddLabel, CLIPTextEncode, CR Image Grid Panel, CR Split String, CR Text, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, Empty_Line, FluxGuidance, ImpactInt, KSampler, LoRA Stack to String converter, LoraLoaderModelOnly, PreviewImage, SaveImage, StringReplace, UNETLoader, VAEDecode, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy loraStack, easy promptLine, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/FOR循环嵌套XY图表测试_pd_1943652132056657922.json, 图片生成/文生图/FOR循环嵌套XY图表测试_pd_2114315023588880385.json, 平台全量/easyuse for循环xyz_pd_1930579631173455874.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_531

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FOR循环嵌套XY图表测试_pd_1943652132056657922.json、图片生成/文生图/FOR循环嵌套XY图表测试_pd_2114315023588880385.json、平台全量/easyuse for循环xyz_pd_1930579631173455874.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `CLIPTextEncode`
- `CR Image Grid Panel`
- `CR Split String`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Empty_Line`
- `FluxGuidance`
- `ImpactInt`
- `KSampler`
- `LoRA Stack to String converter`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy loraStack`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `Float` —— 1/3 个有
- `Int` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `easy mathInt` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 768 | 768 - 768 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
