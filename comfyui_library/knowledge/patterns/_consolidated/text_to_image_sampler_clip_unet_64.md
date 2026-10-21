---
name: text_to_image_sampler_clip_unet_64
type: Text To Image
frequency: 7
level: moderate
coverage: 0.825143
common_nodes: [CLIPTextEncode, DeepTranslatorTextNode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/01动漫人物+场景FLUX文生图_1947078298218455041.json, 图片生成/文生图/1938437078218641410.json, 图片生成/文生图/1942946111835291650.json, 图片生成/文生图/1943306363688939521.json, 图片生成/文生图/1946442950954115073.json, 图片生成/文生图/1959457037811920898.json, 图片生成/文生图/动漫人物+场景制作_2000568730323218434.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_64

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/01动漫人物+场景FLUX文生图_1947078298218455041.json、图片生成/文生图/1938437078218641410.json、图片生成/文生图/1942946111835291650.json、图片生成/文生图/1943306363688939521.json、图片生成/文生图/1946442950954115073.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewTextNode` —— 4/7 个有
- `Any Switch (rgthree)` —— 3/7 个有
- `ConcatTextOfUtils` —— 3/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `JjkText` —— 3/7 个有
- `PreviewImage` —— 2/7 个有
- `ReferenceLatent` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 512 - 1280 | 7 | 66% |
| 高度 | 720 | 512 - 1920 | 7 | 48% |
| 采样步数 | 20 | 20 - 30 | 7 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 512 - 1280，7 个样本
- 高度 中位数 720，观测区间 512 - 1920，7 个样本，取值分散，一致性仅 48%
- 采样步数 中位数 20，观测区间 20 - 30，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
