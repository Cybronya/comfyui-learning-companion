---
name: text_to_image_lora_sampler_clip_302
type: Text To Image
frequency: 7
level: strong
coverage: 0.934857
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/效果图洗图增强细节工作流｜AI渲染秒变真实感照片级_2103739286116986881.json, 图片生成/图生图/欧卡风格转换2工作流｜图生图风格随意切换_2098729696782536706.json, 图片生成/图生图/欧美Q版UI图标生成 风格转换图标设计工具_2098868749016322050.json, 图片生成/图生图/欧美风Q版UI图标批量生成｜图生图一键出全套界面素材_2099103509873516546.json, 图片生成/图生图/角色三视图一键生成｜Klein9b图生图角色设计_2090875375202164737.json, 图片生成/图生图/角色正视图和三视图工作流｜图生图立绘设定神器_2100800199663906818.json, 视频生成/图生视频/Flux2Klein多图编辑9B加速版｜换脸换装都顺手｜图生视频前处理首选_2102632847407407106.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_302

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/效果图洗图增强细节工作流｜AI渲染秒变真实感照片级_2103739286116986881.json、图片生成/图生图/欧卡风格转换2工作流｜图生图风格随意切换_2098729696782536706.json、图片生成/图生图/欧美Q版UI图标生成 风格转换图标设计工具_2098868749016322050.json、图片生成/图生图/欧美风Q版UI图标批量生成｜图生图一键出全套界面素材_2099103509873516546.json、图片生成/图生图/角色三视图一键生成｜Klein9b图生图角色设计_2090875375202164737.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 4/7 个有
- `KSamplerSelect` —— 4/7 个有
- `RandomNoise` —— 4/7 个有
- `SamplerCustomAdvanced` —— 4/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `孤海图像缩放按像素` —— 3/7 个有
- `BasicScheduler` —— 2/7 个有
- `Flux2Scheduler` —— 2/7 个有
- `GetImageSize` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `ImageConcatMulti` —— 1/7 个有
- `Int` —— 1/7 个有
- `JWImageResizeByLongerSide` —— 1/7 个有
- `LoraLoaderBypassModelOnly` —— 1/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（10/7 个样本）：Steps较低可能导致细节不足
