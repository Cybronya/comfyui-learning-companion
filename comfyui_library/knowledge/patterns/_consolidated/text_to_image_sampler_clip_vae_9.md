---
name: text_to_image_sampler_clip_vae_9
type: Text To Image
frequency: 14
level: weak
coverage: 0.911
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku-Z-Image-全自动文生图_2005186111444054017.json, 图片生成/文生图/Nunchaku-Z-Image-美女图像生成_2005261946289090561.json, 图片生成/文生图/Ovis-Image-海报生成_1998366450572255234.json, 图片生成/文生图/Qwen-Image-2512-全自动文生图_2006362427654414338.json, 图片生成/文生图/Qwen-Image-2512-美女图像生成_2006598917072363521.json, 图片生成/文生图/Z-Image-Base-全自动美女生成_2016483416421703682.json, 图片生成/文生图/Z-Image-Turbo-_1994588125756264449.json, 图片生成/文生图/Z-Image-Turbo-全自动文生图_1993944444179251201.json, 图片生成/文生图/Z-Image-Turbo-网红美女图像生成_1994562866558668801.json, 图片生成/文生图/Z-Image-按要求美女图像生成_1998383341026050050.json, 图片生成/文生图/Z-Image-美女造相_2001491783865466882.json, 图片生成/文生图/Z-image-Art-自动文生图_2018672608220291073.json, 图片生成/文生图/Z-image-base-极速自动文生图（4步出图）_2021738815794188290.json, 图片生成/文生图/极致美学文生图（姿态向）v1.5_1985265291271749633.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_9

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Nunchaku-Z-Image-全自动文生图_2005186111444054017.json、图片生成/文生图/Nunchaku-Z-Image-美女图像生成_2005261946289090561.json、图片生成/文生图/Ovis-Image-海报生成_1998366450572255234.json、图片生成/文生图/Qwen-Image-2512-全自动文生图_2006362427654414338.json、图片生成/文生图/Qwen-Image-2512-美女图像生成_2006598917072363521.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 14 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JDCN_StringToList` —— 13/14 个有
- `UNETLoader` —— 12/14 个有
- `easy showAnything` —— 11/14 个有
- `LoraLoaderModelOnly` —— 7/14 个有
- `CR Text Replace` —— 6/14 个有
- `MuyeTextEditOutput` —— 5/14 个有
- `ModelSamplingAuraFlow` —— 4/14 个有
- `ShowText|pysssss` —— 4/14 个有
- `NunchakuZImageDiTLoader` —— 2/14 个有
- `CR Text` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `ProcessString` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 50 | 14 | 4% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 14 | 23% |
| 采样算法 | euler | - | 14 | 71% |
| 调度器 | simple | - | 14 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 720 | 656 - 1536 | 14 | 73% |
| 高度 | 1280 | 1104 - 1648 | 14 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 50，14 个样本，取值分散，一致性仅 4%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，14 个样本，取值分散，一致性仅 23%
- 采样算法 最常用 euler，14 个样本，一致性 71%
- 调度器 最常用 simple，14 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 656 - 1536，14 个样本
- 高度 中位数 1280，观测区间 1104 - 1648，14 个样本，取值集中（一致性 91%）
- 高发问题（11/14 个样本）：Steps较低可能导致细节不足
