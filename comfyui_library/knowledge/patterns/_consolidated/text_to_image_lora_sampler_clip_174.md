---
name: text_to_image_lora_sampler_clip_174
type: Text To Image
frequency: 7
level: moderate
coverage: 0.887
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Replace, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSampler, LoraLoaderModelOnly, ProcessString, SaveImage, Seed (rgthree), Text Concatenate, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/redimage量贩美女图（全自动，批量，极速）_1998274589451018242.json, 图片生成/文生图/z-image_一张图片一次性洗多张一致性图片_1996107207425114113.json, 图片生成/文生图/【dpmpp2msde+sgm】皮肤纹理质感细腻 Z-Image 美女自动扩写+文生图+高清_1994569376554754049.json, 图片生成/文生图/【阿良绘】Z_Image+D-OPSD文生图 _ 多维批量生图：新装版（加速出图）_2073289207604592640.json, 图片生成/文生图/【阿良绘】Z_Image+D-OPSD文生图 _ 批量生图🔧_2057395173566533634.json, 图片生成/文生图/🏇超快速美女孵蛋器超然升级版V1🏇_1995296859344318466.json, 图片生成/文生图/🏇超快速美女孵蛋器超然升级版【本地版】🏇_1995302605654044674.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_174

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/redimage量贩美女图（全自动，批量，极速）_1998274589451018242.json、图片生成/文生图/z-image_一张图片一次性洗多张一致性图片_1996107207425114113.json、图片生成/文生图/【dpmpp2msde+sgm】皮肤纹理质感细腻 Z-Image 美女自动扩写+文生图+高清_1994569376554754049.json、图片生成/文生图/【阿良绘】Z_Image+D-OPSD文生图 _ 多维批量生图：新装版（加速出图）_2073289207604592640.json、图片生成/文生图/【阿良绘】Z_Image+D-OPSD文生图 _ 批量生图🔧_2057395173566533634.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Replace`
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

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/7 个有
- `RH_LLMAPI_Pro_Node` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `LayerUtility: PurgeVRAM` —— 5/7 个有
- `ImpactInt` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `Any Switch (rgthree)` —— 2/7 个有
- `KSamplerAdvanced` —— 2/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `RunningHub Deepcleaner` —— 2/7 个有
- `easy anythingIndexSwitch` —— 2/7 个有
- `CheckpointLoaderSimple` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `Qwen3VL_Chat` —— 1/7 个有
- `SeedVR2` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 12 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 12 | 7 | 0% |
| 采样算法 | euler_ancestral | - | 7 | 43% |
| 调度器 | sgm_uniform | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1080 | 1080 - 1240 | 7 | 95% |
| 高度 | 1920 | 1664 - 1920 | 7 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 12，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 12，7 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 43%
- 调度器 最常用 sgm_uniform，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1240，7 个样本，取值集中（一致性 95%）
- 高度 中位数 1920，观测区间 1664 - 1920，7 个样本，取值集中（一致性 95%）
