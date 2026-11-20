---
name: image_to_image_sampler_vae_13
type: Image To Image
frequency: 11
level: moderate
coverage: 0.865455
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_Nunchaku_任意姿势参考迁移_1995464356798377986.json, 图片生成/图生图/nunchaku Qwen Edit 8步出图_1965791914949808129.json, 图片生成/图生图/qwen edit 双人合影_1972189838340517889.json, 图片生成/图生图/qwen 双人合影_1970745203600596993.json, 图片生成/图生图/qwen 双人拍立得合影_1972850394676285442.json, 图片生成/图生图/一致性去水印_1992437141525385218.json, 图片生成/图生图/三视图一键生成多视角三视图_人物一致性人物转（加速版）_1967533621051580418.json, 图片生成/图生图/人物动作迁移 保持一致性 Qwen-edit多图编辑_1973243474298449922.json, 图片生成/图生图/人物动作迁移_2004095655121436673.json, 平台全量/qwen千问最新编辑模型plus版本_多图编辑千问_1970425976415002625.json, 平台全量/人物转三视图  一键生成多视角三视图 人物一致性 加速版_2025394121183076353.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_13

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen_Nunchaku_任意姿势参考迁移_1995464356798377986.json、图片生成/图生图/nunchaku Qwen Edit 8步出图_1965791914949808129.json、图片生成/图生图/qwen edit 双人合影_1972189838340517889.json、图片生成/图生图/qwen 双人合影_1970745203600596993.json、图片生成/图生图/qwen 双人拍立得合影_1972850394676285442.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `easy imageConcat` —— 9/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `NunchakuQwenImageDiTLoader` —— 8/11 个有
- `TextEncodeQwenImageEditPlus` —— 8/11 个有
- `ReferenceLatent` —— 7/11 个有
- `UNETLoader` —— 7/11 个有
- `ConditioningAverage` —— 6/11 个有
- `SDXLEmptyLatentSizePicker+` —— 6/11 个有
- `PreviewImage` —— 5/11 个有
- `DWPreprocessor` —— 3/11 个有
- `TextEncodeQwenImageEdit` —— 3/11 个有
- `CR Simple Image Compare` —— 2/11 个有
- `EmptyLatentImage` —— 2/11 个有
- `easy imageSize` —— 2/11 个有
- `Text Multiline` —— 1/11 个有
- `easy promptConcat` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 11 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 704x1408 (0.5) | - | 6 | 67% |
| 高度 | 1 | 1 - 1328 | 6 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 最常用 704x1408 (0.5)，6 个样本，一致性 67%
- 高度 中位数 1，观测区间 1 - 1328，6 个样本，取值分散，一致性仅 0%
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
