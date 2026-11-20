---
name: unknown_workflow_sampler_checkpoint_vae_3
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.810143
common_nodes: [CFGNorm, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxResolutionNode, GetImageSize, ImageConcanate, ImageConcatMulti, ImageScaleToTotalPixels, ImpactInt, ImpactMinMax, ImpactSwitch, KSampler, LoadImage, PreviewImage, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, Text Multiline, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型 (1)_2069953874483572737.json, 图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型 (2)_2071783247616495618.json, 图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型_2045422561068064770.json, 图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型_2065254345502978050.json, 图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型_2066768944584814593.json, 图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型_2067486112062459905.json, 图片生成/图生图/Qwen-Edit-2511-AIO-多功能-多图编辑工作流_2049697649493848066.json, 图片生成/图生图/Qwen-Rapid-AIO 最新V23 Image-Edit 多功能融合模型_2017613952586354689.json, 图片生成/图生图/Qwen-Rapid-AIO_V23_多图编辑，姿势修改，去水印，换装，换背景，SFW，高清放大_2025911454716665857.json, 图片生成/图生图/QwenEdit2511AIO多功能多图编辑工作流_2059086839411208194.json, 图片生成/图生图/QwenEdit2511AIO多功能多图编辑工作流_2062036010137112578.json, 图片生成/图生图/v18+Image-Edit-Rapid-AIO融合模型_2013776317078052865.json, 图片生成/图生图/三图融合_2007121347767443457.json, 图片生成/图生图/双图融合 双图  角色与场景结合 Qwen-Rapid-AIO_2034449613838618626.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_3

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型 (1)_2069953874483572737.json、图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型 (2)_2071783247616495618.json、图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型_2045422561068064770.json、图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型_2065254345502978050.json、图片生成/图生图/Image-Edit-Rapid-AIO多功能融合模型_2066768944584814593.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGNorm`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxResolutionNode`
- `GetImageSize`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `ImpactInt`
- `ImpactMinMax`
- `ImpactSwitch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 13/14 个有
- `RH_LLMAPI_NODE` —— 10/14 个有
- `easy showAnything` —— 10/14 个有
- `HAIGC_LoadImagesFromZip` —— 4/14 个有
- `Image Comparer (rgthree)` —— 4/14 个有
- `ImageScaleBy` —— 4/14 个有
- `LoraLoaderModelOnly` —— 4/14 个有
- `MemoryCleaner` —— 4/14 个有
- `SeedVR2LoadDiTModel` —— 4/14 个有
- `SeedVR2LoadVAEModel` —— 4/14 个有
- `SeedVR2VideoUpscaler` —— 4/14 个有
- `easy cleanGpuUsed` —— 4/14 个有
- `GetNode` —— 3/14 个有
- `Label (rgthree)` —— 3/14 个有
- `SetNode` —— 3/14 个有
- `PlaySound|pysssss` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 14 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler_ancestral | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 512 | 512 - 512 | 14 | 100% |
| 高度 | 512 | 512 - 512 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，14 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
