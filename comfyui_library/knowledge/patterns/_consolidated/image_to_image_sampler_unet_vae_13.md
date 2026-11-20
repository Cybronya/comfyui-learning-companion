---
name: image_to_image_sampler_unet_vae_13
type: Image To Image
frequency: 10
level: moderate
coverage: 0.8974
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【遇见AI】longcat image edit turbo 图片编辑_2059223215184105473.json, 图片生成/图生图/一键场景多角度_1988773655125561346.json, 图片生成/图生图/一键多角度一致性_1986711907254087682.json, 图片生成/图生图/一键搞笑漫画风格_1987493162623111169.json, 图片生成/图生图/人物变胖工作流_1997692792333864962.json, 图片生成/图生图/人物服装提取_2000685930392547330.json, 图片生成/图生图/修复光斑--修复曝光LORA---Qwen-Edit-2509_1987219668211576834.json, 图片生成/图生图/千问  镜头移动_1993500582268829697.json, 图片生成/图生图/千问Qwen-多图融合1.0_2012857063315087361.json, 图片生成/图生图/去除光斑_过曝_欠曝修复_1995155032003764226.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_13

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/【遇见AI】longcat image edit turbo 图片编辑_2059223215184105473.json、图片生成/图生图/一键场景多角度_1988773655125561346.json、图片生成/图生图/一键多角度一致性_1986711907254087682.json、图片生成/图生图/一键搞笑漫画风格_1987493162623111169.json、图片生成/图生图/人物变胖工作流_1997692792333864962.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
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
- `CFGNorm` —— 9/10 个有
- `LoraLoaderModelOnly` —— 9/10 个有
- `ModelSamplingAuraFlow` —— 9/10 个有
- `TextEncodeQwenImageEditPlus` —— 8/10 个有
- `Image Comparer (rgthree)` —— 6/10 个有
- `easy imageSize` —— 5/10 个有
- `PrimitiveStringMultiline` —— 2/10 个有
- `TextEncodeQwenImageEdit` —— 2/10 个有
- `Anything Everywhere3` —— 1/10 个有
- `FluxGuidance` —— 1/10 个有
- `FluxKontextImageScale` —— 1/10 个有
- `JDCN_StringToList` —— 1/10 个有
- `RepeatLatentBatch` —— 1/10 个有
- `easy seed` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 10 | 42% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，10 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（13/10 个样本）：Steps较低可能导致细节不足
