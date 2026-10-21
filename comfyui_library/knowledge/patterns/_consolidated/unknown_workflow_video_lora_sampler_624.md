---
name: unknown_workflow_video_lora_sampler_624
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.968
common_nodes: [ColorMatch, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, RH_Translator, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/1934433981473452033.json, 视频生成/图生视频/1934634580886659073.json, 视频生成/图生视频/1932804540896792578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_624

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1934433981473452033.json、视频生成/图生视频/1934634580886659073.json、视频生成/图生视频/1932804540896792578.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `ColorMatch`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RH_Translator`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `LayerMask: LoadFlorence2Model` —— 2/3 个有
- `LayerUtility: Florence2Image2Prompt` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `WanVideoEnhanceAVideo` —— 2/3 个有
- `WanVideoVACEStartToEndFrame` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `GetImageSizeAndCount` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `WanVideoMagCache` —— 1/3 个有
- `WanVideoVACEModelSelect` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
