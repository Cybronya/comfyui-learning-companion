---
name: text_to_image_video_lora_sampler_189
type: Text To Image
frequency: 3
level: strong
coverage: 0.529667
common_nodes: [CLIPLoader, CLIPTextEncode, DWPreprocessor, EmptyLatentImage, FloatConstant, GetImageRangeFromBatch, GetNode, INTConstant, ImageBatchMulti, ImageColorMatch+, ImageFromBatch, ImageResizeKJv2, JjkText, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MaskToImage, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, Power Lora Loader (rgthree), PreviewImage, SetNode, TorchCompileModelWanVideoV2, TrimVideoLatent, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy forLoopEnd, easy forLoopStart, easy showAnything, solarL_SaveImagesToZip, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan 2.1 VACE-SVI CN V2V长视频跳舞专用 图生视频视频生视频_2088683651528744962.json, 视频生成/图生视频/Wan 2.1 VACE-SVI CN V2V长视频跳舞专用 图生视频视频生视频_2089323773471322113.json, 视频生成/图生视频/Wan 2.1 VACE-SVI CN V2V长视频跳舞专用 图生视频视频生视频_2091764185435824130.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_189

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan 2.1 VACE-SVI CN V2V长视频跳舞专用 图生视频视频生视频_2088683651528744962.json、视频生成/图生视频/Wan 2.1 VACE-SVI CN V2V长视频跳舞专用 图生视频视频生视频_2089323773471322113.json、视频生成/图生视频/Wan 2.1 VACE-SVI CN V2V长视频跳舞专用 图生视频视频生视频_2091764185435824130.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DWPreprocessor`
- `EmptyLatentImage`
- `FloatConstant`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageColorMatch+`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Power Lora Loader (rgthree)`
- `PreviewImage`
- `SetNode`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（9/3 个样本）：Steps较低可能导致细节不足
