---
name: unknown_workflow_controlnet_lora_sampler_8
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.764286
common_nodes: [AIO_Preprocessor, Anything Everywhere3, ApplyPulidFlux, CLIPTextEncode, CR Simple Image Compare, CR Text Concatenate, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetNode, InstantIDFaceAnalysis, InstructPixToPixConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PulidFluxEvaClipLoader, PulidFluxModelLoader, RH_Captioner, RH_Translator, SaveImage, SetNode, SetUnionControlNetType, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/超棒真人转动漫风格风格转绘V3_1975112275407319041.json, 平台全量/【精准手绘】kontext手绘  超棒真人转动漫风格 风格转绘_1980098691249901570.json, 平台全量/超棒真人转动漫风格风格转绘V3_1894667543989125121.json, 平台全量/超棒真人转动漫风格风格转绘V3_1968947178196590593.json, 平台全量/超棒真人转动漫风格风格转绘V3_1968947917342007297.json, 平台全量/超棒真人转动漫风格风格转绘V3_1977337880798470145.json, 平台全量/超棒真人转动漫风格风格转绘V3_2066345599521583104.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_8

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/超棒真人转动漫风格风格转绘V3_1975112275407319041.json、平台全量/【精准手绘】kontext手绘  超棒真人转动漫风格 风格转绘_1980098691249901570.json、平台全量/超棒真人转动漫风格风格转绘V3_1894667543989125121.json、平台全量/超棒真人转动漫风格风格转绘V3_1968947178196590593.json、平台全量/超棒真人转动漫风格风格转绘V3_1968947917342007297.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 7 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `InstantIDFaceAnalysis`
- `InstructPixToPixConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxModelLoader`
- `RH_Captioner`
- `RH_Translator`
- `SaveImage`
- `SetNode`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 1/7 个有
- `VOSR2ModelLoader` —— 1/7 个有
- `VOSR2Upscale` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.6 - 0.6 | 7 | 100% |
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.6，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
