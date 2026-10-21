---
name: text_to_image_sampler_clip_vae_5
type: Text To Image
frequency: 14
level: strong
coverage: 0.965429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Turbo 基础 11.27_1997561858070614017.json, 图片生成/文生图/Z-Image-Turbo文生图_1993942538386161666.json, 图片生成/文生图/Z-Image_1996570015086297090.json, 图片生成/文生图/Z-Image文生图_2094304743563812866.json, 图片生成/文生图/Z-Image文生图基础工作流_2004808008284733442.json, 图片生成/文生图/Z-image 全能模型_1994451694316625922.json, 图片生成/文生图/Z-image+lora人像更换_2007628288839127041.json, 图片生成/文生图/Z-image-turbo极速文生图（内置身材调节Lora）_2101265914195955713.json, 图片生成/文生图/Z-image基础文生图工作流（含放大）_2001871745982296066.json, 图片生成/文生图/Z-image超写实文生图工作流_2099335310260916225.json, 图片生成/文生图/Z-image，新王登基，Flux2退散_1993500745689481218.json, 图片生成/文生图/z-image文生图工作流（不油腻超写实）_2099020153999675394.json, 图片生成/文生图/z-image文生图工作流（不油腻超写实）_2099402532144635906.json, 图片生成/文生图/摄影-文生图-Z-image-turbo_2096447342345015297.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_5

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Z-Image-Turbo 基础 11.27_1997561858070614017.json、图片生成/文生图/Z-Image-Turbo文生图_1993942538386161666.json、图片生成/文生图/Z-Image_1996570015086297090.json、图片生成/文生图/Z-Image文生图_2094304743563812866.json、图片生成/文生图/Z-Image文生图基础工作流_2004808008284733442.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 13/14 个有
- `ConditioningZeroOut` —— 11/14 个有
- `ImageUpscaleWithModel` —— 10/14 个有
- `UpscaleModelLoader` —— 10/14 个有
- `LoraLoaderModelOnly` —— 5/14 个有
- `ImageFromBatch` —— 4/14 个有
- `ImageSharpen` —— 4/14 个有
- `PreviewImage` —— 4/14 个有
- `LayerColor: BrightnessContrastV2` —— 2/14 个有
- `Int` —— 1/14 个有
- `LayerColor: Brightness & Contrast` —— 1/14 个有
- `LoraLoader` —— 1/14 个有
- `UnetLoaderGGUF` —— 1/14 个有
- `ZML_LoadImage` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 720 - 1440 | 14 | 80% |
| 高度 | 1824 | 720 - 1920 | 14 | 73% |
| 采样步数 | 10 | 8 - 10 | 14 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 79% |
| 调度器 | simple | - | 14 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| LoRA 模型强度 | 0.5 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 720 - 1440，14 个样本，取值集中（一致性 80%）
- 高度 中位数 1824，观测区间 720 - 1920，14 个样本
- 采样步数 中位数 10，观测区间 8 - 10，14 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 79%
- 调度器 最常用 simple，14 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
