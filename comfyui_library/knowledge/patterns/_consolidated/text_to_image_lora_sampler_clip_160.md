---
name: text_to_image_lora_sampler_clip_160
type: Text To Image
frequency: 11
level: moderate
coverage: 0.859727
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSampler, LoraLoaderModelOnly, ProcessString, SaveImage, Seed (rgthree), Text Concatenate, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/（自用）Red-Z-Image去网红感真实文生图V1(满血版)_1998238511566323714.json, 图片生成/文生图/（贞贞-大网渔网袜量贩版）Z-Image Eyes Deatailed自动扩写文生图V3_1995332136343363586.json, 图片生成/文生图/（贞贞-小情绪量贩版）Z-Image Art自动扩写文生图V1_2017607207981944834.json, 图片生成/文生图/（贞贞-小情绪量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1999764911616126977.json, 图片生成/文生图/（贞贞-量贩版）ZIT-Qwen 3B Engineer V4+ FLow Dop自动扩写文生图V5_2029102488133050370.json, 图片生成/文生图/（贞贞-黑丝量贩版）Z-Image Eyes Deatailed自动扩写文生图V5_1995332160846540801.json, 图片生成/文生图/（贞贞量贩版）Z-image Art自动扩写文生图V1_2017606389824233473.json, 图片生成/文生图/（贞贞量贩版）美少女自动扩写文生图V3_2003911286830317569.json, 图片生成/文生图/（量贩版）BEYOND REAL Z-Image加噪自动扩写文生图V1_2003060145137524737.json, 图片生成/文生图/（（自用）-黑丝连体衣量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1996115146386915330.json, 图片生成/文生图/🦖Z-Image文生图（批量-T8版可灰度）_1995390006330056706.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_160

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/（自用）Red-Z-Image去网红感真实文生图V1(满血版)_1998238511566323714.json、图片生成/文生图/（贞贞-大网渔网袜量贩版）Z-Image Eyes Deatailed自动扩写文生图V3_1995332136343363586.json、图片生成/文生图/（贞贞-小情绪量贩版）Z-Image Art自动扩写文生图V1_2017607207981944834.json、图片生成/文生图/（贞贞-小情绪量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1999764911616126977.json、图片生成/文生图/（贞贞-量贩版）ZIT-Qwen 3B Engineer V4+ FLow Dop自动扩写文生图V5_2029102488133050370.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
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
- `CR Text` —— 10/11 个有
- `CR Text Replace` —— 10/11 个有
- `LayerUtility: PurgeVRAM` —— 10/11 个有
- `RH_LLMAPI_Pro_Node` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `TT_img_enc` —— 3/11 个有
- `CheckpointLoaderSimple` —— 2/11 个有
- `RH_LLMAPI_NODE` —— 2/11 个有
- `TT_img_enc_v2` —— 2/11 个有
- `BasicScheduler` —— 1/11 个有
- `CFGGuider` —— 1/11 个有
- `CLIPLoaderGGUF` —— 1/11 个有
- `DetailDaemonSamplerNode` —— 1/11 个有
- `KSamplerSelect` —— 1/11 个有
- `RandomNoise` —— 1/11 个有
- `SamplerCustomAdvanced` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 1080 - 1920 | 11 | 73% |
| 高度 | 1080 | 1080 - 1920 | 11 | 71% |
| 采样步数 | 10 | 8 - 15 | 11 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 11 | 74% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，观测区间 1080 - 1920，11 个样本
- 高度 中位数 1080，观测区间 1080 - 1920，11 个样本
- 采样步数 中位数 10，观测区间 8 - 15，11 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
