---
name: image_to_image_sampler_unet_vae_27
type: Image To Image
frequency: 9
level: moderate
coverage: 0.896333
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【遇见AI】longcat image edit turbo 图片编辑_2059223215184105473.json, 图片生成/图生图/一键场景多角度_1988773655125561346.json, 图片生成/图生图/一键多角度一致性_1986711907254087682.json, 图片生成/图生图/一键搞笑漫画风格_1987493162623111169.json, 图片生成/图生图/产品增加光影_2022309920766431234.json, 图片生成/图生图/人物变胖工作流_1997692792333864962.json, 图片生成/图生图/修复光斑--修复曝光LORA---Qwen-Edit-2509_1987219668211576834.json, 图片生成/图生图/千问  镜头移动_1993500582268829697.json, 图片生成/图生图/千问Qwen-多图融合1.0_2012857063315087361.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_27

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/【遇见AI】longcat image edit turbo 图片编辑_2059223215184105473.json、图片生成/图生图/一键场景多角度_1988773655125561346.json、图片生成/图生图/一键多角度一致性_1986711907254087682.json、图片生成/图生图/一键搞笑漫画风格_1987493162623111169.json、图片生成/图生图/产品增加光影_2022309920766431234.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `ModelSamplingAuraFlow` —— 8/9 个有
- `TextEncodeQwenImageEditPlus` —— 8/9 个有
- `Image Comparer (rgthree)` —— 5/9 个有
- `easy imageSize` —— 5/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `CR Prompt Text` —— 1/9 个有
- `FluxGuidance` —— 1/9 个有
- `FluxKontextImageScale` —— 1/9 个有
- `JDCN_StringToList` —— 1/9 个有
- `RepeatLatentBatch` —— 1/9 个有
- `TextEncodeQwenImageEdit` —— 1/9 个有
- `easy seed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 25 | 9 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 25，9 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（12/9 个样本）：Steps较低可能导致细节不足
