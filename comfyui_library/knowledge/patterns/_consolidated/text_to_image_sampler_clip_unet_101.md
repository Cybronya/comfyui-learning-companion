---
name: text_to_image_sampler_clip_unet_101
type: Text To Image
frequency: 7
level: moderate
coverage: 0.847286
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, ModelPatchLoader, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-turbo 深度控制_2030690837834768385.json, 图片生成/图生图/【遇见AI】z-image fun controlnet+inpaint_2053783735144857602.json, 图片生成/图生图/【遇见AI】z-image fun controlnet_2053781769182294018.json, 图片生成/图生图/【遇见AI】z-image turbo fun controlnet+inpaint_2053778216468398081.json, 图片生成/图生图/【遇见AI】z-image turbo fun controlnet_2053776858411479041.json, 图片生成/图生图/图生图-CN选择-提示词反推_2069077875545952258.json, 图片生成/文生图/图生图-CN选择-提示词反推_2064280927131488258.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_101

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Z-turbo 深度控制_2030690837834768385.json、图片生成/图生图/【遇见AI】z-image fun controlnet+inpaint_2053783735144857602.json、图片生成/图生图/【遇见AI】z-image fun controlnet_2053781769182294018.json、图片生成/图生图/【遇见AI】z-image turbo fun controlnet+inpaint_2053778216468398081.json、图片生成/图生图/【遇见AI】z-image turbo fun controlnet_2053776858411479041.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/7 个有
- `ZImageFunControlnet` —— 4/7 个有
- `GetImageSizeAndCount` —— 3/7 个有
- `ImageScaleToTotalPixels` —— 3/7 个有
- `QwenImageDiffsynthControlnet` —— 3/7 个有
- `RH_Captioner` —— 3/7 个有
- `ImpactSwitch` —— 2/7 个有
- `Int` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `Manual XY Entry Info` —— 2/7 个有
- `MuyeTextEditOutput` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `easy ifElse` —— 2/7 个有
- `easy isNone` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 7 | 70% |
| 高度 | 768 | 512 - 1536 | 7 | 61% |
| 采样步数 | 10 | 8 - 28 | 7 | 41% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 7 | 27% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，7 个样本
- 高度 中位数 768，观测区间 512 - 1536，7 个样本
- 采样步数 中位数 10，观测区间 8 - 28，7 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，7 个样本，取值分散，一致性仅 27%
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
