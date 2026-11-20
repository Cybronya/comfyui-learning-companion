---
name: unknown_workflow_video_lora_sampler_1181
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.753
common_nodes: [BlockifyMask, BodyRatioMapperSDPoseRender, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, DrawMaskOnImage, GrowMaskWithBlur, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, Primitive integer [Crystools], SAM3_Detect, SDPoseKeypointExtractor, Seed (rgthree), SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/🔥角色替换+动作迁移+面部表情=爆款复刻  无加密节点_2109231949574402050.json, 视频生成/图生视频/🔥角色替换+动作迁移+面部表情=爆款复刻 9月15日 无加密节点_2099712198623981570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1181

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/🔥角色替换+动作迁移+面部表情=爆款复刻  无加密节点_2109231949574402050.json、视频生成/图生视频/🔥角色替换+动作迁移+面部表情=爆款复刻 9月15日 无加密节点_2099712198623981570.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `BodyRatioMapperSDPoseRender`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DrawMaskOnImage`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Primitive integer [Crystools]`
- `SAM3_Detect`
- `SDPoseKeypointExtractor`
- `Seed (rgthree)`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
