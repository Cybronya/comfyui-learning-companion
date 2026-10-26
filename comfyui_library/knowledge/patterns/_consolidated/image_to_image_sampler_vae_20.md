---
name: image_to_image_sampler_vae_20
type: Image To Image
frequency: 7
level: weak
coverage: 0.877143
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Nunchaku_任意姿势参考迁移_1995464356798377986.json, 图片生成/图生图/nunchaku Qwen Edit 8步出图_1965791914949808129.json, 图片生成/图生图/qwen edit 双人合影_1972189838340517889.json, 图片生成/图生图/qwen 双人合影_1970745203600596993.json, 图片生成/图生图/qwen 双人拍立得合影_1972850394676285442.json, 图片生成/图生图/【阡陌】Qwen-Image-Edit-2509升级Plus版人物姿态控制_1971193309135851522.json, 图片生成/图生图/三视图一键生成多视角三视图_人物一致性人物转（加速版）_1967533621051580418.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_20

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen_Nunchaku_任意姿势参考迁移_1995464356798377986.json、图片生成/图生图/nunchaku Qwen Edit 8步出图_1965791914949808129.json、图片生成/图生图/qwen edit 双人合影_1972189838340517889.json、图片生成/图生图/qwen 双人合影_1970745203600596993.json、图片生成/图生图/qwen 双人拍立得合影_1972850394676285442.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `ReferenceLatent` —— 5/7 个有
- `TextEncodeQwenImageEditPlus` —— 5/7 个有
- `easy imageConcat` —— 5/7 个有
- `ConditioningAverage` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `SDXLEmptyLatentSizePicker+` —— 4/7 个有
- `UNETLoader` —— 4/7 个有
- `DWPreprocessor` —— 2/7 个有
- `EmptyLatentImage` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `TextEncodeQwenImageEdit` —— 2/7 个有
- `CR Simple Image Compare` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `easy imageSize` —— 1/7 个有
- `easy promptConcat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 7 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 57% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 704x1408 (0.5) | - | 5 | 60% |
| 高度 | 1 | 1 - 1328 | 5 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，7 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 最常用 704x1408 (0.5)，5 个样本，一致性 60%
- 高度 中位数 1，观测区间 1 - 1328，5 个样本，取值分散，一致性仅 0%
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
