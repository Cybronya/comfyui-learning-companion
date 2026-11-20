---
name: unknown_workflow_video_lora_sampler_536
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.949667
common_nodes: [CLIPVisionLoader, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【遇见AI】wan2.1 MAGREF 多图参考视频_2073698688299524097.json, 视频生成/图生视频/【遇见AI】wan2.1 Skyreels V2 图生视频，支持超过81帧_2067521044533039105.json, 视频生成/图生视频/【遇见AI】wan2.1 Uni3c视频运镜模型_2071441193522778114.json, 视频生成/图生视频/【遇见AI】wan2.1 UniAnimate视频转绘 动作参考_2062803456766861313.json, 视频生成/图生视频/【遇见AI】wan2.1图生视频不同加速lora对比_2062116414055608321.json, 视频生成/图生视频/【遇见AI】wan2.1图生视频基础流，带加速_2061019045620699138.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_536

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/【遇见AI】wan2.1 MAGREF 多图参考视频_2073698688299524097.json、视频生成/图生视频/【遇见AI】wan2.1 Skyreels V2 图生视频，支持超过81帧_2067521044533039105.json、视频生成/图生视频/【遇见AI】wan2.1 Uni3c视频运镜模型_2071441193522778114.json、视频生成/图生视频/【遇见AI】wan2.1 UniAnimate视频转绘 动作参考_2062803456766861313.json、视频生成/图生视频/【遇见AI】wan2.1图生视频不同加速lora对比_2062116414055608321.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
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
- `ImageResizeKJv2` —— 5/6 个有
- `PreviewImage` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `WanVideoVRAMManagement` —— 2/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `WanVideoEncode` —— 1/6 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/6 个有
- `WanVideoUni3C_embeds` —— 1/6 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/6 个有
- `WanVideoUniAnimatePoseInput` —— 1/6 个有
- `easy imageRemBg` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
