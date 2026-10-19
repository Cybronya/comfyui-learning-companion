---
name: unknown_workflow_video_lora_sampler_430
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7778
common_nodes: [DownloadAndLoadFlorence2Model, Florence2Run, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, StringFunction|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1913951966869843970.json, 视频生成/图生视频/2060066021968539649.json, 视频生成/图生视频/1913946553239961602.json, 视频生成/图生视频/1926653775266877442.json, 视频生成/图生视频/1928694139590754306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_430

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1913951966869843970.json、视频生成/图生视频/2060066021968539649.json、视频生成/图生视频/1913946553239961602.json、视频生成/图生视频/1926653775266877442.json、视频生成/图生视频/1928694139590754306.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `StringFunction|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `WanVideoSLG` —— 4/5 个有
- `WanVideoTeaCache` —— 4/5 个有
- `Anything Everywhere` —— 3/5 个有
- `Seed Everywhere` —— 3/5 个有
- `WanVideoEnhanceAVideo` —— 3/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `Bjornulf_ShowInt` —— 1/5 个有
- `CLIPTextEncode` —— 1/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `CogVideoEnhanceAVideo` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `Text` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `WanVideoSetBlockSwap` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
