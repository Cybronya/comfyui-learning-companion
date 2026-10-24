---
name: text_to_image_sampler_clip_unet_121
type: Text To Image
frequency: 6
level: moderate
coverage: 0.9665
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【遇见AI】Juggernaut-Z-Image模型和Zturbo  Zbase对比_2054033528748298242.json, 图片生成/文生图/【阡陌】通义千问Qwen-image文生图工作流_1953718095699431426.json, 图片生成/文生图/动漫专用模型文生图_2019252456521211906.json, 图片生成/文生图/千问文生图工作流_1992469322945851393.json, 图片生成/文生图/千问文生图工作流_2003750459162673154.json, 图片生成/文生图/官流Qwen-lmage-FP8中文版_1953112797149392898.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_121

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/【遇见AI】Juggernaut-Z-Image模型和Zturbo  Zbase对比_2054033528748298242.json、图片生成/文生图/【阡陌】通义千问Qwen-image文生图工作流_1953718095699431426.json、图片生成/文生图/动漫专用模型文生图_2019252456521211906.json、图片生成/文生图/千问文生图工作流_1992469322945851393.json、图片生成/文生图/千问文生图工作流_2003750459162673154.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/6 个有
- `ModelSamplingAuraFlow` —— 2/6 个有
- `CR Seed` —— 1/6 个有
- `EasyCache` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `Textbox` —— 1/6 个有
- `easy promptLine` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 26 | 8 - 35 | 6 | 60% |
| Prompt 约束强度(CFG) | 4 | 1 - 8 | 6 | 46% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 800 | 720 - 1280 | 6 | 78% |
| 高度 | 1120 | 1024 - 1368 | 6 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 26，观测区间 8 - 35，6 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 8，6 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 800，观测区间 720 - 1280，6 个样本
- 高度 中位数 1120，观测区间 1024 - 1368，6 个样本，取值集中（一致性 88%）
