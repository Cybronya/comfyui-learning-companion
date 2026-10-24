---
name: text_to_image_video_lora_sampler_15
type: Text To Image
frequency: 29
level: weak
coverage: 0.868621
common_nodes: [AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, KSampler, LoadAudio, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Infinitetalk单人数字人｜无限时长自循环口播_2089424078561177602.json, 视频生成/图生视频/I2V-InfiniteTalk数字人-GGUF（加速版）_1982695660992503809.json, 视频生成/图生视频/InfiniTetalk情感口播对口型，数字人图生视频制作_2110880440189014018.json, 视频生成/图生视频/InfiniTetalk情感口播数字人｜超自然对口型口播必备_2111111924355264514.json, 视频生成/图生视频/InfiniTetalk数字人对口型｜情感口播超自然口型同步_2108430225666301953.json, 视频生成/图生视频/InfiniTetalk超自然对口型，情感口播数字人制作_2110858558400188418.json, 视频生成/图生视频/InfiniTetalk超自然对口型，情感口播数字人制作_2111254679618416641.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型 情感口播人物特效_2094193709834395649.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型 情感口播视频生成_2098854674370752513.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型 情感口播视频生成_2099597317438525442.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型 情感口播视频生成_2100680027225550850.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型 情感口播视频生成_2104705468173213698.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型 情感口播视频生成_2104711738179538945.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型，情感口播数字人制作_2110525729363550210.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型，情感口播数字人制作_2111275845468901377.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播人物特效_2108413955092865026.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播人物特效图生视频_2090439293465612289.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播嘴型不违和_2111344640648634370.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播自然逼真不出戏_2106217891178831874.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播视频一步到位_2111104461941858305.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播视频生成_2097816767069507586.json, 视频生成/图生视频/InfiniTetalk超自然数字人对口型｜情感口播视频运镜_2097979213222604801.json, 视频生成/图生视频/InfiniTetalk超自然数字人｜对口型情感口播生成_2094908442413723649.json, 视频生成/图生视频/InfiniTetalk配口型｜Wan2.1图像数字人KJ节点版_2094339522954874882.json, 视频生成/图生视频/InfiniteTalk超自然数字人对口型情感口播工作流，图生视频数字人工具_2106150910039781377.json, 视频生成/图生视频/InfiniteTalk超自然数字人对口型情感口播工作流，图生视频数字人工具_2106480253395881985.json, 视频生成/图生视频/InfiniteTalk超自然数字人对口型情感口播工作流，图生视频数字人方案_2106502944366616577.json, 视频生成/图生视频/Wan2.1 InfiniTetalk图像数字人配口型KJ节点人物特效_2088176935515021313.json, 视频生成/文生视频/视频生成_2108532387113160705.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（数字人/数字人/Infinitetalk单人数字人｜无限时长自循环口播_2089424078561177602.json、视频生成/图生视频/I2V-InfiniteTalk数字人-GGUF（加速版）_1982695660992503809.json、视频生成/图生视频/InfiniTetalk情感口播对口型，数字人图生视频制作_2110880440189014018.json、视频生成/图生视频/InfiniTetalk情感口播数字人｜超自然对口型口播必备_2111111924355264514.json、视频生成/图生视频/InfiniTetalk数字人对口型｜情感口播超自然口型同步_2108430225666301953.json…）

- **类型**：Text To Image
- **样本数**：29
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 29 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `KSampler`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
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

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 28/29 个有
- `GetNode` —— 27/29 个有
- `JjkText` —— 27/29 个有
- `LoraLoaderModelOnly` —— 27/29 个有
- `SetNode` —— 27/29 个有
- `solarL_SaveImagesToZip` —— 27/29 个有
- `孤海注释` —— 26/29 个有
- `Audio Duration (mtb)` —— 25/29 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 25/29 个有
- `PlaySound|pysssss` —— 25/29 个有
- `GetImageRangeFromBatch` —— 24/29 个有
- `MathExpression|pysssss` —— 24/29 个有
- `SaveImage` —— 15/29 个有
- `WanVideoTorchCompileSettings` —— 5/29 个有
- `ImageResizeKJv2` —— 4/29 个有
- `SimpleMath+` —— 3/29 个有
- `INTConstant` —— 2/29 个有
- `Int` —— 2/29 个有
- `PreviewAny` —— 2/29 个有
- `PreviewImage` —— 2/29 个有
- `RH_GetAudioDuration` —— 2/29 个有
- `ToInt` —— 2/29 个有
- `easy showAnything` —— 2/29 个有
- `EmptyImage` —— 1/29 个有
- `GetImageSizeAndCount` —— 1/29 个有
- `PixaromaResolution` —— 1/29 个有
- `Power Lora Loader (rgthree)` —— 1/29 个有
- `PrimitiveStringMultiline` —— 1/29 个有
- `VAEEncode` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1280 | 29 | 0% |
| 高度 | 80 | 80 - 1024 | 29 | 0% |
| 采样步数 | 4 | 4 - 9 | 29 | 73% |
| Prompt 约束强度(CFG) | 4.5 | 0 - 4.5 | 29 | 76% |
| 采样算法 | er_sde | - | 29 | 93% |
| 调度器 | beta | - | 29 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1280，29 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，29 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 9，29 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 0 - 4.5，29 个样本
- 采样算法 最常用 er_sde，29 个样本，一致性 93%
- 调度器 最常用 beta，29 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（30/29 个样本）：Steps较低可能导致细节不足
