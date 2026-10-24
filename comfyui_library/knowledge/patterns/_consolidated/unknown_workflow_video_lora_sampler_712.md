---
name: unknown_workflow_video_lora_sampler_712
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.905
common_nodes: [AudioCrop, AudioSeparation, HuMoEmbeds, ImageBatchMulti, ImageFromBatch, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoCombineEmbeds, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, Wav2VecModelLoader, WhisperModelLoader, easy imageRemBg]
problems: []
missing: []
members: [图片生成/文生图/ai MV应用版（30S福音）_2000822453771399170.json, 视频生成/图生视频/👽Humo数字人音乐MV嗨歌版👽_1968957972288323586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_712

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/ai MV应用版（30S福音）_2000822453771399170.json、视频生成/图生视频/👽Humo数字人音乐MV嗨歌版👽_1968957972288323586.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `HuMoEmbeds`
- `ImageBatchMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoCombineEmbeds`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `Wav2VecModelLoader`
- `WhisperModelLoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `AudioCropProcessUTK` —— 1/2 个有
- `CM_FloatUnaryOperation` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `JWIntegerToString` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
