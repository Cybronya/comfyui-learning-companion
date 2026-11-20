---
name: image_to_image_sampler_clip_unet_91
type: Image To Image
frequency: 7
level: strong
coverage: 0.907714
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/老照片修复+上色-kontext dev开源_1943087447620141057.json, 平台全量/老照片划痕清理工作流-Flux Kontext 保留原色调_2096574494428192770.json, 平台全量/角色三视图 生成人物角色三视图_2034433147311497217.json, 平台全量/超好用的老照片修复工作流_2026228455569887233.json, 平台全量/阮旭东aigc：仿 全能图片V1 3d渲染打印工作流（含supir放大+前后对比）_1960960023000231937.json, 视频生成/图生视频/精修(全能)-kontext_2048657663176740866.json, 视频生成/图生视频/🦖一秒变胖子_1947223142697750530.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_91

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/老照片修复+上色-kontext dev开源_1943087447620141057.json、平台全量/老照片划痕清理工作流-Flux Kontext 保留原色调_2096574494428192770.json、平台全量/角色三视图 生成人物角色三视图_2034433147311497217.json、平台全量/超好用的老照片修复工作流_2026228455569887233.json、平台全量/阮旭东aigc：仿 全能图片V1 3d渲染打印工作流（含supir放大+前后对比）_1960960023000231937.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `FluxKontextImageScale` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `SaveImage` —— 6/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `RH_Translator` —— 3/7 个有
- `PreviewImage` —— 2/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `JWInteger` —— 1/7 个有
- `Preview from image [Crystools]` —— 1/7 个有
- `RepeatLatentBatch` —— 1/7 个有
- `SUPIR_Upscale` —— 1/7 个有
- `VHS_LoadVideoFFmpeg` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 25 | 7 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 25，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
