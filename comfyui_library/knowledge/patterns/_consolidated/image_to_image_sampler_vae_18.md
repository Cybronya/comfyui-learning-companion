---
name: image_to_image_sampler_vae_18
type: Image To Image
frequency: 8
level: moderate
coverage: 0.925625
common_nodes: [ConditioningZeroOut, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX krea 人像洗图真实感_1951921534116024322.json, 图片生成/图生图/FLUX krea 反推提示词图生图工作流_1951922402819297282.json, 图片生成/图生图/FLUX图生图_1948702291495460865.json, 图片生成/图生图/【阡陌】FLUX krea 反推提示词图生图工作流_1951533161555636225.json, 图片生成/图生图/【阡陌】FLUX krea 图生图工作流_1951526547859648513.json, 图片生成/图生图/【阡陌】FLUX+LORA+Joy Caption 反推提示词图生图_1942197993288183810.json, 图片生成/图生图/【阡陌】Nunchaku8倍加速 flux joy反推图生图_1944745315662745601.json, 图片生成/图生图/反推洗图 美女图起号Joycaption 3（beta one）效果_1926990150398803970.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_18

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FLUX krea 人像洗图真实感_1951921534116024322.json、图片生成/图生图/FLUX krea 反推提示词图生图工作流_1951922402819297282.json、图片生成/图生图/FLUX图生图_1948702291495460865.json、图片生成/图生图/【阡陌】FLUX krea 反推提示词图生图工作流_1951533161555636225.json、图片生成/图生图/【阡陌】FLUX krea 图生图工作流_1951526547859648513.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 7/8 个有
- `DualCLIPLoader` —— 7/8 个有
- `FluxGuidance` —— 7/8 个有
- `UNETLoader` —— 7/8 个有
- `LayerUtility: JoyCaptionBeta1` —— 5/8 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 5/8 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 5/8 个有
- `ShowText|pysssss` —— 3/8 个有
- `DeepTranslatorTextNode` —— 2/8 个有
- `LoraLoader` —— 2/8 个有
- `CLIPTextEncodeFlux` —— 1/8 个有
- `CheckpointLoaderSimple` —— 1/8 个有
- `ConstrainImage|pysssss` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `NunchakuFluxDiTLoader` —— 1/8 个有
- `NunchakuTextEncoderLoaderV2` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 38 | 8 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | normal | - | 8 | 88% |
| 重绘幅度 | 0.9 | 0.6 - 1 | 8 | 83% |
| LoRA 模型强度 | 0.675 | - | 2 | 52% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 38，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 normal，8 个样本，一致性 88%
- 重绘幅度 中位数 0.9，观测区间 0.6 - 1，8 个样本，取值集中（一致性 83%）
- LoRA 模型强度 中位数 0.675，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
