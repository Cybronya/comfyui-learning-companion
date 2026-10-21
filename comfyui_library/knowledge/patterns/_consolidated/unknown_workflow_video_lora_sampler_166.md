---
name: unknown_workflow_video_lora_sampler_166
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.947727
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1950100729937747969.json, 视频生成/图生视频/1954848772384710658.json, 视频生成/图生视频/1953405056387305473.json, 视频生成/图生视频/1988552709458542593.json, 视频生成/图生视频/1953012198424702978.json, 视频生成/图生视频/1951106522648653826.json, 视频生成/图生视频/2004446571733417986.json, 视频生成/图生视频/2005731300571049986.json, 视频生成/图生视频/1959096828304240641.json, 视频生成/图生视频/1962000212275478530.json, 视频生成/图生视频/1954808332802506754.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_166

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1950100729937747969.json、视频生成/图生视频/1954848772384710658.json、视频生成/图生视频/1953405056387305473.json、视频生成/图生视频/1988552709458542593.json、视频生成/图生视频/1953012198424702978.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
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
- `INTConstant` —— 10/11 个有
- `CR Prompt Text` —— 8/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/11 个有
- `JWInteger` —— 7/11 个有
- `ImageFromBatch+` —— 6/11 个有
- `LayerUtility: PurgeVRAM` —— 6/11 个有
- `CLIPVisionLoader` —— 3/11 个有
- `WanVideoClipVisionEncode` —— 3/11 个有
- `WanVideoTorchCompileSettings` —— 3/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `WanVideoTeaCache` —— 2/11 个有
- `ConcatTextOfUtils` —— 1/11 个有
- `Display Int (rgthree)` —— 1/11 个有
- `InversionDemoLazyIndexSwitch` —— 1/11 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 1/11 个有
- `LoadAudio` —— 1/11 个有
- `RIFE VFI` —— 1/11 个有
- `Random Number` —— 1/11 个有
- `YC Color Match` —— 1/11 个有
- `easy mathInt` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
