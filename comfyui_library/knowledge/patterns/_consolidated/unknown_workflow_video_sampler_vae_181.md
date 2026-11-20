---
name: unknown_workflow_video_sampler_vae_181
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.764
common_nodes: [Anything Everywhere, Anything Everywhere3, Audio Duration (mtb), AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, Seed Everywhere, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader, easy imageSize]
problems: []
missing: []
members: [数字人/数字人/数字人(单人)-Infinitetalk_1970726121132204033.json, 数字人/数字人/电商带货数字人对口型_1997359205885612034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_181

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/数字人(单人)-Infinitetalk_1970726121132204033.json、数字人/数字人/电商带货数字人对口型_1997359205885612034.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `Audio Duration (mtb)`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `Seed Everywhere`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadWanVideoT5TextEncoder` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `SparkTTSRun` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoLoraSelectMulti` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoTextEncodeCached` —— 1/2 个有
- `easy anythingIndexSwitch` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
