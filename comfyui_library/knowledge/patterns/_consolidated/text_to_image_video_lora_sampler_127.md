---
name: text_to_image_video_lora_sampler_127
type: Text To Image
frequency: 6
level: strong
coverage: 0.523
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, EmptyLatentImage, GetNode, INTConstant, ImageFromBatch, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, Power Lora Loader (rgthree), SamplerCustom, SetNode, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimate2ContextOptions, WanAnimate2ToVideo, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/WanAnimate2动作迁移工作流｜一张图让角色跳舞_2100890163294597121.json, 视频生成/图生视频/WanAnimate2动作迁移工作流｜丝滑长视频人物替换生成_2097768858282184705.json, 视频生成/图生视频/WanAnimate2动作迁移模型｜丝滑长视频生成工作流_2095948603918475266.json, 视频生成/图生视频/WanAnimate2动作迁移｜图生视频精准复刻人物动作姿态_2101507280977092610.json, 视频生成/图生视频/WanAnimate2最强动作迁移｜王者归来丝滑长视频_2097960146419937281.json, 视频生成/图生视频/王者级动作迁移长视频｜WanAnimate2 丝滑换脸出片_2096236030365097986.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_127

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/WanAnimate2动作迁移工作流｜一张图让角色跳舞_2100890163294597121.json、视频生成/图生视频/WanAnimate2动作迁移工作流｜丝滑长视频人物替换生成_2097768858282184705.json、视频生成/图生视频/WanAnimate2动作迁移模型｜丝滑长视频生成工作流_2095948603918475266.json、视频生成/图生视频/WanAnimate2动作迁移｜图生视频精准复刻人物动作姿态_2101507280977092610.json、视频生成/图生视频/WanAnimate2最强动作迁移｜王者归来丝滑长视频_2097960146419937281.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `EmptyLatentImage`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Power Lora Loader (rgthree)`
- `SamplerCustom`
- `SetNode`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimate2ContextOptions`
- `WanAnimate2ToVideo`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `FastGroupsBypassSwitch` —— 5/6 个有
- `FeiHouWanAnimate2SeamColorMatch` —— 5/6 个有
- `FeiHouWanAnimate2ToVideo` —— 5/6 个有
- `Seed (rgthree)` —— 5/6 个有
- `WanAnimate2Cache` —— 4/6 个有
- `Int` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
