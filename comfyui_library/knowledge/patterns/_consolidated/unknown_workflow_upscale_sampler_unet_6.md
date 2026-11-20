---
name: unknown_workflow_upscale_sampler_unet_6
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.676444
common_nodes: [CLIPLoader, CR Text, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, PainterFluxImageEdit, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy imageRemBg, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein万物换背景-人物、产品等更换背景加强版-直出4K_2053352211169726465.json, 图片生成/图生图/人物、产品等更换背景加强版-直出4K-Flux2-Klein_2052208582476746753.json, 图片生成/图生图/人物、产品等更换背景加强版-直出4K-Flux2-Klein_2056207912913121282.json, 图片生成/图生图/人物、产品等更换背景加强版-直出4K-Flux2-Klein万物换背景生成器_2052615144416530434.json, 图片生成/图生图/换头、换脸4K高度还原_2058061127715741698.json, 平台全量/人物_产品背景更换Flux-2-klein-9B高清放大直出4K_2026525642497462273.json, 平台全量/人物、产品等更换背景加强版-直出4K-Flux2-Klein_2016320728475377666.json, 平台全量/人物、产品等更换背景加强版-直出4K-Flux2-Klein_2055552821348585473.json, 平台全量/换头、换脸提高相似度优化版-直出4K-可自定义输出分辨率-Flux 2 Klein_2016320048398344193.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_6

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein万物换背景-人物、产品等更换背景加强版-直出4K_2053352211169726465.json、图片生成/图生图/人物、产品等更换背景加强版-直出4K-Flux2-Klein_2052208582476746753.json、图片生成/图生图/人物、产品等更换背景加强版-直出4K-Flux2-Klein_2056207912913121282.json、图片生成/图生图/人物、产品等更换背景加强版-直出4K-Flux2-Klein万物换背景生成器_2052615144416530434.json、图片生成/图生图/换头、换脸4K高度还原_2058061127715741698.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PainterFluxImageEdit`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageRemBg`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `GrowMaskWithBlur` —— 7/9 个有
- `ImageResizeAdvanced` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `RH_LLMAPI_Pro_Node` —— 7/9 个有
- `easy imageDetailTransfer` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `MaskPreview+` —— 2/9 个有
- `SolidMask` —— 2/9 个有
- `easy ifElse` —— 2/9 个有
- `easy int` —— 2/9 个有
- `easy isMaskEmpty` —— 2/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 9 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | sgm_uniform | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，9 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
