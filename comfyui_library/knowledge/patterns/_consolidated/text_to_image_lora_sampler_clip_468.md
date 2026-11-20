---
name: text_to_image_lora_sampler_clip_468
type: Text To Image
frequency: 4
level: moderate
coverage: 0.93675
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageBatchMulti, KSampler, LoadImage, LoraLoaderModelOnly, RunningHub_ImageQwenI2L_Loader(Style), RunningHub_ImageQwenI2L_LoraGenerator, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/I2L-秒出风格lora_1999667952062431233.json, 图片生成/文生图/I2L风格训练_1999591597580972033.json, 图片生成/文生图/I2L风格训练_2045037199279792129.json, 图片生成/文生图/【超快速LoRA训练】Qwen Image i2L模型：只需6张相同风格图片，1分钟训练出对应风格LoRA！_2001117117581754370.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_468

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/I2L-秒出风格lora_1999667952062431233.json、图片生成/文生图/I2L风格训练_1999591597580972033.json、图片生成/文生图/I2L风格训练_2045037199279792129.json、图片生成/文生图/【超快速LoRA训练】Qwen Image i2L模型：只需6张相同风格图片，1分钟训练出对应风格LoRA！_2001117117581754370.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageBatchMulti`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RunningHub_ImageQwenI2L_Loader(Style)`
- `RunningHub_ImageQwenI2L_LoraGenerator`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `ImageScaleToMegapixels` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ApplySageAttention` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `RunningHub Deepcleaner` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 512 - 1024 | 4 | 75% |
| 高度 | 1280 | 512 - 1536 | 4 | 67% |
| 采样步数 | 20 | 8 - 20 | 4 | 69% |
| Prompt 约束强度(CFG) | 4 | 1 - 8 | 4 | 41% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 512 - 1024，4 个样本
- 高度 中位数 1280，观测区间 512 - 1536，4 个样本
- 采样步数 中位数 20，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 8，4 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
