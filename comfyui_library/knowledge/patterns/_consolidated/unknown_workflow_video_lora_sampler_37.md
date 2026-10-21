---
name: unknown_workflow_video_lora_sampler_37
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.755875
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, StringFunction|pysssss, easy cleanGpuUsed, CR Text]
members: [图片生成/图生图/2054042696234356738.json, 图片生成/文生图/1930983914234687490.json, 图片生成/文生图/1940241127955976194.json, 视频生成/图生视频/1928668581439946753.json, 视频生成/图生视频/2054373287651749889.json, 视频生成/图生视频/2054382753839362050.json, 视频生成/图生视频/2054473798069563394.json, 视频生成/图生视频/2054478953833877505.json, 视频生成/图生视频/1928368447712051201.json, 视频生成/图生视频/1926535706535993346.json, 视频生成/图生视频/2033441724210618370.json, 视频生成/图生视频/2043932369274540034.json, 视频生成/图生视频/2067234276629901314.json, 视频生成/图生视频/1933695456268738561.json, 视频生成/图生视频/2053629546980753409.json, 视频生成/图生视频/超顺滑动漫动态壁纸-图生图一键生成_2053662483356893185.json, 视频生成/图生视频/2053670474537816066.json, 视频生成/图生视频/2053675574866001922.json, 视频生成/图生视频/2053993835801391105.json, 视频生成/图生视频/2054045816519708674.json, 视频生成/图生视频/2056564858732240898.json, 视频生成/图生视频/2071593615868129282.json, 视频生成/图生视频/2071596547552403457.json, 视频生成/图生视频/2078863256298545153.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/2054042696234356738.json、图片生成/文生图/1930983914234687490.json、图片生成/文生图/1940241127955976194.json、视频生成/图生视频/1928668581439946753.json、视频生成/图生视频/2054373287651749889.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 24 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 23/24 个有
- `CogVideoEnhanceAVideo` —— 23/24 个有
- `DownloadAndLoadFlorence2Model` —— 23/24 个有
- `Florence2Run` —— 23/24 个有
- `Int` —— 23/24 个有
- `MathExpression|pysssss` —— 23/24 个有
- `StringFunction|pysssss` —— 23/24 个有
- `WanVideoSetBlockSwap` —— 23/24 个有
- `ImageCASharpening+` —— 2/24 个有
- `WanVideoVACEModelSelect` —— 2/24 个有
- `CR Text` —— 1/24 个有
- `ImageSizeAndBatchSize` —— 1/24 个有
- `WanVideoExperimentalArgs` —— 1/24 个有
- `WanVideoSEDecode` —— 1/24 个有
- `WanVideoSEImageClipEncode` —— 1/24 个有
- `WanVideoSEModelLoader` —— 1/24 个有
- `WanVideoSESampler` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、MathExpression|pysssss、StringFunction|pysssss、easy cleanGpuUsed、CR Text
