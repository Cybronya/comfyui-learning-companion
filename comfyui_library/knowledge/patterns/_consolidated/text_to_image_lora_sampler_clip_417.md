---
name: text_to_image_lora_sampler_clip_417
type: Text To Image
frequency: 4
level: strong
coverage: 0.859
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kontest 民俗风艺术照写真1_1984498079749586946.json, 图片生成/图生图/kontext 28项功能预设工作流_1982734162232786946.json, 图片生成/图生图/kontext-刺绣风格转换_1943252768754987009.json, 图片生成/图生图/kontext-玩偶风格转换_1941375169623703554.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_417

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/kontest 民俗风艺术照写真1_1984498079749586946.json、图片生成/图生图/kontext 28项功能预设工作流_1982734162232786946.json、图片生成/图生图/kontext-刺绣风格转换_1943252768754987009.json、图片生成/图生图/kontext-玩偶风格转换_1941375169623703554.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `RepeatLatentBatch` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `CR Prompt List` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `Primitive string multiline [Crystools]` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1024 - 1536 | 4 | 80% |
| 高度 | 1024 | 768 - 1680 | 4 | 70% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1280，观测区间 1024 - 1536，4 个样本，取值集中（一致性 80%）
- 高度 中位数 1024，观测区间 768 - 1680，4 个样本
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
