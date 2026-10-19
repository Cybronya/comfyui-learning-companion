---
name: unknown_workflow_video_lora_sampler_193
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5725
common_nodes: [CLIPVisionLoader, DrawViTPose, GetNode, ImageResizeKJv2, JWInteger, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy mathInt, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1978123000795029506.json, 视频生成/图生视频/叮叮的鼓点咚咚咚_2083830136331399170.json, 视频生成/图生视频/女生舞蹈复刻_2098325811605622786.json, 视频生成/图生视频/2071997191392157697.json, 视频生成/图生视频/2073410541107896321.json, 视频生成/图生视频/舞蹈动作复刻_2086688476229095425.json, 视频生成/图生视频/舞蹈动作模仿2_2101567862912671746.json, 视频生成/图生视频/舞蹈动作模仿_2084254634042023937.json, 视频生成/图生视频/2080278150566735874.json, 视频生成/图生视频/2079046607487725569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_193

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1978123000795029506.json、视频生成/图生视频/叮叮的鼓点咚咚咚_2083830136331399170.json、视频生成/图生视频/女生舞蹈复刻_2098325811605622786.json、视频生成/图生视频/2071997191392157697.json、视频生成/图生视频/2073410541107896321.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetNode`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy mathInt`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 9/10 个有
- `VHS_VideoInfoSource` —— 9/10 个有
- `LayerUtility: PurgeVRAM V2` —— 8/10 个有
- `ImageConcatenate_UTK` —— 6/10 个有
- `WanAnimatePlus BlockSwap` —— 5/10 个有
- `WanVideoTorchCompileSettings` —— 4/10 个有
- `BatchCount+` —— 1/10 个有
- `CM_IntToFloat` —— 1/10 个有
- `GradientImage` —— 1/10 个有
- `ImpactInt` —— 1/10 个有
- `Int` —— 1/10 个有
- `LazySwitch1way` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `WanVideoBlockSwap` —— 1/10 个有
- `easy batchAnything` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy compare` —— 1/10 个有
- `easy forLoopEnd` —— 1/10 个有
- `easy forLoopStart` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
