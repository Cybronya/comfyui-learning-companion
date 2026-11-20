---
name: text_to_image_lora_sampler_clip_264
type: Text To Image
frequency: 8
level: strong
coverage: 0.83575
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/去AI感增强真实感工作流，MiniMax H3 LTX Wan图生视频动作迁移多合一_2103189879533424642.json, 图片生成/文生图/咖啡馆漫画风文生图工作流｜动漫角色场景插图｜氛围感出图利器_2101873892548759553.json, 图片生成/文生图/好玩的文生图工作流｜人物类特效创意出图神器_2098761942302289921.json, 图片生成/文生图/影视小说名及角色微观画卷Qwen-image名人节日省市支持国家微观画卷九宫格_2087469479310741505.json, 视频生成/文生视频/MiniMax H3 LTX Wan去AI感增强真实感视频处理工具_2102153536049082369.json, 视频生成/文生视频/MiniMax H3+LTX+Wan全家桶｜图生视频文生视频动作迁移三合一，去AI感增强真实感_2100439705560117249.json, 视频生成/文生视频/去AI感增强真实感合集｜MiniMax H3与LTX、Wan全模式生视频_2103071760437571586.json, 视频生成/文生视频/图生视频文生视频动作迁移去AI感增强真实感处理_2100637621520261121.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_264

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/去AI感增强真实感工作流，MiniMax H3 LTX Wan图生视频动作迁移多合一_2103189879533424642.json、图片生成/文生图/咖啡馆漫画风文生图工作流｜动漫角色场景插图｜氛围感出图利器_2101873892548759553.json、图片生成/文生图/好玩的文生图工作流｜人物类特效创意出图神器_2098761942302289921.json、图片生成/文生图/影视小说名及角色微观画卷Qwen-image名人节日省市支持国家微观画卷九宫格_2087469479310741505.json、视频生成/文生视频/MiniMax H3 LTX Wan去AI感增强真实感视频处理工具_2102153536049082369.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 6/8 个有
- `SaveImage` —— 6/8 个有
- `VHS_LoadVideo` —— 5/8 个有
- `VHS_VideoCombine` —— 5/8 个有
- `CheckpointLoaderSimple` —— 2/8 个有
- `DualCLIPLoader` —— 1/8 个有
- `FluxGuidance` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `WujiEditor` —— 1/8 个有
- `WujiSampler` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
