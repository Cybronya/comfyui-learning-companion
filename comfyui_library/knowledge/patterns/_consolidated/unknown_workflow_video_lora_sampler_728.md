---
name: unknown_workflow_video_lora_sampler_728
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9655
common_nodes: [CreateCFGScheduleFloatList, FloatConstant, GetImageSizeAndCount, INTConstant, ImageResizeKJ, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, SaveImage, ShowText|pysssss, TT_img_enc, Text Random Line, TextCombinerTwo, TextInput_, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2007442248425807873.json, 视频生成/图生视频/2007441699622096897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_728

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2007442248425807873.json、视频生成/图生视频/2007441699622096897.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `FloatConstant`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJ`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SaveImage`
- `ShowText|pysssss`
- `TT_img_enc`
- `Text Random Line`
- `TextCombinerTwo`
- `TextInput_`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `WanVideoContextOptions` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
