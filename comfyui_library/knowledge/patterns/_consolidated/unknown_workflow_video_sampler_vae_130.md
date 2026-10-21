---
name: unknown_workflow_video_sampler_vae_130
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.842
common_nodes: [CLIPVisionLoader, CR Text, ImpactInt, LoadImage, LoadWanVideoT5TextEncoder, SimpleMath+, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1936026655389306882.json, 视频生成/图生视频/1985179323869052930.json, 视频生成/图生视频/2058042457992028161.json, 视频生成/文生视频/电商女装男装童装带货动图+全节点注释_2057109561508712450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_130

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1936026655389306882.json、视频生成/图生视频/1985179323869052930.json、视频生成/图生视频/2058042457992028161.json、视频生成/文生视频/电商女装男装童装带货动图+全节点注释_2057109561508712450.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Text`
- `ImpactInt`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 3/4 个有
- `Qwen3VL_Advanced` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `LayerColor: ColorAdapter` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `WanVideoLoraSelect` —— 1/4 个有
- `WanVideoLoraSelectMulti` —— 1/4 个有
- `WanVideoMagCache` —— 1/4 个有
- `WanVideoTextEncode` —— 1/4 个有
- `WanVideoVRAMManagement` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
