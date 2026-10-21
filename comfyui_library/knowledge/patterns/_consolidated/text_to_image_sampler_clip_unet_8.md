---
name: text_to_image_sampler_clip_unet_8
type: Text To Image
frequency: 20
level: weak
coverage: 0.86275
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image-base 多采样器对比工作流_2016377804211888130.json, 图片生成/文生图/z-image-turbo 文生图_1997981712913195009.json, 图片生成/文生图/z-image-turbo-基础工作流_2010586668142698498.json, 图片生成/文生图/z-image文生图工作流_1998291742837366786.json, 图片生成/文生图/z-image文生图工作流_2001830276877697026.json, 图片生成/文生图/z-image文生图工作流_2002604407730630657.json, 图片生成/文生图/z-image文生图工作流_2009919536497168386.json, 图片生成/文生图/z-image文生图工作流_2089710476165992450.json, 图片生成/文生图/z-image文生图工作流_2098948533117345794.json, 图片生成/文生图/z-image文生图工作流_2101933018976968706.json, 图片生成/文生图/zimage奇幻天宫_2087361360895242241.json, 图片生成/文生图/zimage广告图直出_2016732158576041986.json, 图片生成/文生图/zimage文生图+lora仙逆姚惜雪_2005983053098991617.json, 图片生成/文生图/zimage文生图+全息翼界lora_2014158819462488066.json, 图片生成/文生图/【尺素】krea2 turbo文生图_2069950720853499905.json, 图片生成/文生图/人物生成（自用）_2094050883234521090.json, 图片生成/文生图/阿清的偶像捏脸工作流_2057382985531478018.json, 数字人/数字人/【尺素】krea2 熟颜世绘_2078697317879865345.json, 数字人/数字人/尺素出品krea2熟颜世绘｜美少女文生图有味道，质感细腻很出片_2099462000886771713.json, 视频生成/文生视频/SeedVR2.5视频高清放大流｜老片新看画质逆袭_2098771107917688833.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_8

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/z-image-base 多采样器对比工作流_2016377804211888130.json、图片生成/文生图/z-image-turbo 文生图_1997981712913195009.json、图片生成/文生图/z-image-turbo-基础工作流_2010586668142698498.json、图片生成/文生图/z-image文生图工作流_1998291742837366786.json、图片生成/文生图/z-image文生图工作流_2001830276877697026.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 19/20 个有
- `ConditioningZeroOut` —— 16/20 个有
- `LoraLoaderModelOnly` —— 5/20 个有
- `SetNode` —— 5/20 个有
- `easy promptList` —— 5/20 个有
- `GetNode` —— 4/20 个有
- `INTConstant` —— 4/20 个有
- `ImageScaleToTotalPixels` —— 3/20 个有
- `SeedVR2LoadDiTModel` —— 3/20 个有
- `SeedVR2LoadVAEModel` —— 3/20 个有
- `SeedVR2VideoUpscaler` —— 3/20 个有
- `JjkText` —— 2/20 个有
- `ZImageLoraModelOnly` —— 2/20 个有
- `solarL_SaveImagesToZip` —— 2/20 个有
- `孤海注释` —— 2/20 个有
- `TTResolutionSelector` —— 1/20 个有
- `VHS_LoadVideo` —— 1/20 个有
- `VHS_VideoCombine` —— 1/20 个有
- `VHS_VideoInfo` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 50 | 20 | 15% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 20 | 24% |
| 采样算法 | euler | - | 20 | 75% |
| 调度器 | simple | - | 20 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 1024 | 80 - 1920 | 20 | 54% |
| 高度 | 1536 | 80 - 1920 | 20 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 50，20 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，20 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，20 个样本，一致性 75%
- 调度器 最常用 simple，20 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 80 - 1920，20 个样本
- 高度 中位数 1536，观测区间 80 - 1920，20 个样本
- 高发问题（16/20 个样本）：Steps较低可能导致细节不足
