---
name: text_to_image_video_lora_sampler_118
type: Text To Image
frequency: 6
level: weak
coverage: 0.763333
common_nodes: [ACE_TextConcatenate, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DiffusionModelLoaderKJ, EmptyLatentImage, EnhancedLoadDiffusionModel, FluxKontextMultiReferenceLatentMethod, GetImageSize, GetNode, ImageBatchExtendWithOverlap, ImageFromBatch+, Int, JDCN_StringToList, KSampler, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveFloat, Qwen3_VQA, RandomInt, RunningHub Deepcleaner, SetNode, Text, TextConcatenate_UTK, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy imageListToImageBatch, easy indexAnything, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/そんなことしないでよ_2022575986100932609.json, 视频生成/图生视频/そんなことしないでよ｜分镜出图图生视频一键生成_2095795519737122818.json, 视频生成/图生视频/そんなことしないでよ｜分镜出图图生视频生成_2092153729062625282.json, 视频生成/图生视频/分镜生成出图图生视频｜そんなことしないでよ视频工作流_2088171760624685058.json, 视频生成/图生视频/分镜生成图生视频 多参考图创作处理生成工具_2100279975579574274.json, 视频生成/图生视频/2014185518350737409.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_118

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/そんなことしないでよ_2022575986100932609.json、视频生成/图生视频/そんなことしないでよ｜分镜出图图生视频一键生成_2095795519737122818.json、视频生成/图生视频/そんなことしないでよ｜分镜出图图生视频生成_2092153729062625282.json、视频生成/图生视频/分镜生成出图图生视频｜そんなことしないでよ视频工作流_2088171760624685058.json、视频生成/图生视频/分镜生成图生视频 多参考图创作处理生成工具_2100279975579574274.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
- `ACE_TextConcatenate`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DiffusionModelLoaderKJ`
- `EmptyLatentImage`
- `EnhancedLoadDiffusionModel`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSize`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageFromBatch+`
- `Int`
- `JDCN_StringToList`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `RandomInt`
- `RunningHub Deepcleaner`
- `SetNode`
- `Text`
- `TextConcatenate_UTK`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageListToImageBatch`
- `easy indexAnything`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DF_String_Concatenate` —— 5/6 个有
- `ImageConcatenate_UTK` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `JjkText` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `solarL_SaveImagesToZip` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `SaveImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 6 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 6 | 51% |
| 采样算法 | er_sde | - | 6 | 67% |
| 调度器 | beta | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 1024 | 6 | 0% |
| 高度 | 80 | 80 - 1024 | 6 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，6 个样本
- 采样算法 最常用 er_sde，6 个样本，一致性 67%
- 调度器 最常用 beta，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，6 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，6 个样本，取值分散，一致性仅 0%
- 高发问题（10/6 个样本）：Steps较低可能导致细节不足
