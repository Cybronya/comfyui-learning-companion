---
name: unknown_workflow_video_lora_sampler_281
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.887125
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, INTConstant, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2073033317150187521.json, 视频生成/图生视频/1997179060881133570.json, 视频生成/图生视频/1959215164312727553.json, 视频生成/图生视频/1957833676750159874.json, 视频生成/图生视频/1957824248537776130.json, 视频生成/图生视频/1979579693227741185.json, 视频生成/图生视频/1958894026126733314.json, 视频生成/图生视频/1972314410939248641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_281

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2073033317150187521.json、视频生成/图生视频/1997179060881133570.json、视频生成/图生视频/1959215164312727553.json、视频生成/图生视频/1957833676750159874.json、视频生成/图生视频/1957824248537776130.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `DownloadAndLoadGIMMVFIModel` —— 6/8 个有
- `GIMMVFI_interpolate` —— 6/8 个有
- `RHHiddenNodes` —— 6/8 个有
- `GetImageSizeAndCount` —— 5/8 个有
- `ImageUpscaleWithModel` —— 4/8 个有
- `UpscaleModelLoader` —— 4/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `GetNode` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `ShowText` —— 1/8 个有
- `StringReplace` —— 1/8 个有
- `WanVideoContextOptions` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
