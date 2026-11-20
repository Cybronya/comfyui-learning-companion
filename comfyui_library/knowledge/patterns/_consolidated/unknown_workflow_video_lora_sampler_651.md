---
name: unknown_workflow_video_lora_sampler_651
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.928
common_nodes: [Audio Duration (mtb), AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, FloatConstant, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/MAGREF+MultiTalk_1942507580919058434.json, 视频生成/图生视频/Wan2.1数字人_1951180458820313090.json, 视频生成/图生视频/数字人加运镜_1951224914336526338.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_651

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/MAGREF+MultiTalk_1942507580919058434.json、视频生成/图生视频/Wan2.1数字人_1951180458820313090.json、视频生成/图生视频/数字人加运镜_1951224914336526338.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `FloatConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 2/3 个有
- `WanVideoContextOptions` —— 2/3 个有
- `WanVideoExperimentalArgs` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `Bookmark (rgthree)` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `RMBG` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `WanVideoEncode` —— 1/3 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/3 个有
- `WanVideoUni3C_embeds` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
