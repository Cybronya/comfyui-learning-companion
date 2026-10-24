---
name: image_to_image_video_lora_sampler_6
type: Image To Image
frequency: 4
level: strong
coverage: 0.789
common_nodes: [> Text Replace, Any To Any, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Overlay Text, CR Prompt Text, CR Text Replace, ConditioningZeroOut, GetTextFromJson, ImageBatchToList, ImageFromBatch, ImageListToBatch+, ImageResizeKJv2, ImageScaleToTotalPixels, JWInteger, KSampler, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoadJsonFromText, LoraLoaderModelOnly, ModelSamplingSD3, PDIMAGE_LongerSize, Qwen3_VQA, Seed (rgthree), Text Concatenate, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed, easy imageListToImageBatch, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/(贞贞版-三宫格竖版视频+图片)NextScene V2+Smooth多镜头V3_1986012853360631810.json, 视频生成/图生视频/三宫格视频 _ 自动配音 _ 自动BGM_1986789347150262274.json, 视频生成/文生视频/(三宫格图片+长视频)NextScene V2+Smooth多镜头V2_1982879856159535105.json, 视频生成/文生视频/(三宫格竖版视频+图片-F2P)NextScene V2+Smooth多镜头V4_1982866140634447874.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_6

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/(贞贞版-三宫格竖版视频+图片)NextScene V2+Smooth多镜头V3_1986012853360631810.json、视频生成/图生视频/三宫格视频 _ 自动配音 _ 自动BGM_1986789347150262274.json、视频生成/文生视频/(三宫格图片+长视频)NextScene V2+Smooth多镜头V2_1982879856159535105.json、视频生成/文生视频/(三宫格竖版视频+图片-F2P)NextScene V2+Smooth多镜头V4_1982866140634447874.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `> Text Replace`
- `Any To Any`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Overlay Text`
- `CR Prompt Text`
- `CR Text Replace`
- `ConditioningZeroOut`
- `GetTextFromJson`
- `ImageBatchToList`
- `ImageFromBatch`
- `ImageListToBatch+`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `JWInteger`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadJsonFromText`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PDIMAGE_LongerSize`
- `Qwen3_VQA`
- `Seed (rgthree)`
- `Text Concatenate`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `easy imageListToImageBatch`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcatFromBatch` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `ImageListToImageBatch` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `Pick From Batch (mtb)` —— 3/4 个有
- `RunningHub Deepcleaner` —— 3/4 个有
- `SDVM Image List Repeat` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `Float` —— 2/4 个有
- `AILab_MiniCPM_4_V` —— 1/4 个有
- `AudioToFPS` —— 1/4 个有
- `CM_FloatToInt` —— 1/4 个有
- `HunyuanVideoFoley` —— 1/4 个有
- `IndexTTS2Run` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `ListCounter //Inspire` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SoundFlow_Mixer` —— 1/4 个有
- `easy batchAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler_ancestral | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
