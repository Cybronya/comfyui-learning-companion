---
name: unknown_workflow_video_lora_sampler_462
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.912
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, SplineEditor, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wanvideo_WanMove_I2V_example_1998599416028258305.json, 视频生成/图生视频/【遇见AI】wan2.1 AIT轨迹控制图生视频_2071858962642857985.json, 视频生成/图生视频/【阿良绘】WanMove轨迹控制：运动示例工作流_2007470369120198658.json, 视频生成/图生视频/【阿良绘】WanMove轨迹控制：运动示例工作流_2008000096457203714.json, 视频生成/图生视频/万相ATI字节最新轨迹驱动图生视频_1929817339246624770.json, 视频生成/图生视频/图生视频 轨迹控制 稳定好玩~【wan2.1】_1999451312800624642.json, 视频生成/文生视频/Wan-Move潜在轨迹引导视频生成_1998898965116542977.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_462

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/wanvideo_WanMove_I2V_example_1998599416028258305.json、视频生成/图生视频/【遇见AI】wan2.1 AIT轨迹控制图生视频_2071858962642857985.json、视频生成/图生视频/【阿良绘】WanMove轨迹控制：运动示例工作流_2007470369120198658.json、视频生成/图生视频/【阿良绘】WanMove轨迹控制：运动示例工作流_2008000096457203714.json、视频生成/图生视频/万相ATI字节最新轨迹驱动图生视频_1929817339246624770.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `SplineEditor`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 6/7 个有
- `WanVideoSetBlockSwap` —— 6/7 个有
- `WanVideoSetLoRAs` —— 6/7 个有
- `WanVideoTextEncode` —— 6/7 个有
- `RepeatImageBatch` —— 5/7 个有
- `WanVideoAddWanMoveTracks` —— 5/7 个有
- `WanVideoWanDrawWanMoveTracks` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 4/7 个有
- `WanVideoATITracks` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `AppendStringsToList` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `WanVideoATITracksVisualize` —— 1/7 个有
- `WanVideoTeaCache` —— 1/7 个有
- `WanVideoTextEncodeCached` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
