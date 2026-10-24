---
name: text_to_image_sampler_clip_unet_128
type: Text To Image
frequency: 5
level: strong
coverage: 0.7668
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Replace, ConditioningZeroOut, EmptyLatentImage, JDCN_StringToList, KSampler, ProcessString, RH_LLMAPI_Pro_Node, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物风格摄影 批量 港风梦幻 自动 生图 2.1_1995792225806192642.json, 图片生成/图生图/人物风格摄影美少女 圣诞写真 2.2_1997641285509033985.json, 图片生成/图生图/批量自动 胶片颗粒 人物风格摄影  生图 2.0_1995324105584992257.json, 图片生成/文生图/人物风格摄影美少女 自动扩写 生图 1.0_1994976217612869633.json, 图片生成/文生图/美少女量贩式生成_1994800940983181313.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_128

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/人物风格摄影 批量 港风梦幻 自动 生图 2.1_1995792225806192642.json、图片生成/图生图/人物风格摄影美少女 圣诞写真 2.2_1997641285509033985.json、图片生成/图生图/批量自动 胶片颗粒 人物风格摄影  生图 2.0_1995324105584992257.json、图片生成/文生图/人物风格摄影美少女 自动扩写 生图 1.0_1994976217612869633.json、图片生成/文生图/美少女量贩式生成_1994800940983181313.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Replace`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JDCN_StringToList`
- `KSampler`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `RHHiddenNodes` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `Text Concatenate` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `easy promptConcat` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `Float` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 5 | 100% |
| 高度 | 1920 | 1920 - 1920 | 5 | 100% |
| 采样步数 | 11 | 8 - 11 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 0.3 - 1 | 5 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 11，观测区间 8 - 11，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，5 个样本
