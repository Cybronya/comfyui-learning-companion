---
name: unknown_workflow_video_lora_sampler_397
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9468
common_nodes: [VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/【遇见AI】wan2.1文生视频基础流，带加速_2061013216846770177.json, 视频生成/图生视频/2073698688299524097.json, 视频生成/图生视频/2067521044533039105.json, 视频生成/图生视频/2071441193522778114.json, 视频生成/图生视频/2062803456766861313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_397

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/【遇见AI】wan2.1文生视频基础流，带加速_2061013216846770177.json、视频生成/图生视频/2073698688299524097.json、视频生成/图生视频/2067521044533039105.json、视频生成/图生视频/2071441193522778114.json、视频生成/图生视频/2062803456766861313.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
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
- `CLIPVisionLoader` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `WanVideoClipVisionEncode` —— 4/5 个有
- `WanVideoImageToVideoEncode` —— 4/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `WanVideoEmptyEmbeds` —— 1/5 个有
- `WanVideoEncode` —— 1/5 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/5 个有
- `WanVideoUni3C_embeds` —— 1/5 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/5 个有
- `WanVideoUniAnimatePoseInput` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
