---
name: text_to_image_sampler_clip_unet_175
type: Text To Image
frequency: 3
level: strong
coverage: 0.837333
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LayerUtility: TextJoin, ModelSamplingAuraFlow, PreviewAny, PrimitiveInt, SaveImage, Text, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Anima3.8b vs 2.9b vs base生图_2113071120273461249.json, 图片生成/文生图/Anima+2.9b+vs+Anima base+生图_2089681885474680834.json, 图片生成/文生图/anima-preview3_2042590608996442114.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_175

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Anima3.8b vs 2.9b vs base生图_2113071120273461249.json、图片生成/文生图/Anima+2.9b+vs+Anima base+生图_2089681885474680834.json、图片生成/文生图/anima-preview3_2042590608996442114.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: TextJoin`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `PrimitiveInt`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `Anima38BV2Loader` —— 1/3 个有
- `Anima38BV2Prompt` —— 1/3 个有
- `AnimaQwen35Loader` —— 1/3 个有
- `Int` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 920 | 896 - 1024 | 3 | 94% |
| 高度 | 1536 | 1152 - 1536 | 3 | 87% |
| 采样步数 | 30 | 20 - 40 | 3 | 73% |
| Prompt 约束强度(CFG) | 5 | 4 - 5 | 3 | 90% |
| 采样算法 | res_multistep | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 920，观测区间 896 - 1024，3 个样本，取值集中（一致性 94%）
- 高度 中位数 1536，观测区间 1152 - 1536，3 个样本，取值集中（一致性 87%）
- 采样步数 中位数 30，观测区间 20 - 40，3 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 4 - 5，3 个样本，取值集中（一致性 90%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
