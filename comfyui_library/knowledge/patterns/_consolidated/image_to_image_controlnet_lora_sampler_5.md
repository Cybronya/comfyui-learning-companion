---
name: image_to_image_controlnet_lora_sampler_5
type: Image To Image
frequency: 5
level: strong
coverage: 0.7874
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Simple Image Compare, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetNode, InstructPixToPixConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SetNode, SetUnionControlNetType, ShowText|pysssss, StyleModelApplySimple, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss, easy promptConcat, easy stylesSelector]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动漫转绘真人风格_2007629065053806594.json, 图片生成/图生图/超强的！动漫转真人风格V3！光速出图_2054491953286402050.json, 平台全量/动漫转绘真人风格_1941878818359635970.json, 平台全量/超棒的！动漫转绘真人风格V3！_1906556416297979905.json, 平台全量/超棒的！动漫转绘真人风格V3！_2066345489182027776.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/动漫转绘真人风格_2007629065053806594.json、图片生成/图生图/超强的！动漫转真人风格V3！光速出图_2054491953286402050.json、平台全量/动漫转绘真人风格_1941878818359635970.json、平台全量/超棒的！动漫转绘真人风格V3！_1906556416297979905.json、平台全量/超棒的！动漫转绘真人风格V3！_2066345489182027776.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Simple Image Compare`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `InstructPixToPixConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `StyleModelApplySimple`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`
- `easy promptConcat`
- `easy stylesSelector`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 4/5 个有
- `Prompts Everywhere` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `Int` —— 1/5 个有
- `VOSR2ModelLoader` —— 1/5 个有
- `VOSR2Upscale` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 0.3 | 0.3 - 0.3 | 5 | 100% |
| ControlNet 权重 | 0.4 | 0.4 - 0.4 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.3，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.4，观测区间 0.4 - 0.4，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
