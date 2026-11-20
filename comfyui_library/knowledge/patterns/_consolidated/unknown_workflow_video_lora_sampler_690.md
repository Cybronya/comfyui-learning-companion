---
name: unknown_workflow_video_lora_sampler_690
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.60675
common_nodes: [AILab_MiniCPM_4_V_Advanced, CLIPVisionLoader, GetNode, ImageBatchMulti, ImageResizeKJv2, ImageStitch, Int, LoadImage, SetNode, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncodeLatentBatch, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [平台全量/wan2.2 首尾帧及插帧辅助图生视频工作流_1984488129035976706.json, 平台全量/【首尾帧视频】万相Wan2.2 14B FLF2V 首尾帧及插帧辅助图生视频工作流 加速版首尾帧生_1984809663709462529.json, 平台全量/万相双图首尾帧+万相Wan2.2 14B FLF2V 首尾帧及插帧辅助图生视频工作流 加速版首尾帧生_1993964237435371522.json, 视频生成/图生视频/wan2.2首尾帧➕插帧自动生成分镜短视频_1986392312181911553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_690

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/wan2.2 首尾帧及插帧辅助图生视频工作流_1984488129035976706.json、平台全量/【首尾帧视频】万相Wan2.2 14B FLF2V 首尾帧及插帧辅助图生视频工作流 加速版首尾帧生_1984809663709462529.json、平台全量/万相双图首尾帧+万相Wan2.2 14B FLF2V 首尾帧及插帧辅助图生视频工作流 加速版首尾帧生_1993964237435371522.json、视频生成/图生视频/wan2.2首尾帧➕插帧自动生成分镜短视频_1986392312181911553.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_MiniCPM_4_V_Advanced`
- `CLIPVisionLoader`
- `GetNode`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `ImageStitch`
- `Int`
- `LoadImage`
- `SetNode`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncodeLatentBatch`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactImageBatchToImageList` —— 3/4 个有
- `WanVideoLoraSelectMulti` —— 3/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
