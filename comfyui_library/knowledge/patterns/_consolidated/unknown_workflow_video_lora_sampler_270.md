---
name: unknown_workflow_video_lora_sampler_270
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9765
common_nodes: [LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2图生视频kj版_1950852674944180226.json, 视频生成/图生视频/wan2.2图生视频kj版_1978672767467982850.json, 视频生成/图生视频/wan2.2首尾帧(KJ版)_1951645924265283586.json, 视频生成/图生视频/一键花瓣消散_1967820040437399554.json, 视频生成/图生视频/动态表情包_2005731300571049986.json, 视频生成/图生视频/变形金刚工作流_1959096828304240641.json, 视频生成/图生视频/图生视频（Wan2.2-V1）高质量加速版_1950432359721123842.json, 视频生成/图生视频/灵动传媒短视频生成（最新版）_1954808332802506754.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_270

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/wan2.2图生视频kj版_1950852674944180226.json、视频生成/图生视频/wan2.2图生视频kj版_1978672767467982850.json、视频生成/图生视频/wan2.2首尾帧(KJ版)_1951645924265283586.json、视频生成/图生视频/一键花瓣消散_1967820040437399554.json、视频生成/图生视频/动态表情包_2005731300571049986.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 7/8 个有
- `CreateCFGScheduleFloatList` —— 6/8 个有
- `INTConstant` —— 6/8 个有
- `JWInteger` —— 6/8 个有
- `GetImageSizeAndCount` —— 5/8 个有
- `CR Prompt Text` —— 4/8 个有
- `ImageFromBatch+` —— 4/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `RIFE VFI` —— 2/8 个有
- `Text` —— 2/8 个有
- `ImpactSwitch` —— 1/8 个有
- `InversionDemoLazyIndexSwitch` —— 1/8 个有
- `LayerUtility: TextJoinV2` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `Random Number` —— 1/8 个有
- `easy int` —— 1/8 个有
- `easy seed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
