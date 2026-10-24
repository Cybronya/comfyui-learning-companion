---
name: text_to_image_lora_sampler_clip_230
type: Text To Image
frequency: 8
level: moderate
coverage: 0.90875
common_nodes: [AILab_QwenVL, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, Krea2ControlApply, Krea2ControlImageEncode, Krea2ControlLoRALoader, LayerUtility: ImageScaleByAspectRatio, LoadImage, ModelSamplingAuraFlow, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/krea2-cn控制图生图_2090805286805266433.json, 图片生成/图生图/krea2深度控制图生图_2075408443883745282.json, 图片生成/图生图/krea2深度控制图生图_2075410063556177922.json, 图片生成/图生图/krea2深度控制图生图_2083459570168582145.json, 图片生成/图生图/krea2深度控制图生图洗图_2075405320553324546.json, 图片生成/图生图/krea2深度控制洗图_2075409406933688322.json, 图片生成/文生图/Krea2 CN控制图生图工作流，文生图图生图控制处理工具_2107990625491709953.json, 图片生成/文生图/krea2-cn控制图生图_2105949894426058753.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_230

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/krea2-cn控制图生图_2090805286805266433.json、图片生成/图生图/krea2深度控制图生图_2075408443883745282.json、图片生成/图生图/krea2深度控制图生图_2075410063556177922.json、图片生成/图生图/krea2深度控制图生图_2083459570168582145.json、图片生成/图生图/krea2深度控制图生图洗图_2075405320553324546.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `Krea2ControlApply`
- `Krea2ControlImageEncode`
- `Krea2ControlLoRALoader`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingV2Preprocessor` —— 5/8 个有
- `AIO_Preprocessor` —— 3/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `VAEEncode` —— 2/8 个有
- `JjkText` —— 1/8 个有
- `solarL_SaveImagesToZip` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 8 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 8 | 19% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 80 - 1536 | 8 | 61% |
| 高度 | 1024 | 80 - 1024 | 8 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，8 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1536，8 个样本
- 高度 中位数 1024，观测区间 80 - 1024，8 个样本
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
