---
name: unknown_workflow_video_lora_sampler_223
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.919333
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wanmove轨迹控制_2000380802502455298.json, 视频生成/图生视频/Wanmove轨迹控制运动_1999041056794628098.json, 视频生成/图生视频/Wanmove轨迹控制运动_1999430361350275074.json, 视频生成/图生视频/Wanmove轨迹控制运动视频_2007414676862279682.json, 视频生成/图生视频/wan2.2 图生图_1995404196142833665.json, 视频生成/图生视频/wanvideo_WanMove_I2V_example_1998599416028258305.json, 视频生成/图生视频/【阿良绘】WanMove轨迹控制：运动示例工作流_2007470369120198658.json, 视频生成/图生视频/【阿良绘】WanMove轨迹控制：运动示例工作流_2008000096457203714.json, 视频生成/图生视频/图生视频 轨迹控制 稳定好玩~【wan2.1】_1999451312800624642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_223

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Wanmove轨迹控制_2000380802502455298.json、视频生成/图生视频/Wanmove轨迹控制运动_1999041056794628098.json、视频生成/图生视频/Wanmove轨迹控制运动_1999430361350275074.json、视频生成/图生视频/Wanmove轨迹控制运动视频_2007414676862279682.json、视频生成/图生视频/wan2.2 图生图_1995404196142833665.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `RepeatImageBatch` —— 8/9 个有
- `SplineEditor` —— 8/9 个有
- `WanVideoAddWanMoveTracks` —— 8/9 个有
- `WanVideoWanDrawWanMoveTracks` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `INTConstant` —— 4/9 个有
- `easy showAnything` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `FloatToSigmas` —— 1/9 个有
- `ImpactInt` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `LayerUtility: TextBox` —— 1/9 个有
- `Note Plus (mtb)` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有
- `StringToFloatList` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
