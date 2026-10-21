---
name: unknown_workflow_video_lora_sampler_602
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.906667
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, ColorMatch, ImageResizeKJv2, ImageScaleBy, Int, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, Pick From Batch (mtb), RHHiddenNodes, SaveImage, SimpleMath+, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1991891221526409218.json, 视频生成/图生视频/1994964520529539073.json, 视频生成/图生视频/1992045257871216642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_602

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1991891221526409218.json、视频生成/图生视频/1994964520529539073.json、视频生成/图生视频/1992045257871216642.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `ColorMatch`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `Int`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `Pick From Batch (mtb)`
- `RHHiddenNodes`
- `SaveImage`
- `SimpleMath+`
- `ToInt`
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SaveAudio` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
