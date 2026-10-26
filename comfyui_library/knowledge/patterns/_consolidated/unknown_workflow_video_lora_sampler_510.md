---
name: unknown_workflow_video_lora_sampler_510
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9536
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【遇见AI】wan2.1 Uni3c视频运镜模型_2071441193522778114.json, 视频生成/图生视频/【遇见AI】wan2.1 UniAnimate视频转绘 动作参考_2062803456766861313.json, 视频生成/图生视频/【遇见AI】wan2.1图生视频不同加速lora对比_2062116414055608321.json, 视频生成/图生视频/【遇见AI】wan2.1图生视频基础流，带加速_2061019045620699138.json, 视频生成/图生视频/【遇见AI】wan2.1首尾帧基础流_2062101371284975617.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_510

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/【遇见AI】wan2.1 Uni3c视频运镜模型_2071441193522778114.json、视频生成/图生视频/【遇见AI】wan2.1 UniAnimate视频转绘 动作参考_2062803456766861313.json、视频生成/图生视频/【遇见AI】wan2.1图生视频不同加速lora对比_2062116414055608321.json、视频生成/图生视频/【遇见AI】wan2.1图生视频基础流，带加速_2061019045620699138.json、视频生成/图生视频/【遇见AI】wan2.1首尾帧基础流_2062101371284975617.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 2/5 个有
- `WanVideoVRAMManagement` —— 2/5 个有
- `PreviewImage` —— 1/5 个有
- `WanVideoEncode` —— 1/5 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/5 个有
- `WanVideoUni3C_embeds` —— 1/5 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/5 个有
- `WanVideoUniAnimatePoseInput` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
