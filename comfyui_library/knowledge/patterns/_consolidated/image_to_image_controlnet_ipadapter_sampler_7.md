---
name: image_to_image_controlnet_ipadapter_sampler_7
type: Image To Image
frequency: 4
level: strong
coverage: 0.83625
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, IPAdapterAdvanced, IPAdapterUnifiedLoader, ImageInvert, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/LINE ART图片转线稿_2043585712259338241.json, 图片生成/图生图/LineArt图片转线稿_在线生图_1899080497694425090.json, 平台全量/一键线稿上色_1910522041051639810.json, 平台全量/线稿上色_1890351686018584577.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_sampler_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/LINE ART图片转线稿_2043585712259338241.json、图片生成/图生图/LineArt图片转线稿_在线生图_1899080497694425090.json、平台全量/一键线稿上色_1910522041051639810.json、平台全量/线稿上色_1890351686018584577.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `ImageInvert`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 2/4 个有
- `ConstrainImage|pysssss` —— 2/4 个有
- `LatentUpscaleBy` —— 2/4 个有
- `LineArtPreprocessor` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `Label (rgthree)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.8 | 0.8 - 0.8 | 4 | 100% |
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.08 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.8，观测区间 0.8 - 0.8，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.08，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
