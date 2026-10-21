---
name: text_to_image_lora_sampler_clip_105
type: Text To Image
frequency: 10
level: strong
coverage: 0.8916
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSampler, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, ProcessString, SaveImage, Text Concatenate, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Red Z-Image Vs Z-image Turbo对比_1998113383687839745.json, 图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图(Pruned+Lora版)_1999788853470916609.json, 图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图V1(Pruned+Lora版)_1999758914910646273.json, 图片生成/文生图/Red-Z-Image去网红感真实文生图V1(Pruned+Lora可调权重版)_1998475968048168961.json, 图片生成/文生图/Red-Z-Image去网红感真实文生图V1(满血版)_1998238134959767554.json, 图片生成/文生图/Z-Image-Turbo  D-OPSD美少女文生图_2058718122760302593.json, 图片生成/文生图/Z-Image-Turbo D-OPSD美少女文生图V1_2058219333456842754.json, 图片生成/文生图/Z-Image-Turbo D-OPSD（提示词自动化）_2062196278603378689.json, 图片生成/文生图/Z-image 超快速美女孵蛋器超然升级版V1_1995339133893718018.json, 图片生成/文生图/Z-image全功能+网红美女爆图工作流_1995507321415598081.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_105

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Red Z-Image Vs Z-image Turbo对比_1998113383687839745.json、图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图(Pruned+Lora版)_1999788853470916609.json、图片生成/文生图/Red-Z-Image+Detail Deamon去网红感真实文生图V1(Pruned+Lora版)_1999758914910646273.json、图片生成/文生图/Red-Z-Image去网红感真实文生图V1(Pruned+Lora可调权重版)_1998475968048168961.json、图片生成/文生图/Red-Z-Image去网红感真实文生图V1(满血版)_1998238134959767554.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `ProcessString`
- `SaveImage`
- `Text Concatenate`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 9/10 个有
- `easy showAnything` —— 8/10 个有
- `RH_LLMAPI_Pro_Node` —— 6/10 个有
- `UNETLoader` —— 6/10 个有
- `CR Text` —— 5/10 个有
- `CR Text Replace` —— 5/10 个有
- `CheckpointLoaderSimple` —— 5/10 个有
- `Float` —— 3/10 个有
- `LoadImage` —— 3/10 个有
- `ImpactInt` —— 2/10 个有
- `JWFloat` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `DifferentialDiffusion` —— 1/10 个有
- `EmptySD3LatentImage` —— 1/10 个有
- `FluxGuidance` —— 1/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `InpaintModelConditioning` —— 1/10 个有
- `MaskBlur+` —— 1/10 个有
- `ModelSamplingAuraFlow` —— 1/10 个有
- `RH_Captioner` —— 1/10 个有
- `Seed` —— 1/10 个有
- `easy anythingIndexSwitch` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 10 | 100% |
| 高度 | 1920 | 1920 - 1920 | 10 | 100% |
| 采样步数 | 10 | 8 - 10 | 10 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 0.85 - 1 | 10 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，10 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 8 - 10，10 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 0.85 - 1，10 个样本，取值集中（一致性 95%）
