---
name: text_to_image_sampler_clip_vae_14
type: Text To Image
frequency: 10
level: moderate
coverage: 0.923
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Engineer-V4--文生图_2028091411702222850.json, 图片生成/文生图/Z-Image-SuperV3-文生图_2018341790440493058.json, 图片生成/文生图/Z-Image-Turbo + Lora 文生图_2008180292552495105.json, 图片生成/文生图/Z-Image-Turbo D-OPSD（提示词自动化）_2062196278603378689.json, 图片生成/文生图/Z-image文生图_2035961089313214465.json, 图片生成/文生图/redimage量贩美女图（全自动，批量，极速）_1998274589451018242.json, 图片生成/文生图/z-image_一张图片一次性洗多张一致性图片_1996107207425114113.json, 图片生成/文生图/【dpmpp2msde+sgm】皮肤纹理质感细腻 Z-Image 美女自动扩写+文生图+高清_1994569376554754049.json, 图片生成/文生图/【阿良绘】Z_Image+D-OPSD文生图 _ 多维批量生图：新装版（加速出图）_2073289207604592640.json, 图片生成/文生图/【阿良绘】Z_Image+D-OPSD文生图 _ 批量生图🔧_2057395173566533634.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_14

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Z-Image-Engineer-V4--文生图_2028091411702222850.json、图片生成/文生图/Z-Image-SuperV3-文生图_2018341790440493058.json、图片生成/文生图/Z-Image-Turbo + Lora 文生图_2008180292552495105.json、图片生成/文生图/Z-Image-Turbo D-OPSD（提示词自动化）_2062196278603378689.json、图片生成/文生图/Z-image文生图_2035961089313214465.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 9/10 个有
- `CR Prompt Text` —— 9/10 个有
- `LoraLoaderModelOnly` —— 9/10 个有
- `UNETLoader` —— 8/10 个有
- `JDCN_StringToList` —— 7/10 个有
- `ProcessString` —— 7/10 个有
- `Text Concatenate` —— 7/10 个有
- `LayerUtility: PurgeVRAM` —— 6/10 个有
- `RH_LLMAPI_Pro_Node` —— 6/10 个有
- `Seed (rgthree)` —— 6/10 个有
- `CR Text Replace` —— 5/10 个有
- `CR Text` —— 4/10 个有
- `easy showAnything` —— 4/10 个有
- `Any Switch (rgthree)` —— 2/10 个有
- `CheckpointLoaderSimple` —— 2/10 个有
- `KSamplerAdvanced` —— 2/10 个有
- `LoadImage` —— 2/10 个有
- `RunningHub Deepcleaner` —— 2/10 个有
- `CLIPLoaderGGUF` —— 1/10 个有
- `DuckHideNode` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `ImpactInt` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `Seed` —— 1/10 个有
- `SeedVR2` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1240 | 10 | 95% |
| 高度 | 1920 | 1664 - 1920 | 10 | 96% |
| 采样步数 | 10 | 8 - 15 | 8 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 12 | 10 | 0% |
| 采样算法 | euler | - | 10 | 50% |
| 调度器 | simple | - | 10 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1240，10 个样本，取值集中（一致性 95%）
- 高度 中位数 1920，观测区间 1664 - 1920，10 个样本，取值集中（一致性 96%）
- 采样步数 中位数 10，观测区间 8 - 15，8 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 12，10 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，10 个样本，一致性 50%
- 调度器 最常用 simple，10 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
