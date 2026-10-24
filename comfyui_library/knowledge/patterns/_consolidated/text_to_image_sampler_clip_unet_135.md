---
name: text_to_image_sampler_clip_unet_135
type: Text To Image
frequency: 5
level: moderate
coverage: 0.9218
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen-image 文生图_1955085568910790658.json, 图片生成/文生图/qwen_image文生图支持中文_1948416477526392833.json, 图片生成/文生图/动漫柔和光（Anima）_2073031688103485441.json, 图片生成/文生图/千问3D布艺可爱画风_1969762845573476353.json, 图片生成/文生图/国庆头像-千问3D布艺可爱画风_1969885972878008322.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_135

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/qwen-image 文生图_1955085568910790658.json、图片生成/文生图/qwen_image文生图支持中文_1948416477526392833.json、图片生成/文生图/动漫柔和光（Anima）_2073031688103485441.json、图片生成/文生图/千问3D布艺可爱画风_1969762845573476353.json、图片生成/文生图/国庆头像-千问3D布艺可爱画风_1969885972878008322.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `ConcatText_Zho` —— 2/5 个有
- `Int` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `Switch any [Crystools]` —— 2/5 个有
- `CFGNorm` —— 1/5 个有
- `FluxResolutionNode` —— 1/5 个有
- `LoadImage` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 904 - 1600 | 5 | 78% |
| 高度 | 1368 | 904 - 1600 | 5 | 78% |
| 采样步数 | 25 | 4 - 30 | 5 | 58% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 4 | 5 | 66% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | normal | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 904 - 1600，5 个样本
- 高度 中位数 1368，观测区间 904 - 1600，5 个样本
- 采样步数 中位数 25，观测区间 4 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 4，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 normal，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
