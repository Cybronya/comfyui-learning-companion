---
name: image_to_image_sampler_clip_checkpoint_2
type: Image To Image
frequency: 14
level: moderate
coverage: 0.921214
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/【AI小王子】18.图生图反推关键词_2046839296702812161.json, 图片生成/图生图/【遇见AI】SD1.5基础图生图工作流_2011358352109998082.json, 图片生成/图生图/一键生成3D动漫_1910479127286349825.json, 图片生成/图生图/一键生成二次元动漫_1910461036196233217.json, 图片生成/图生图/一键生成吉卜力风格二次元动漫_1910616593620238337.json, 图片生成/图生图/动漫人物真人化V1_1955916030663118850.json, 图片生成/图生图/卡通图生图_1969999349163958274.json, 图片生成/图生图/图生图-SDXL-完美生成3D形象-+_1912322252413595649.json, 图片生成/图生图/图生图_1946045231777148930.json, 图片生成/图生图/图生图_1946895861551128577.json, 图片生成/图生图/图生图_2017126492739735553.json, 图片生成/图生图/图生图工作流_2075388564568891394.json, 图片生成/图生图/图生图（动漫转真人）_1906953442139545601.json, 图片生成/文生图/SDXL线稿预处理工作流（一键转绘）_2078726858711064578.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/【AI小王子】18.图生图反推关键词_2046839296702812161.json、图片生成/图生图/【遇见AI】SD1.5基础图生图工作流_2011358352109998082.json、图片生成/图生图/一键生成3D动漫_1910479127286349825.json、图片生成/图生图/一键生成二次元动漫_1910461036196233217.json、图片生成/图生图/一键生成吉卜力风格二次元动漫_1910616593620238337.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `AutoNegativePrompt` —— 2/14 个有
- `ControlNetApplyAdvanced` —— 2/14 个有
- `ControlNetLoader` —— 2/14 个有
- `LineArtPreprocessor` —— 2/14 个有
- `PreviewImage` —— 2/14 个有
- `ShowText|pysssss` —— 2/14 个有
- `WD14Tagger|pysssss` —— 2/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `RepeatLatentBatch` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 35 | 14 | 80% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 14 | 91% |
| 采样算法 | euler | - | 14 | 64% |
| 调度器 | normal | - | 14 | 71% |
| 重绘幅度 | 0.495 | 0.2 - 1 | 14 | 62% |
| ControlNet 权重 | 0.65 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 35，14 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，14 个样本，取值集中（一致性 91%）
- 采样算法 最常用 euler，14 个样本，一致性 64%
- 调度器 最常用 normal，14 个样本，一致性 71%
- 重绘幅度 中位数 0.495，观测区间 0.2 - 1，14 个样本
- ControlNet 权重 中位数 0.65，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
