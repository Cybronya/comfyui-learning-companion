---
name: text_to_image_lora_sampler_clip_88
type: Text To Image
frequency: 11
level: strong
coverage: 0.851545
common_nodes: [CLIPTextEncode, CR Text Replace, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSampler, LoraLoaderModelOnly, ProcessString, RH_LLMAPI_Pro_Node, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/人物风格摄影美少女 自动扩写 生图 1.0_1994976217612869633.json, 图片生成/文生图/美女模特 反推提示词 图片裂变 9宫格分镜图 洗图  Z-Image-Turbo D-OPSD_2056920485178462210.json, 图片生成/文生图/美少女量贩式生成_1994800940983181313.json, 图片生成/文生图/量贩版 ZIT-D-OPSD美少女文生图（自动化批量出图）_2066140658238316545.json, 图片生成/文生图/（小情绪量贩版）Z-Image Art自动扩写文生图V1_2017609951325196290.json, 图片生成/文生图/（贞贞-Coser量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2057773705002053634.json, 图片生成/文生图/（量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1994411563819864066.json, 图片生成/文生图/（量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2056786094817112066.json, 图片生成/文生图/（量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2065067678041198593.json, 图片生成/文生图/（量贩版）Z-image Art自动扩写文生图V1_2017609963115384833.json, 图片生成/文生图/（黑丝量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1994961305289285634.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_88

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/人物风格摄影美少女 自动扩写 生图 1.0_1994976217612869633.json、图片生成/文生图/美女模特 反推提示词 图片裂变 9宫格分镜图 洗图  Z-Image-Turbo D-OPSD_2056920485178462210.json、图片生成/文生图/美少女量贩式生成_1994800940983181313.json、图片生成/文生图/量贩版 ZIT-D-OPSD美少女文生图（自动化批量出图）_2066140658238316545.json、图片生成/文生图/（小情绪量贩版）Z-Image Art自动扩写文生图V1_2017609951325196290.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text Replace`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `LoraLoaderModelOnly`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 10/11 个有
- `LayerUtility: PurgeVRAM` —— 10/11 个有
- `Text Concatenate` —— 10/11 个有
- `CR Text` —— 9/11 个有
- `Seed (rgthree)` —— 9/11 个有
- `CLIPLoader` —— 7/11 个有
- `PreviewAny` —— 5/11 个有
- `ClipLoaderGGUF` —— 4/11 个有
- `QwenImageEngineer` —— 4/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `LoadImage` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `RHHiddenNodes` —— 1/11 个有
- `RH_Captioner` —— 1/11 个有
- `ShowText|pysssss` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 11 | 11 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 1080 | 1080 - 1920 | 11 | 79% |
| 高度 | 1920 | 1080 - 1920 | 11 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 11，11 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1920，11 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，11 个样本，取值集中（一致性 87%）
