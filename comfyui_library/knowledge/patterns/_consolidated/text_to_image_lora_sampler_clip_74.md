---
name: text_to_image_lora_sampler_clip_74
type: Text To Image
frequency: 12
level: weak
coverage: 0.870833
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleBy, KSampler, LoraLoaderModelOnly, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2 + Flux2-Klein文生图_2096577029973041153.json, 图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2071552520446636033.json, 图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2071597722657968129.json, 图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2088834570824273922.json, 图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模王炸合体_2071802083606618114.json, 图片生成/文生图/Krea2+zimage双采极致风格参考_2074326036057255937.json, 图片生成/文生图/Krea2影视资产生成V1_2103524349650235394.json, 图片生成/文生图/Krea2影视资产生成工作流，文生图影视素材快速产出工具_2103978065222266882.json, 图片生成/文生图/krea2 二次采样+细节修复_2079377686283243522.json, 图片生成/文生图/krea2+zit+flux2-klein三采极致图_2080093488003248130.json, 图片生成/文生图/三模合体王炸｜Krea2+Z-Image Turbo+Flux2-Klein 文生图_2089298165005639682.json, 图片生成/文生图/邪修krea2单模型双采，细节拉满！（萌妹lora版）_2079122786253103105.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_74

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Krea2 + Flux2-Klein文生图_2096577029973041153.json、图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2071552520446636033.json、图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2071597722657968129.json、图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模合体，直接王炸！_2088834570824273922.json、图片生成/文生图/Krea2 + Z-Image Turbo + Flux2-Klein三模王炸合体_2071802083606618114.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 11/12 个有
- `CR Text` —— 11/12 个有
- `ColorMatch` —— 11/12 个有
- `EmptyFlux2LatentImage` —— 11/12 个有
- `Flux2Scheduler` —— 11/12 个有
- `GetImageSize` —— 11/12 个有
- `KSamplerSelect` —— 11/12 个有
- `LCSColorAnchor` —— 11/12 个有
- `LCSLoadData` —— 11/12 个有
- `LCSSharpnessCalibrate` —— 11/12 个有
- `LCSSharpnessIntervene` —— 11/12 个有
- `RandomNoise` —— 11/12 个有
- `ReferenceLatent` —— 11/12 个有
- `SamplerCustomAdvanced` —— 11/12 个有
- `TTResolutionSelector` —— 11/12 个有
- `ImageResize+` —— 10/12 个有
- `SeedVR2LoadDiTModel` —— 10/12 个有
- `SeedVR2LoadVAEModel` —— 10/12 个有
- `SeedVR2VideoUpscaler` —— 10/12 个有
- `TTP_Image_Assy` —— 10/12 个有
- `TTP_Image_Tile_Batch` —— 10/12 个有
- `TTP_Tile_image_size` —— 10/12 个有
- `easy imageSize` —— 10/12 个有
- `GetNode` —— 9/12 个有
- `ImageScaleToTotalPixels` —— 9/12 个有
- `Label (rgthree)` —— 9/12 个有
- `PreviewImage` —— 9/12 个有
- `easy cleanGpuUsed` —— 9/12 个有
- `CLIPLoaderGGUF` —— 7/12 个有
- `ConditioningKrea2Rebalance` —— 5/12 个有
- `ColorMatchV2` —— 2/12 个有
- `JjkText` —— 2/12 个有
- `KSamplerAdvanced` —— 2/12 个有
- `LatentUpscaleBy` —— 2/12 个有
- `ModelAttentionBackend` —— 2/12 个有
- `easy promptList` —— 2/12 个有
- `solarL_SaveImagesToZip` —— 2/12 个有
- `孤海注释` —— 2/12 个有
- `GODMT_MergeList` —— 1/12 个有
- `Krea2StyleReference` —— 1/12 个有
- `Krea2StyleTransfer` —— 1/12 个有
- `LoadImage` —— 1/12 个有
- `MemoryCleaner` —— 1/12 个有
- `Text` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1920 | 12 | 51% |
| 高度 | 1024 | 80 - 1080 | 12 | 59% |
| 采样步数 | 6 | 4 - 8 | 10 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 12 | 3% |
| 采样算法 | euler | - | 12 | 67% |
| 调度器 | simple | - | 12 | 67% |
| 重绘幅度 | 0.3 | 0.25 - 1 | 10 | 36% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1920，12 个样本
- 高度 中位数 1024，观测区间 80 - 1080，12 个样本
- 采样步数 中位数 6，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，12 个样本，取值分散，一致性仅 3%
- 采样算法 最常用 euler，12 个样本，一致性 67%
- 调度器 最常用 simple，12 个样本，一致性 67%
- 重绘幅度 中位数 0.3，观测区间 0.25 - 1，10 个样本，取值分散，一致性仅 36%
- 高发问题（21/12 个样本）：Steps较低可能导致细节不足
