---
name: text_to_image_lora_sampler_clip_57
type: Text To Image
frequency: 16
level: moderate
coverage: 0.918813
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImageBatchMulti, KSampler, LoadImage, LoraLoaderModelOnly, RunningHub_ImageQwenI2L_Loader(Style), RunningHub_ImageQwenI2L_LoraGenerator, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen I2L风格化（手绘）_2000864734511591426.json, 图片生成/图生图/Qwen I2L风格迁移(素描)_2000754601685024769.json, 图片生成/图生图/Qwen I2L风格迁移V1（抽象矢量）_1999455955618234370.json, 图片生成/图生图/Qwen I2L风格迁移V1（潦草手绘）_1999446540601131010.json, 图片生成/图生图/Qwen I2L风格迁移V1（素描画）_1999456220161470466.json, 图片生成/图生图/Qwen I2L风格迁移V1（蓝底扁平）_1999459545154023425.json, 图片生成/图生图/Qwen I2L风格迁移模仿-两分钟风格lora炼制_2000809836424163330.json, 图片生成/图生图/Qwen i2L-风格迁移模仿-两分钟炼风格lora_2000851690133782529.json, 图片生成/图生图/Qwen i2L-风格迁移模仿-两分钟炼风格lora_2046393246267482114.json, 图片生成/图生图/Qwen+i2L-风格迁移模仿-lora_2016779197426962433.json, 图片生成/图生图/Qwen-Image-i2L(图生Lora)_1999351494661074945.json, 图片生成/图生图/Qwen-Image-i2L风格迁移融图_1999494754196914178.json, 图片生成/图生图/RH_ImageQwenI2L图生Lora体验_1999336956502962178.json, 图片生成/图生图/imageqwenI2l图生lora_1999628296188985346.json, 图片生成/图生图/【gen全能视频Si】 qwen-image i2l参考图出风格lora_1999771864371167233.json, 图片生成/文生图/RH_ImageQwenI2L图生Lora_1999263590009929729.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_57

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Qwen I2L风格化（手绘）_2000864734511591426.json、图片生成/图生图/Qwen I2L风格迁移(素描)_2000754601685024769.json、图片生成/图生图/Qwen I2L风格迁移V1（抽象矢量）_1999455955618234370.json、图片生成/图生图/Qwen I2L风格迁移V1（潦草手绘）_1999446540601131010.json、图片生成/图生图/Qwen I2L风格迁移V1（素描画）_1999456220161470466.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 16 个 workflow 都包含：
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 10/16 个有
- `ImageConcatMulti` —— 10/16 个有
- `PDIMAGE_LongerSize` —— 10/16 个有
- `PreviewImage` —— 4/16 个有
- `Text Multiline` —— 4/16 个有
- `ConditioningZeroOut` —— 1/16 个有
- `ImageResizeKJv2` —— 1/16 个有
- `PreviewAny` —— 1/16 个有
- `PrimitiveStringMultiline` —— 1/16 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 16 | 79% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 16 | 68% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 848 | 720 - 1280 | 16 | 76% |
| 高度 | 1280 | 768 - 1664 | 16 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，16 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，16 个样本
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 848，观测区间 720 - 1280，16 个样本
- 高度 中位数 1280，观测区间 768 - 1664，16 个样本
