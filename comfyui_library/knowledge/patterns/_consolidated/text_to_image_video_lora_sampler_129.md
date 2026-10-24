---
name: text_to_image_video_lora_sampler_129
type: Text To Image
frequency: 5
level: strong
coverage: 0.9196
common_nodes: [BasicScheduler, BatchImagesNode, BerniniConditioning, CLIPLoader, CLIPTextEncode, CR Text, CreateVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetVideoComponents, INTConstant, ImageConcanate, ImageFromBatch, Int, JjkText, KSampler, KSamplerSelect, LoadImage, LoadVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, SaveVideo, SimpleMath+, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/bernini视频编辑三合一 wan2.2人物替换动作迁移全支持_2095076398569443330.json, 图片生成/图生图/bernini视频编辑三合一 wan2.2人物替换动作迁移全支持_2097470311955521538.json, 图片生成/图生图/bernini视频编辑三合一 wan2.2人物替换动作迁移全支持_2099398714593996802.json, 图片生成/图生图/bernini视频编辑人物替换｜wan2.2动作迁移换背景_2093411808987148290.json, 图片生成/图生图/bernini视频编辑｜wan2.2人物替换动作迁移换背景_2093736057765453825.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_129

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/bernini视频编辑三合一 wan2.2人物替换动作迁移全支持_2095076398569443330.json、图片生成/图生图/bernini视频编辑三合一 wan2.2人物替换动作迁移全支持_2097470311955521538.json、图片生成/图生图/bernini视频编辑三合一 wan2.2人物替换动作迁移全支持_2099398714593996802.json、图片生成/图生图/bernini视频编辑人物替换｜wan2.2动作迁移换背景_2093411808987148290.json、图片生成/图生图/bernini视频编辑｜wan2.2人物替换动作迁移换背景_2093736057765453825.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetVideoComponents`
- `INTConstant`
- `ImageConcanate`
- `ImageFromBatch`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SaveVideo`
- `SimpleMath+`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
