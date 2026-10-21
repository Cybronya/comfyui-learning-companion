---
name: text_to_image_sampler_clip_vae_6
type: Text To Image
frequency: 12
level: moderate
coverage: 0.913417
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku-Z-Image-全自动文生图_2005186111444054017.json, 图片生成/文生图/Nunchaku-Z-Image-美女图像生成_2005261946289090561.json, 图片生成/文生图/Ovis-Image-海报生成_1998366450572255234.json, 图片生成/文生图/Qwen-Image-2512-全自动文生图_2006362427654414338.json, 图片生成/文生图/Qwen-Image-2512-美女图像生成_2006598917072363521.json, 图片生成/文生图/Z-Image-Base-全自动美女生成_2016483416421703682.json, 图片生成/文生图/Z-Image-Turbo-_1994588125756264449.json, 图片生成/文生图/Z-Image-Turbo-全自动文生图_1993944444179251201.json, 图片生成/文生图/Z-Image-Turbo-网红美女图像生成_1994562866558668801.json, 图片生成/文生图/Z-Image-按要求美女图像生成_1998383341026050050.json, 图片生成/文生图/Z-Image-美女造相_2001491783865466882.json, 图片生成/文生图/Z-image-Art-自动文生图_2018672608220291073.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_6

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Nunchaku-Z-Image-全自动文生图_2005186111444054017.json、图片生成/文生图/Nunchaku-Z-Image-美女图像生成_2005261946289090561.json、图片生成/文生图/Ovis-Image-海报生成_1998366450572255234.json、图片生成/文生图/Qwen-Image-2512-全自动文生图_2006362427654414338.json、图片生成/文生图/Qwen-Image-2512-美女图像生成_2006598917072363521.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 12 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JDCN_StringToList` —— 11/12 个有
- `easy showAnything` —— 11/12 个有
- `UNETLoader` —— 10/12 个有
- `CR Text Replace` —— 5/12 个有
- `LoraLoaderModelOnly` —— 5/12 个有
- `MuyeTextEditOutput` —— 5/12 个有
- `ModelSamplingAuraFlow` —— 2/12 个有
- `NunchakuZImageDiTLoader` —— 2/12 个有
- `ShowText|pysssss` —— 2/12 个有
- `PreviewImage` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 50 | 12 | 4% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 12 | 21% |
| 采样算法 | euler | - | 12 | 83% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 720 | 656 - 1024 | 12 | 88% |
| 高度 | 1280 | 1104 - 1648 | 12 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 50，12 个样本，取值分散，一致性仅 4%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，12 个样本，取值分散，一致性仅 21%
- 采样算法 最常用 euler，12 个样本，一致性 83%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 656 - 1024，12 个样本，取值集中（一致性 88%）
- 高度 中位数 1280，观测区间 1104 - 1648，12 个样本，取值集中（一致性 90%）
- 高发问题（9/12 个样本）：Steps较低可能导致细节不足
