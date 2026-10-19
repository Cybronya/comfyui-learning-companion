---
name: unknown_workflow_controlnet_video_lora_8
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.951667
common_nodes: [CR Prompt Text, ImageConcanate, ImageResizeKJ, JWInteger, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1945410798665572353.json, 视频生成/图生视频/1928986648586129410.json, 视频生成/图生视频/1928871989627273218.json, 视频生成/图生视频/1929015446484238338.json, 视频生成/图生视频/2000739633522671617.json, 视频生成/图生视频/1929133519367475202.json, 视频生成/图生视频/1957795522704764930.json, 视频生成/图生视频/1931247339858493442.json, 视频生成/图生视频/1931944580948930561.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_8

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1945410798665572353.json、视频生成/图生视频/1928986648586129410.json、视频生成/图生视频/1928871989627273218.json、视频生成/图生视频/1929015446484238338.json、视频生成/图生视频/2000739633522671617.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CR Prompt Text`
- `ImageConcanate`
- `ImageResizeKJ`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 7/9 个有
- `LoadImage` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `RunningHub OmniConsistency LoraLoader` —— 3/9 个有
- `RunningHub OmniConsistency Sampler` —— 3/9 个有
- `SaveImage` —— 3/9 个有
- `ColorCorrect` —— 2/9 个有
- `EasyControlGenerate` —— 2/9 个有
- `EasyControlLoadFlux` —— 2/9 个有
- `EasyControlLoadLora` —— 2/9 个有
- `GetImageRangeFromBatch` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `WanVideoEasyCache` —— 1/9 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/9 个有
- `WanVideoUniAnimatePoseInput` —— 1/9 个有
- `easy promptConcat` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
