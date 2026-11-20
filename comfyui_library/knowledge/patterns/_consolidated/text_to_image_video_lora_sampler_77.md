---
name: text_to_image_video_lora_sampler_77
type: Text To Image
frequency: 11
level: strong
coverage: 0.844
common_nodes: [AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/InfiniTetalk配口型｜Wan2.1图像数字人KJ节点版_2094339522954874882.json, 视频生成/图生视频/InfiniTetalk音频驱动数字人｜电商带货图生视频_2096311256083951618.json, 视频生成/图生视频/InfiniteTalk超自然数字人对口型情感口播工作流，图生视频数字人工具_2106150910039781377.json, 视频生成/图生视频/InfiniteTalk超自然数字人对口型情感口播工作流，图生视频数字人工具_2106480253395881985.json, 视频生成/图生视频/InfiniteTalk超自然数字人对口型情感口播工作流，图生视频数字人方案_2106502944366616577.json, 视频生成/图生视频/Wan2.1 InfiniTetalk图像数字人配口型KJ节点人物特效_2088176935515021313.json, 视频生成/图生视频/对口型情感口播数字人InfiniTetalk超自然数字人对口型工作流，数字人图生视频方案_2108338478210699265.json, 视频生成/图生视频/对口型情感口播数字人InfiniTetalk超自然数字人对口型工作流，数字人图生视频方案_2108440403677634562.json, 视频生成/图生视频/数字人口播工作流，文生视频数字人图生视频处理方案_2110538752048328706.json, 视频生成/图生视频/音频驱动开口说话｜InfiniTetalk数字人电商带货_2096557364114714626.json, 视频生成/文生视频/口播视频量产神器｜数字人文生图生视频全能_2096622690554699778.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_77

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/InfiniTetalk配口型｜Wan2.1图像数字人KJ节点版_2094339522954874882.json、视频生成/图生视频/InfiniTetalk音频驱动数字人｜电商带货图生视频_2096311256083951618.json、视频生成/图生视频/InfiniteTalk超自然数字人对口型情感口播工作流，图生视频数字人工具_2106150910039781377.json、视频生成/图生视频/InfiniteTalk超自然数字人对口型情感口播工作流，图生视频数字人工具_2106480253395881985.json、视频生成/图生视频/InfiniteTalk超自然数字人对口型情感口播工作流，图生视频数字人方案_2106502944366616577.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 10/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `Audio Duration (mtb)` —— 9/11 个有
- `GetImageRangeFromBatch` —— 9/11 个有
- `MathExpression|pysssss` —— 9/11 个有
- `PlaySound|pysssss` —— 9/11 个有
- `SaveImage` —— 6/11 个有
- `WanVideoTorchCompileSettings` —— 6/11 个有
- `PreviewAudio` —— 4/11 个有
- `easy int` —— 4/11 个有
- `Anything Everywhere` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `ColorCorrectOfUtils` —— 2/11 个有
- `INTConstant` —— 2/11 个有
- `ImageCASharpening+` —— 2/11 个有
- `IndexTTS2Run` —— 2/11 个有
- `PreviewAny` —— 2/11 个有
- `PrimitiveStringMultiline` —— 2/11 个有
- `GetImageSizeAndCount` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `LogicUtil_SleepNodeAny` —— 1/11 个有
- `PixaromaResolution` —— 1/11 个有
- `PreviewImage` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
