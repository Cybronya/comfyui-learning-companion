---
name: unknown_workflow_video_lora_sampler_845
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.627
common_nodes: [Any Switch (rgthree), AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, Fast Groups Bypasser (rgthree), Float, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, PrimitiveStringMultiline, Qwen3_VQA, SaveAudio, SetNode, SoulXPodcastGenerate, SoulXPodcastInputParser, SoulXPodcastLoader, StringConcatenate, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1985626915035914241.json, 音频生成/音频生成/你的数字人能说河南话，稳定的输出_1987756118204198914.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_845

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1985626915035914241.json、音频生成/音频生成/你的数字人能说河南话，稳定的输出_1987756118204198914.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `PrimitiveStringMultiline`
- `Qwen3_VQA`
- `SaveAudio`
- `SetNode`
- `SoulXPodcastGenerate`
- `SoulXPodcastInputParser`
- `SoulXPodcastLoader`
- `StringConcatenate`
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
- `easy int`
- `easy showAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
