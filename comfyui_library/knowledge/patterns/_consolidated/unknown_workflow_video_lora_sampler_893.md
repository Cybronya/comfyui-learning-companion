---
name: unknown_workflow_video_lora_sampler_893
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8
common_nodes: [ApplyFaceProcessor, CR Text, FaceProcessorLoader, GetNode, ImageConcatMulti, ImpactSwitch, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PreviewImage, RH_LLMAPI_NODE, SetNode, Text Concatenate, VHS_VideoCombine, Wan22PromptSelector, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy imageScaleDownToSize, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1+Stand-In+MultiTalk 人脸一致性文生数字人_1956219463043612673.json, 视频生成/文生视频/Wan2.1+Stand-In身份一致性文生视频_1956197962999320577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_893

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.1+Stand-In+MultiTalk 人脸一致性文生数字人_1956219463043612673.json、视频生成/文生视频/Wan2.1+Stand-In身份一致性文生视频_1956197962999320577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFaceProcessor`
- `CR Text`
- `FaceProcessorLoader`
- `GetNode`
- `ImageConcatMulti`
- `ImpactSwitch`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `SetNode`
- `Text Concatenate`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy imageScaleDownToSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `AudioSeparation` —— 1/2 个有
- `DownloadAndLoadWav2VecModel` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MultiTalkModelLoader` —— 1/2 个有
- `MultiTalkWav2VecEmbeds` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
