---
name: text_to_image_lora_sampler_clip_275
type: Text To Image
frequency: 7
level: strong
coverage: 0.856714
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSampler, LoraLoaderModelOnly, ProcessString, SaveImage, Seed (rgthree), Text Concatenate, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/（自用）Red-Z-Image去网红感真实文生图V1(满血版)_1998238511566323714.json, 图片生成/文生图/（量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1994411563819864066.json, 图片生成/文生图/（量贩版）Z-image Art自动扩写文生图V1_2017609963115384833.json, 图片生成/文生图/（量贩装）Red-Z-Image去网红感自动提示词真实文生图V1(满血版)_1998237684017586177.json, 图片生成/文生图/（黑丝量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1994961305289285634.json, 图片生成/文生图/（（自用）-黑丝连体衣量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1996115146386915330.json, 图片生成/文生图/🦖Z-Image文生图（批量-T8版可灰度）_1995390006330056706.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_275

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/（自用）Red-Z-Image去网红感真实文生图V1(满血版)_1998238511566323714.json、图片生成/文生图/（量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1994411563819864066.json、图片生成/文生图/（量贩版）Z-image Art自动扩写文生图V1_2017609963115384833.json、图片生成/文生图/（量贩装）Red-Z-Image去网红感自动提示词真实文生图V1(满血版)_1998237684017586177.json、图片生成/文生图/（黑丝量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1994961305289285634.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LoraLoaderModelOnly`
- `ProcessString`
- `SaveImage`
- `Seed (rgthree)`
- `Text Concatenate`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/7 个有
- `CR Text Replace` —— 6/7 个有
- `LayerUtility: PurgeVRAM` —— 6/7 个有
- `RH_LLMAPI_Pro_Node` —— 6/7 个有
- `UNETLoader` —— 5/7 个有
- `CheckpointLoaderSimple` —— 3/7 个有
- `TT_img_enc` —— 3/7 个有
- `TT_img_enc_v2` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1920 | 7 | 76% |
| 高度 | 1920 | 1080 - 1920 | 7 | 84% |
| 采样步数 | 10 | 8 - 10 | 7 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1920，7 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，7 个样本，取值集中（一致性 84%）
- 采样步数 中位数 10，观测区间 8 - 10，7 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
