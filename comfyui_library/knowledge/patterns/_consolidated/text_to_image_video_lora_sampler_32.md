---
name: text_to_image_video_lora_sampler_32
type: Text To Image
frequency: 16
level: weak
coverage: 0.80375
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, GetImageRangeFromBatch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VAEDecode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/对口型+情感口播++数字人+InfiniTetalk+超自然数字人对口型_2095721057431932929.json, 视频生成/图生视频/对口型情感口播数字人InfiniTetalk超自然数字人对口型工作流，数字人图生视频方案_2108338478210699265.json, 视频生成/图生视频/对口型情感口播数字人InfiniTetalk超自然数字人对口型工作流，数字人图生视频方案_2108440403677634562.json, 视频生成/图生视频/数字人口播工作流，文生视频数字人图生视频处理方案_2110538752048328706.json, 视频生成/图生视频/数字人口播视频制作｜输入文案生成真人讲解片_2106644228221784066.json, 视频生成/图生视频/数字人对口型情感口播InfiniTetalk超自然数字人对口型_2108700227837448193.json, 视频生成/图生视频/数字人对口型情感口播InfiniTetalk超自然数字人对口型工作流，数字人图生视频方案_2108341641831608321.json, 视频生成/图生视频/超自然数字人对口型InfiniTetalk｜口播视频运镜出片_2108422368073961473.json, 视频生成/图生视频/超自然数字人对口型｜InfiniTetalk 情感口播 数字人表情自然生动_2105480911436472322.json, 视频生成/图生视频/音频驱动开口说话｜InfiniTetalk数字人电商带货_2096557364114714626.json, 视频生成/文生视频/口播视频量产神器｜数字人文生图生视频全能_2096622690554699778.json, 视频生成/文生视频/数字人口播工作流，文生视频数字人图生视频处理方案_2106837103236702210.json, 视频生成/文生视频/数字人口播视频制作｜真人形象快速生成工作流_2096308137073664001.json, 视频生成/文生视频/数字人口播视频制作｜输入文案生成真人讲解片_2106644228221784066.json, 视频生成/文生视频/数字人口播视频生成｜文生视频图生视频一键直出_2095803345842827265.json, 视频生成/文生视频/数字人口播视频生成｜音频驱动口型同步工作流_2095568073246986242.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_32

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/对口型+情感口播++数字人+InfiniTetalk+超自然数字人对口型_2095721057431932929.json、视频生成/图生视频/对口型情感口播数字人InfiniTetalk超自然数字人对口型工作流，数字人图生视频方案_2108338478210699265.json、视频生成/图生视频/对口型情感口播数字人InfiniTetalk超自然数字人对口型工作流，数字人图生视频方案_2108440403677634562.json、视频生成/图生视频/数字人口播工作流，文生视频数字人图生视频处理方案_2110538752048328706.json、视频生成/图生视频/数字人口播视频制作｜输入文案生成真人讲解片_2106644228221784066.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 16 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `GetImageRangeFromBatch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VAEDecode`
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
- `CLIPLoader` —— 15/16 个有
- `JjkText` —— 15/16 个有
- `LoraLoaderModelOnly` —— 15/16 个有
- `UNETLoader` —— 15/16 个有
- `VAELoader` —— 15/16 个有
- `solarL_SaveImagesToZip` —— 15/16 个有
- `孤海注释` —— 14/16 个有
- `GetNode` —— 12/16 个有
- `PlaySound|pysssss` —— 12/16 个有
- `SetNode` —— 12/16 个有
- `PreviewAudio` —— 9/16 个有
- `WanVideoTorchCompileSettings` —— 9/16 个有
- `easy int` —— 9/16 个有
- `IndexTTS2Run` —— 8/16 个有
- `PrimitiveStringMultiline` —— 8/16 个有
- `SaveImage` —— 7/16 个有
- `Anything Everywhere` —— 5/16 个有
- `easy showAnything` —— 5/16 个有
- `LogicUtil_SleepNodeAny` —— 4/16 个有
- `CheckpointLoaderSimple` —— 1/16 个有
- `ColorCorrectOfUtils` —— 1/16 个有
- `ImageCASharpening+` —— 1/16 个有
- `ImageScale` —— 1/16 个有
- `ImageUpscaleWithModel` —— 1/16 个有
- `PreviewImage` —— 1/16 个有
- `UpscaleModelLoader` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 512 | 16 | 2% |
| 高度 | 80 | 80 - 512 | 16 | 2% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 16 | 80% |
| 采样算法 | er_sde | - | 16 | 94% |
| 调度器 | beta | - | 16 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 512，16 个样本，取值分散，一致性仅 2%
- 高度 中位数 80，观测区间 80 - 512，16 个样本，取值分散，一致性仅 2%
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，16 个样本，取值集中（一致性 80%）
- 采样算法 最常用 er_sde，16 个样本，一致性 94%
- 调度器 最常用 beta，16 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
