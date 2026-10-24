---
name: unknown_workflow_controlnet_video_lora_24
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.912333
common_nodes: [ImageResizeKJv2, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/单人图像说话（WanMultitalk）（魔方）_1948265018342158337.json, 视频生成/图生视频/图生视频加运镜_1951201282436571137.json, 视频生成/图生视频/数字人加运镜_1951224914336526338.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_24

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/单人图像说话（WanMultitalk）（魔方）_1948265018342158337.json、视频生成/图生视频/图生视频加运镜_1951201282436571137.json、视频生成/图生视频/数字人加运镜_1951224914336526338.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 2/3 个有
- `DownloadAndLoadWav2VecModel` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `MultiTalkModelLoader` —— 2/3 个有
- `MultiTalkWav2VecEmbeds` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `WanVideoContextOptions` —— 2/3 个有
- `AudioSeparation` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `FloatConstant` —— 1/3 个有
- `WanVideoClipVisionEncode` —— 1/3 个有
- `WanVideoSLG` —— 1/3 个有
- `WanVideoTeaCache` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
