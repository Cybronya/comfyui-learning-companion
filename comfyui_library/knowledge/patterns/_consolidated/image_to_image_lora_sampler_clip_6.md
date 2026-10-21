---
name: image_to_image_lora_sampler_clip_6
type: Image To Image
frequency: 4
level: moderate
coverage: 0.93875
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [seed _O]
members: [图片生成/文生图/1965677148407255041.json, 图片生成/文生图/草扎草编工艺_灯具设计_斗笠型_2098035544990244865.json, 图片生成/文生图/草扎草编工艺_灯具设计_灯笼型_2098035451851530241.json, 图片生成/文生图/草扎草编工艺_灯具设计_鱼篓型_2098023963254419458.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1965677148407255041.json、图片生成/文生图/草扎草编工艺_灯具设计_斗笠型_2098035544990244865.json、图片生成/文生图/草扎草编工艺_灯具设计_灯笼型_2098035451851530241.json、图片生成/文生图/草扎草编工艺_灯具设计_鱼篓型_2098023963254419458.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CannyEdgePreprocessor` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `LoadKontextPresets` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `seed _O` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 24 | 4 | 67% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 4 | 60% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 0.95 | 0.95 - 1 | 4 | 98% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 24，4 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 0.95，观测区间 0.95 - 1，4 个样本，取值集中（一致性 98%）
- 这些节点还没有知识卡，系统对它们的理解有限：seed _O
