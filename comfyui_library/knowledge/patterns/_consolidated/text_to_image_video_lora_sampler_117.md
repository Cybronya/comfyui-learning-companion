---
name: text_to_image_video_lora_sampler_117
type: Text To Image
frequency: 6
level: strong
coverage: 0.693333
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, DownloadAndLoadWav2VecModel, EmptyLatentImage, ImageResizeKJv2, KSampler, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewImage, SimpleMath+, VAEDecode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AI代码侠土豆-I2V数字人一条龙合集_1999484627213484033.json, 数字人/数字人/AI代码侠土豆-I2V数字人一条龙合集王改革_2000808693069475841.json, 数字人/数字人/I2V-InfiniteTalk数字人单人_2002788498899890178.json, 数字人/数字人/I2V数字人_2002786080296452098.json, 视频生成/图生视频/-I2V数字人一条龙合集，动作，表情，肢体语言，全部到位！！！_2045983790081773570.json, 视频生成/图生视频/I2V-InfiniteTalk数字人-GGUF（加速版）_1982695660992503809.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_117

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/AI代码侠土豆-I2V数字人一条龙合集_1999484627213484033.json、数字人/数字人/AI代码侠土豆-I2V数字人一条龙合集王改革_2000808693069475841.json、数字人/数字人/I2V-InfiniteTalk数字人单人_2002788498899890178.json、数字人/数字人/I2V数字人_2002786080296452098.json、视频生成/图生视频/-I2V数字人一条龙合集，动作，表情，肢体语言，全部到位！！！_2045983790081773570.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 6 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewImage`
- `SimpleMath+`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `LayerUtility: PurgeVRAM` —— 4/6 个有
- `PreviewAudio` —— 4/6 个有
- `QZ_ResolutionPreset` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `Text Multiline` —— 4/6 个有
- `UNETLoader_Any` —— 4/6 个有
- `VAELoader_Any` —— 4/6 个有
- `easy downloadIndexTTSAndLoadModel` —— 4/6 个有
- `easy indexTTSGenerateSimple` —— 4/6 个有
- `GetNode` —— 2/6 个有
- `Power Lora Loader (rgthree)` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `UNETLoader` —— 2/6 个有
- `VAELoader` —— 2/6 个有
- `Int` —— 1/6 个有
- `SaveAudio` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1280 | 6 | 53% |
| 高度 | 512 | 512 - 720 | 6 | 83% |
| 采样步数 | 10 | 8 - 10 | 6 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1280，6 个样本
- 高度 中位数 512，观测区间 512 - 720，6 个样本，取值集中（一致性 83%）
- 采样步数 中位数 10，观测区间 8 - 10，6 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
