---
name: image_to_image_sampler_clip_vae_31
type: Image To Image
frequency: 7
level: strong
coverage: 0.905286
common_nodes: [CLIPTextEncode, ConditioningZeroOut, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/Joycaption 2 与Joycaption 3（beta one）效果对比_1926157024697151490.json, 图片生成/图生图/FLUX krea 反推提示词图生图工作流_1951922402819297282.json, 图片生成/图生图/【阡陌】FLUX krea 反推提示词图生图工作流_1951533161555636225.json, 图片生成/图生图/【阡陌】FLUX+LORA+Joy Caption 反推提示词图生图_1942197993288183810.json, 图片生成/图生图/【阡陌】Nunchaku8倍加速 flux joy反推图生图_1944745315662745601.json, 图片生成/图生图/反推洗图 美女图起号Joycaption 3（beta one）效果_1926990150398803970.json, 平台全量/镜头描述_1935614810891407362.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_31

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/反推提示词/Joycaption 2 与Joycaption 3（beta one）效果对比_1926157024697151490.json、图片生成/图生图/FLUX krea 反推提示词图生图工作流_1951922402819297282.json、图片生成/图生图/【阡陌】FLUX krea 反推提示词图生图工作流_1951533161555636225.json、图片生成/图生图/【阡陌】FLUX+LORA+Joy Caption 反推提示词图生图_1942197993288183810.json、图片生成/图生图/【阡陌】Nunchaku8倍加速 flux joy反推图生图_1944745315662745601.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 6/7 个有
- `FluxGuidance` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `ShowText|pysssss` —— 5/7 个有
- `CheckpointLoaderSimple` —— 3/7 个有
- `ConstrainImage|pysssss` —— 3/7 个有
- `DeepTranslatorTextNode` —— 2/7 个有
- `Joy_caption_two` —— 2/7 个有
- `Joy_caption_two_load` —— 2/7 个有
- `LoraLoader` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `NunchakuFluxDiTLoader` —— 1/7 个有
- `NunchakuTextEncoderLoaderV2` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 57% |
| 重绘幅度 | 1 | 0.6 - 1 | 7 | 82% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，7 个样本，取值集中（一致性 82%）
