---
name: unknown_workflow_video_lora_sampler_853
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.708667
common_nodes: [AppendStringsToList, CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, SplineEditor, VHS_VideoCombine, WanVideoATITracks, WanVideoATITracksVisualize, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/03-05-05-WAN2.1-运镜控制-ATI多点轨迹引导图生视频_1989933219632082946.json, 视频生成/图生视频/ATI轨迹控制_1929724832999489537.json, 视频生成/图生视频/Wan2.1 ATI多点轨迹引导图生视频工作流_1929199069892349953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_853

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/03-05-05-WAN2.1-运镜控制-ATI多点轨迹引导图生视频_1989933219632082946.json、视频生成/图生视频/ATI轨迹控制_1929724832999489537.json、视频生成/图生视频/Wan2.1 ATI多点轨迹引导图生视频工作流_1929199069892349953.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `AppendStringsToList`
- `CLIPVisionLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SplineEditor`
- `VHS_VideoCombine`
- `WanVideoATITracks`
- `WanVideoATITracksVisualize`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `WanVideoEnhanceAVideo` —— 2/3 个有
- `WanVideoExperimentalArgs` —— 2/3 个有
- `WanVideoSLG` —— 2/3 个有
- `WanVideoTeaCache` —— 2/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
