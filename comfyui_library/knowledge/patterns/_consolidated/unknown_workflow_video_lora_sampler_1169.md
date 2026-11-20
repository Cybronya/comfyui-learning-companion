---
name: unknown_workflow_video_lora_sampler_1169
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.701
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PrimitiveStringMultiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/最新数字人InfiniteTalk -高质量数字人（支持超长时间）_1958071063076884481.json, 视频生成/文生视频/数字人口播_2106320471296925698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1169

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/最新数字人InfiniteTalk -高质量数字人（支持超长时间）_1958071063076884481.json、视频生成/文生视频/数字人口播_2106320471296925698.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PrimitiveStringMultiline`
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
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `IndexTTS2Run` —— 1/2 个有
- `JWIntegerToString` —— 1/2 个有
- `MaxNode` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `SaveAudio` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy imageScaleDownToSize` —— 1/2 个有
- `easy imageSize` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
