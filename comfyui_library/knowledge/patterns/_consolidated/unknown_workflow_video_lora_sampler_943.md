---
name: unknown_workflow_video_lora_sampler_943
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.55
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioSeparation, GetNode, ImageResizeKJv2, LoadAudio, LoadImage, SetNode, VHS_VideoCombine, WanVideoAddAudioEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan_s2v图生视频_1960490609888866305.json, 视频生成/文生视频/S2V KJ版工作流Aiwood手搓版_1961072837920493569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_943

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/wan_s2v图生视频_1960490609888866305.json、视频生成/文生视频/S2V KJ版工作流Aiwood手搓版_1961072837920493569.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioSeparation`
- `GetNode`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoAddAudioEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `LoadWanVideoT5TextEncoder` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoTextEncodeCached` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
