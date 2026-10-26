---
name: text_to_image_sampler_clip_unet_81
type: Text To Image
frequency: 8
level: moderate
coverage: 0.788875
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSampler, ProcessString, RH_LLMAPI_Pro_Node, SaveImage, Text Concatenate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物风格摄影 批量 港风梦幻 自动 生图 2.1_1995792225806192642.json, 图片生成/图生图/人物风格摄影美少女 圣诞写真 2.2_1997641285509033985.json, 图片生成/图生图/批量自动 胶片颗粒 人物风格摄影  生图 2.0_1995324105584992257.json, 图片生成/文生图/Z-Image-Turbo D-OPSD（提示词自动化）_2062196278603378689.json, 图片生成/文生图/【dpmpp2msde+sgm】皮肤纹理质感细腻 Z-Image 美女自动扩写+文生图+高清_1994569376554754049.json, 图片生成/文生图/【阿良绘】Z_Image+D-OPSD文生图 _ 多维批量生图：新装版（加速出图）_2073289207604592640.json, 图片生成/文生图/【阿良绘】Z_Image+D-OPSD文生图 _ 批量生图🔧_2057395173566533634.json, 图片生成/文生图/人物风格摄影美少女 自动扩写 生图 1.0_1994976217612869633.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_81

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/人物风格摄影 批量 港风梦幻 自动 生图 2.1_1995792225806192642.json、图片生成/图生图/人物风格摄影美少女 圣诞写真 2.2_1997641285509033985.json、图片生成/图生图/批量自动 胶片颗粒 人物风格摄影  生图 2.0_1995324105584992257.json、图片生成/文生图/Z-Image-Turbo D-OPSD（提示词自动化）_2062196278603378689.json、图片生成/文生图/【dpmpp2msde+sgm】皮肤纹理质感细腻 Z-Image 美女自动扩写+文生图+高清_1994569376554754049.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Replace` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `easy showAnything` —— 6/8 个有
- `LayerUtility: PurgeVRAM` —— 5/8 个有
- `LoadImage` —— 5/8 个有
- `ShowText|pysssss` —— 5/8 个有
- `CR Prompt Text` —— 4/8 个有
- `JjkText` —— 4/8 个有
- `RHHiddenNodes` —— 4/8 个有
- `CR Text` —— 3/8 个有
- `Seed (rgthree)` —— 3/8 个有
- `Any Switch (rgthree)` —— 2/8 个有
- `KSamplerAdvanced` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `RunningHub Deepcleaner` —— 2/8 个有
- `easy promptConcat` —— 2/8 个有
- `Float` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `Seed` —— 1/8 个有
- `SeedVR2` —— 1/8 个有
- `SetNode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1240 | 8 | 95% |
| 高度 | 1920 | 1664 - 1920 | 8 | 96% |
| 采样步数 | 11 | 8 - 12 | 6 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 12 | 8 | 0% |
| 采样算法 | euler | - | 8 | 62% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 0.3 - 1 | 6 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1240，8 个样本，取值集中（一致性 95%）
- 高度 中位数 1920，观测区间 1664 - 1920，8 个样本，取值集中（一致性 96%）
- 采样步数 中位数 11，观测区间 8 - 12，6 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 12，8 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，6 个样本
- 高发问题（5/8 个样本）：Steps较低可能导致细节不足
