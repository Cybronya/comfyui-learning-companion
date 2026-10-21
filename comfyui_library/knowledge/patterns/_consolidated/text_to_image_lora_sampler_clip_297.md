---
name: text_to_image_lora_sampler_clip_297
type: Text To Image
frequency: 3
level: moderate
coverage: 0.943333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageBatchMulti, KSampler, LoadImage, LoraLoaderModelOnly, RunningHub_ImageQwenI2L_Loader(Style), RunningHub_ImageQwenI2L_LoraGenerator, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/I2L-秒出风格lora_1999667952062431233.json, 图片生成/文生图/I2L风格训练_1999591597580972033.json, 图片生成/文生图/RH_ImageQwenI2L图生Lora_1999263590009929729.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_297

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/I2L-秒出风格lora_1999667952062431233.json、图片生成/文生图/I2L风格训练_1999591597580972033.json、图片生成/文生图/RH_ImageQwenI2L图生Lora_1999263590009929729.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
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
- `ImageConcanate` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `ImageScaleToMegapixels` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `ApplySageAttention` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RunningHub Deepcleaner` —— 1/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 720 - 1024 | 3 | 84% |
| 高度 | 1280 | 1280 - 1536 | 3 | 91% |
| 采样步数 | 20 | 8 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 4 | 1 - 8 | 3 | 34% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 720 - 1024，3 个样本，取值集中（一致性 84%）
- 高度 中位数 1280，观测区间 1280 - 1536，3 个样本，取值集中（一致性 91%）
- 采样步数 中位数 20，观测区间 8 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 8，3 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
