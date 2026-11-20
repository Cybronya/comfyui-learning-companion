---
name: unknown_workflow_sampler_clip_unet_33
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.79035
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Moss Sft Fixed文生图_2112960432251166721.json, 图片生成/文生图/Moss 文生图 2K分辨率直出_2113627882475053058.json, 图片生成/文生图/Moss 文生图_2111394608352681986.json, 图片生成/文生图/Moss-Base Fixed文生图_2112960445203177473.json, 图片生成/文生图/Moss-Base文生图_2112960420595195905.json, 图片生成/文生图/Moss-Sft文生图-极简_2112960408704339969.json, 图片生成/文生图/Moss-image Sft文生图_自动词优化版_2112493550918258689.json, 图片生成/文生图/Moss-image Sft文生图_自动词优化版_2112499136711979009.json, 图片生成/文生图/Moss-image 文生图_2113858245021491201.json, 图片生成/文生图/Moss-image(文生图）_2111701557262766082.json, 图片生成/文生图/Moss-image+Base+Fixed文生图_2112225720482226178.json, 图片生成/文生图/Moss-image+Base文生图_2112079816290816001.json, 图片生成/文生图/Moss-image+Sft+Fixed文生图_2112225707626680321.json, 图片生成/文生图/Moss-image+Sft文生图_2112079796443369473.json, 图片生成/文生图/Moss-image_Base文生图高质量加速版V2(Un版)_2115259773263368194.json, 图片生成/文生图/Moss_Image_sft 无损加速工作流_2113974334170681345.json, 平台全量/MOSS_Image布局控制图像设计Sft+base_2118524928076107777.json, 平台全量/MOSS_Image布局控制图像设计Sft+base_2119016419772948482.json, 视频生成/文生视频/MOSS_Image布局控制图像设计Sft+base_2115293164587278337.json, 视频生成/文生视频/MOSS_Image布局控制图像设计Sft+base_2115304685547642882.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_33

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/Moss Sft Fixed文生图_2112960432251166721.json、图片生成/文生图/Moss 文生图 2K分辨率直出_2113627882475053058.json、图片生成/文生图/Moss 文生图_2111394608352681986.json、图片生成/文生图/Moss-Base Fixed文生图_2112960445203177473.json、图片生成/文生图/Moss-Base文生图_2112960420595195905.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 16/20 个有
- `PreviewAny` —— 15/20 个有
- `TextGenerate` —— 13/20 个有
- `ComfySwitchNode` —— 12/20 个有
- `PrimitiveBoolean` —— 12/20 个有
- `SkipLayerGuidanceDiTSimple` —— 9/20 个有
- `CreateBoundingBoxes` —— 5/20 个有
- `MOSSImageLayoutPrompt` —— 5/20 个有
- `LazyCache` —— 1/20 个有
- `MOSSImageBlockCacheT8` —— 1/20 个有
- `MOSSImagePromptEnhancerT8` —— 1/20 个有
- `easy showAnything` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 50 | 20 | 78% |
| Prompt 约束强度(CFG) | 3 | 2.5 - 3 | 20 | 91% |
| 采样算法 | er_sde | - | 20 | 90% |
| 调度器 | simple | - | 20 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 50，20 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 2.5 - 3，20 个样本，取值集中（一致性 91%）
- 采样算法 最常用 er_sde，20 个样本，一致性 90%
- 调度器 最常用 simple，20 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
