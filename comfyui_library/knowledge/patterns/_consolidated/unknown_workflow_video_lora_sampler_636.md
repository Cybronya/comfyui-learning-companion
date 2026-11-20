---
name: unknown_workflow_video_lora_sampler_636
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPVisionLoader, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: TextBox, LoadImage, LoadWanVideoT5TextEncoder, VHS_SelectEveryNthImage, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/电眼雷神_1964946808004820993.json, 视频生成/图生视频/wan 极限奔跑视频特效_1951958322155081729.json, 视频生成/图生视频/眼冒闪电视频特效_1922989414665154562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_636

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/电眼雷神_1964946808004820993.json、视频生成/图生视频/wan 极限奔跑视频特效_1951958322155081729.json、视频生成/图生视频/眼冒闪电视频特效_1922989414665154562.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: TextBox`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_SelectEveryNthImage`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 2/3 个有
- `StringFunction|pysssss` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `easy int` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
