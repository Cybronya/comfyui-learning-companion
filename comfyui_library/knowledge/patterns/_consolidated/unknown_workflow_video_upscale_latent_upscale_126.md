---
name: unknown_workflow_video_upscale_latent_upscale_126
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.922
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, CR Prompt Text, CreateVideo, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MiniMaxH3LatentUpscaleBy32T8, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PlaySound|pysssss, Qwen3ASRLoader, Qwen3ASRTranscribe, RunningHub_VoxCPM_Generate, RunningHub_VoxCPM_LoadModel, SaveAudio, SaveVideo, SetNode, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/（终版）对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2091491653193396226.json, 数字人/数字人/（终版）视频口播带货工作流_2096439571230842881.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_126

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/（终版）对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2091491653193396226.json、数字人/数字人/（终版）视频口播带货工作流_2096439571230842881.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CreateVideo`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MiniMaxH3LatentUpscaleBy32T8`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PlaySound|pysssss`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `RunningHub_VoxCPM_Generate`
- `RunningHub_VoxCPM_LoadModel`
- `SaveAudio`
- `SaveVideo`
- `SetNode`
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
- `CFGNorm` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `Int` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `TextEncodeQwenImageEdit` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAELoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
