---
name: unknown_workflow_video_lora_sampler_450
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 1
common_nodes: [Int, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2070959715483475969.json, 视频生成/图生视频/1949636462812778497.json, 视频生成/图生视频/1932620542149324802.json, 视频生成/图生视频/1930526505158496258.json, 视频生成/图生视频/2018170301388955650.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_450

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2070959715483475969.json、视频生成/图生视频/1949636462812778497.json、视频生成/图生视频/1932620542149324802.json、视频生成/图生视频/1930526505158496258.json、视频生成/图生视频/2018170301388955650.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `Int`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `LayerUtility: PurgeVRAM V2` —— 4/5 个有
- `WanVideoEnhanceAVideo` —— 4/5 个有
- `WanVideoSLG` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `ImageSizeAndBatchSize` —— 3/5 个有
- `WanVideoTeaCache` —— 3/5 个有
- `WanVideoExperimentalArgs` —— 2/5 个有
- `CR Upscale Image` —— 1/5 个有
- `DownloadAndLoadFlorence2Model` —— 1/5 个有
- `Florence2Run` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `StringFunction|pysssss` —— 1/5 个有
- `WanVideoLoraSelectMulti` —— 1/5 个有
- `WanVideoMagCache` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
