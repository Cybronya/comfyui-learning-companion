---
name: unknown_workflow_video_lora_sampler_460
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.907
common_nodes: [CogVideoEnhanceAVideo, CreateCFGScheduleFloatList, DF_Integer, ImageStitch, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, PrimitiveBoolean, RH_Captioner, RH_Translator, SimpleMath+, Textbox, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy ifElse, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/wan2.2-14B 首尾帧最新_1952194962240819201.json, 图片生成/文生图/qwen_image+wan2.2——飞翔荷兰人_1971507524669259778.json, 视频生成/图生视频/4min-0.05-图生视频wan2.2视频循环首尾帧_1965238550650306562.json, 视频生成/图生视频/wan2.2图生视频，效果好，速度快_1964263324487700481.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_460

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/wan2.2-14B 首尾帧最新_1952194962240819201.json、图片生成/文生图/qwen_image+wan2.2——飞翔荷兰人_1971507524669259778.json、视频生成/图生视频/4min-0.05-图生视频wan2.2视频循环首尾帧_1965238550650306562.json、视频生成/图生视频/wan2.2图生视频，效果好，速度快_1964263324487700481.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CogVideoEnhanceAVideo`
- `CreateCFGScheduleFloatList`
- `DF_Integer`
- `ImageStitch`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveBoolean`
- `RH_Captioner`
- `RH_Translator`
- `SimpleMath+`
- `Textbox`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/4 个有
- `CLIPTextEncode` —— 2/4 个有
- `CLIPVisionEncode` —— 2/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `CR Text Replace` —— 2/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ModelSamplingSD3` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `TextBox` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `VAEDecode` —— 2/4 个有
- `VAELoader` —— 2/4 个有
- `WanImageToVideo` —— 2/4 个有
- `AILab_MiniCPM_4_V` —— 1/4 个有
- `ColorMatchToReference` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `KSampler` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 调度器 最常用 simple，2 个样本，一致性 50%
