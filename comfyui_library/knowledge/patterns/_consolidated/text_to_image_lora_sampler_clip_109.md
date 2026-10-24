---
name: text_to_image_lora_sampler_clip_109
type: Text To Image
frequency: 13
level: moderate
coverage: 0.855154
common_nodes: [CLIPTextEncode, CR Prompt Text, CR Text, CR Text Replace, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSampler, LoraLoaderModelOnly, ProcessString, RH_LLMAPI_Pro_Node, SaveImage, Seed (rgthree), Text Concatenate, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/量贩版 ZIT-D-OPSD美少女文生图（自动化批量出图）_2066140658238316545.json, 图片生成/文生图/（小情绪量贩版）Z-Image Art自动扩写文生图V1_2017609951325196290.json, 图片生成/文生图/（贞贞-Coser量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2057773705002053634.json, 图片生成/文生图/（贞贞-大网渔网袜量贩版）Z-Image Eyes Deatailed自动扩写文生图V3_1995332136343363586.json, 图片生成/文生图/（贞贞-小情绪量贩版）Z-Image Art自动扩写文生图V1_2017607207981944834.json, 图片生成/文生图/（贞贞-小情绪量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1999764911616126977.json, 图片生成/文生图/（贞贞-量贩版）ZIT-Qwen 3B Engineer V4+ FLow Dop自动扩写文生图V5_2029102488133050370.json, 图片生成/文生图/（贞贞-黑丝量贩版）Z-Image Eyes Deatailed自动扩写文生图V5_1995332160846540801.json, 图片生成/文生图/（贞贞量贩版）Z-image Art自动扩写文生图V1_2017606389824233473.json, 图片生成/文生图/（贞贞量贩版）美少女自动扩写文生图V3_2003911286830317569.json, 图片生成/文生图/（量贩版）BEYOND REAL Z-Image加噪自动扩写文生图V1_2003060145137524737.json, 图片生成/文生图/（量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2056786094817112066.json, 图片生成/文生图/（量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2065067678041198593.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_109

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/量贩版 ZIT-D-OPSD美少女文生图（自动化批量出图）_2066140658238316545.json、图片生成/文生图/（小情绪量贩版）Z-Image Art自动扩写文生图V1_2017609951325196290.json、图片生成/文生图/（贞贞-Coser量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2057773705002053634.json、图片生成/文生图/（贞贞-大网渔网袜量贩版）Z-Image Eyes Deatailed自动扩写文生图V3_1995332136343363586.json、图片生成/文生图/（贞贞-小情绪量贩版）Z-Image Art自动扩写文生图V1_2017607207981944834.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `CR Text Replace`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LoraLoaderModelOnly`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `Seed (rgthree)`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 12/13 个有
- `CLIPLoader` —— 9/13 个有
- `ClipLoaderGGUF` —— 4/13 个有
- `PreviewAny` —— 4/13 个有
- `QwenImageEngineer` —— 4/13 个有
- `easy cleanGpuUsed` —— 4/13 个有
- `RH_LLMAPI_NODE` —— 2/13 个有
- `BasicScheduler` —— 1/13 个有
- `CFGGuider` —— 1/13 个有
- `CLIPLoaderGGUF` —— 1/13 个有
- `DetailDaemonSamplerNode` —— 1/13 个有
- `KSamplerSelect` —— 1/13 个有
- `RandomNoise` —— 1/13 个有
- `SamplerCustomAdvanced` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 15 | 13 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 13 | 75% |
| 采样算法 | euler | - | 13 | 92% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1080 | 1080 - 1920 | 13 | 71% |
| 高度 | 1920 | 1080 - 1920 | 13 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 15，13 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 92%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1920，13 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，13 个样本
