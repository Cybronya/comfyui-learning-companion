---
name: text_to_image_sampler_clip_unet_195
type: Text To Image
frequency: 3
level: moderate
coverage: 0.867667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-Image 美女自动扩写文生图_1996110278268010498.json, 图片生成/文生图/Z-Image-SuperV3-文生图_2018341790440493058.json, 图片生成/文生图/Z-Image-lora_1994678393864134657.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_195

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-Image 美女自动扩写文生图_1996110278268010498.json、图片生成/文生图/Z-Image-SuperV3-文生图_2018341790440493058.json、图片生成/文生图/Z-Image-lora_1994678393864134657.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `LoadImage` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 15 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 512 - 1080 | 3 | 70% |
| 高度 | 1920 | 512 - 1920 | 3 | 54% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 15，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 1080，3 个样本
- 高度 中位数 1920，观测区间 512 - 1920，3 个样本
