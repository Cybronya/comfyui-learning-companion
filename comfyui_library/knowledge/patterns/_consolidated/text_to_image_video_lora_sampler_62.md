---
name: text_to_image_video_lora_sampler_62
type: Text To Image
frequency: 12
level: strong
coverage: 0.8795
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, GetImageRangeFromBatch, GetNode, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PlaySound|pysssss, SetNode, UNETLoader, VAEDecode, VAELoader, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/终版视频口播带货工作流｜数字人快速生成制作_2096735921801617409.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播人物特效_2108413955092865026.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播人物特效图生视频_2090439293465612289.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播嘴型不违和_2111344640648634370.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播自然逼真不出戏_2106217891178831874.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播视频一步到位_2111104461941858305.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播视频生成_2097816767069507586.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播视频运镜_2097979213222604801.json, 视频生成/图生视频/InfiniTetalk超自然数字人｜对口型情感口播生成_2094908442413723649.json, 视频生成/图生视频/InfiniteTalk超自然数字人对口型情感口播工作流，图生视频数字人工具_2106150910039781377.json, 视频生成/图生视频/InfiniteTalk超自然数字人对口型情感口播工作流，图生视频数字人工具_2106480253395881985.json, 视频生成/图生视频/InfiniteTalk超自然数字人对口型情感口播工作流，图生视频数字人方案_2106502944366616577.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_62

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/终版视频口播带货工作流｜数字人快速生成制作_2096735921801617409.json、视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播人物特效_2108413955092865026.json、视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播人物特效图生视频_2090439293465612289.json、视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播嘴型不违和_2111344640648634370.json、视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播自然逼真不出戏_2106217891178831874.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 12 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `GetNode`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PlaySound|pysssss`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 11/12 个有
- `SaveImage` —— 4/12 个有
- `CFGNorm` —— 1/12 个有
- `CR Prompt Text` —— 1/12 个有
- `CR Text` —— 1/12 个有
- `CreateVideo` —— 1/12 个有
- `EmptySD3LatentImage` —— 1/12 个有
- `Int` —— 1/12 个有
- `LTXVConcatAVLatent` —— 1/12 个有
- `LTXVSeparateAVLatent` —— 1/12 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 1/12 个有
- `ModelSamplingAuraFlow` —— 1/12 个有
- `Qwen3ASRLoader` —— 1/12 个有
- `Qwen3ASRTranscribe` —— 1/12 个有
- `RunningHub_VoxCPM_Generate` —— 1/12 个有
- `RunningHub_VoxCPM_LoadModel` —— 1/12 个有
- `SaveAudio` —— 1/12 个有
- `SaveVideo` —— 1/12 个有
- `TextEncodeQwenImageEdit` —— 1/12 个有
- `TextEncodeQwenImageEditPlus` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
