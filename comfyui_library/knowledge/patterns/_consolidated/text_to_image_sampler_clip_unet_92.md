---
name: text_to_image_sampler_clip_unet_92
type: Text To Image
frequency: 8
level: weak
coverage: 0.990375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/泠月luna Krea2 turbo 单采_2084111094850867201.json, 图片生成/文生图/溶图lora基础版_2043624892586795010.json, 图片生成/文生图/电锯人漫画画风_2100390025178472449.json, 图片生成/文生图/真实人像Kook_Flux_klein工作流_2019756687074267138.json, 图片生成/文生图/维琳娜·艾嘉德ANIMA专属工作流(图图lora)_2068391183554007042.json, 图片生成/文生图/谢帅文生图工作流_2108466900505292802.json, 图片生成/文生图/超写实人像生成 Magic-Wan-Image V2_1990394619835944962.json, 图片生成/文生图/（文生图 电商海报挺好 文字清晰）MOSS image 最强开源文生图｜开源生图的黑马_2112088005384167425.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_92

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/泠月luna Krea2 turbo 单采_2084111094850867201.json、图片生成/文生图/溶图lora基础版_2043624892586795010.json、图片生成/文生图/电锯人漫画画风_2100390025178472449.json、图片生成/文生图/真实人像Kook_Flux_klein工作流_2019756687074267138.json、图片生成/文生图/维琳娜·艾嘉德ANIMA专属工作流(图图lora)_2068391183554007042.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `MuyeTextEditOutput` —— 2/8 个有
- `CR Text Concatenate` —— 1/8 个有
- `ModelSamplingSD3` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `ResolutionStdSelector` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `SkipLayerGuidanceDiTSimple` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 45 | 8 | 31% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 8 | 8 | 16% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 512 - 1200 | 8 | 78% |
| 高度 | 1496 | 512 - 1920 | 8 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 45，8 个样本，取值分散，一致性仅 31%
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 8，8 个样本，取值分散，一致性仅 16%
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1200，8 个样本
- 高度 中位数 1496，观测区间 512 - 1920，8 个样本
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
