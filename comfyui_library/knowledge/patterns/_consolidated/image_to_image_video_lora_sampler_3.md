---
name: image_to_image_video_lora_sampler_3
type: Image To Image
frequency: 9
level: moderate
coverage: 0.749111
common_nodes: [Any To Any, CLIPLoader, CR Overlay Text, CR Text Replace, ConditioningZeroOut, GetTextFromJson, ImageFromBatch, ImageScaleToTotalPixels, JWInteger, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoadJsonFromText, LoraLoaderModelOnly, Qwen3_VQA, Text Concatenate, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy imageListToImageBatch, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [Any To Any, CR Overlay Text, CR Text Replace, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, SDVM Image List Repeat, Text Concatenate, Text Multiline, easy imageListToImageBatch, easy promptLine]
members: [图片生成/文生图/(三宫格+三连视频)NextScene V2+Smooth自动多帧首尾帧V6_1982852158058049537.json, 图片生成/文生图/1982858526529847297.json, 图片生成/文生图/1983524926810464257.json, 视频生成/图生视频/1982852158058049537.json, 视频生成/图生视频/1986012853360631810.json, 视频生成/图生视频/1982841681064144898.json, 视频生成/图生视频/1986789347150262274.json, 视频生成/文生视频/(三宫格图片+长视频)NextScene V2+Smooth多镜头V2_1982879856159535105.json, 视频生成/文生视频/(三宫格竖版视频+图片-F2P)NextScene V2+Smooth多镜头V4_1982866140634447874.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/(三宫格+三连视频)NextScene V2+Smooth自动多帧首尾帧V6_1982852158058049537.json、图片生成/文生图/1982858526529847297.json、图片生成/文生图/1983524926810464257.json、视频生成/图生视频/1982852158058049537.json、视频生成/图生视频/1986012853360631810.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 9 个 workflow 都包含：
- `Any To Any`
- `CLIPLoader`
- `CR Overlay Text`
- `CR Text Replace`
- `ConditioningZeroOut`
- `GetTextFromJson`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `JWInteger`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadJsonFromText`
- `LoraLoaderModelOnly`
- `Qwen3_VQA`
- `Text Concatenate`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy imageListToImageBatch`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcatFromBatch` —— 8/9 个有
- `ImageListToImageBatch` —— 8/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `SDVM Image List Repeat` —— 8/9 个有
- `SaveImage` —— 8/9 个有
- `CLIPTextEncode` —— 7/9 个有
- `KSamplerAdvanced` —— 7/9 个有
- `ModelSamplingSD3` —— 7/9 个有
- `ImageConcatMulti` —— 6/9 个有
- `RunningHub Deepcleaner` —— 6/9 个有
- `> Text Replace` —— 4/9 个有
- `CLIPVisionEncode` —— 4/9 个有
- `CLIPVisionLoader` —— 4/9 个有
- `CR Prompt Text` —— 4/9 个有
- `ImageBatchToList` —— 4/9 个有
- `ImageListToBatch+` —— 4/9 个有
- `ImageResizeKJv2` —— 4/9 个有
- `PDIMAGE_LongerSize` —— 4/9 个有
- `Seed (rgthree)` —— 4/9 个有
- `WanImageToVideo` —— 4/9 个有
- `easy cleanGpuUsed` —— 4/9 个有
- `ImageConcanate` —— 3/9 个有
- `ImageScaleBy` —— 3/9 个有
- `MathExpression|pysssss` —— 3/9 个有
- `PathchSageAttentionKJ` —— 3/9 个有
- `Pick From Batch (mtb)` —— 3/9 个有
- `WanFirstMiddleLastFrameToVideo` —— 3/9 个有
- `wanBlockSwap` —— 3/9 个有
- `Float` —— 2/9 个有
- `ImageFromBatch+` —— 2/9 个有
- `AILab_MiniCPM_4_V` —— 1/9 个有
- `Anything Everywhere` —— 1/9 个有
- `AudioToFPS` —— 1/9 个有
- `CM_FloatToInt` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `HunyuanVideoFoley` —— 1/9 个有
- `IndexTTS2Run` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `ListCounter //Inspire` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `PreviewAny` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `QwenVisionNode` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `SoundFlow_Mixer` —— 1/9 个有
- `easy batchAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 78% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 9 | 55% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler_ancestral | - | 9 | 44% |
| 重绘幅度 | simple | - | 9 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 78%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，9 个样本
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，9 个样本，一致性 44%
- 重绘幅度 最常用 simple，9 个样本，一致性 78%
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Any To Any、CR Overlay Text、CR Text Replace、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM
