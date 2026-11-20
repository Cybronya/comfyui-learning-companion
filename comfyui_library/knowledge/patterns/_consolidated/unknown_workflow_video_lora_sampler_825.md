---
name: unknown_workflow_video_lora_sampler_825
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.888
common_nodes: [CLIPVisionLoader, CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/图生视频 · 万物飘散 _ Wan2.2 I2V 双通道 原片直出_2056372722174881794.json, 视频生成/图生视频/wan 2.2 冰冻视频特效_1953012198424702978.json, 视频生成/图生视频/冰天雪地视频特效_2004446571733417986.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_825

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/图生视频 · 万物飘散 _ Wan2.2 I2V 双通道 原片直出_2056372722174881794.json、视频生成/图生视频/wan 2.2 冰冻视频特效_1953012198424702978.json、视频生成/图生视频/冰天雪地视频特效_2004446571733417986.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
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
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `Text` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
