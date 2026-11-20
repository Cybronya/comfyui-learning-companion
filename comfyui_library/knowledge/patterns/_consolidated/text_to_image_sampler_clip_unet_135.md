---
name: text_to_image_sampler_clip_unet_135
type: Text To Image
frequency: 6
level: strong
coverage: 0.971
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图V2_2006090856985530370.json, 图片生成/文生图/文生图_2002461454764765185.json, 图片生成/文生图/文生图_2083074458058846209.json, 图片生成/文生图/流体金属家居产品设计_2022553115676909569.json, 图片生成/文生图/节点系列10-PromptList节点_2012025090799575042.json, 图片生成/文生图/高层住宅立面泛化_2015087544735637505.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_135

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/文生图V2_2006090856985530370.json、图片生成/文生图/文生图_2002461454764765185.json、图片生成/文生图/文生图_2083074458058846209.json、图片生成/文生图/流体金属家居产品设计_2022553115676909569.json、图片生成/文生图/节点系列10-PromptList节点_2012025090799575042.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `easy promptList` —— 3/6 个有
- `ConcatTextOfUtils` —— 2/6 个有
- `ModelSamplingAuraFlow` —— 2/6 个有
- `Text` —— 2/6 个有
- `ttN concat` —— 2/6 个有
- `Lora Loader Stack (rgthree)` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `Text List to Text` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 9 | 6 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1004 | 720 - 1280 | 6 | 77% |
| 高度 | 1280 | 1280 - 1560 | 6 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 9，6 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1004，观测区间 720 - 1280，6 个样本
- 高度 中位数 1280，观测区间 1280 - 1560，6 个样本，取值集中（一致性 91%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
