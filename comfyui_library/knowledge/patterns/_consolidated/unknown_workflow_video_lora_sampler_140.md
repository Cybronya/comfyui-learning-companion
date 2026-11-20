---
name: unknown_workflow_video_lora_sampler_140
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.9438
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2图生视频kj版_1950852674944180226.json, 视频生成/图生视频/wan2.2图生视频kj版_1978672767467982850.json, 视频生成/图生视频/wan2.2图生视频（KJ流）加速_1950178102964084737.json, 视频生成/图生视频/wan2.2首尾帧(KJ版)_1951645924265283586.json, 视频生成/图生视频/一键花瓣消散_1967820040437399554.json, 视频生成/图生视频/动态表情包_2005731300571049986.json, 视频生成/图生视频/变形金刚工作流_1959096828304240641.json, 视频生成/图生视频/大明动画风格 图生视频_1962000212275478530.json, 视频生成/图生视频/扭起来_1997179060881133570.json, 视频生成/图生视频/抖音坐着自拍_1959215164312727553.json, 视频生成/图生视频/抖音扭一扭_1957833676750159874.json, 视频生成/图生视频/抖音摇摆_1957824248537776130.json, 视频生成/图生视频/抖音涨粉利器真实跳舞抖胸_1979579693227741185.json, 视频生成/图生视频/抖音走路_1958894026126733314.json, 视频生成/图生视频/自拍2_1972314410939248641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_140

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/wan2.2图生视频kj版_1950852674944180226.json、视频生成/图生视频/wan2.2图生视频kj版_1978672767467982850.json、视频生成/图生视频/wan2.2图生视频（KJ流）加速_1950178102964084737.json、视频生成/图生视频/wan2.2首尾帧(KJ版)_1951645924265283586.json、视频生成/图生视频/一键花瓣消散_1967820040437399554.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 15 个 workflow 都包含：
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
- `WanVideoLoraSelect` —— 14/15 个有
- `CreateCFGScheduleFloatList` —— 13/15 个有
- `INTConstant` —— 13/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/15 个有
- `JWInteger` —— 12/15 个有
- `WanVideoTorchCompileSettings` —— 11/15 个有
- `CR Prompt Text` —— 10/15 个有
- `GetImageSizeAndCount` —— 10/15 个有
- `LayerUtility: PurgeVRAM` —— 9/15 个有
- `CR Text Concatenate` —— 7/15 个有
- `RHHiddenNodes` —— 7/15 个有
- `DownloadAndLoadGIMMVFIModel` —— 6/15 个有
- `GIMMVFI_interpolate` —— 6/15 个有
- `ImageFromBatch+` —— 4/15 个有
- `ImageUpscaleWithModel` —— 4/15 个有
- `UpscaleModelLoader` —— 4/15 个有
- `ImageResizeKJv2` —— 3/15 个有
- `Text` —— 2/15 个有
- `easy cleanGpuUsed` —— 2/15 个有
- `ConcatTextOfUtils` —— 1/15 个有
- `RH_Translator` —— 1/15 个有
- `RIFE VFI` —— 1/15 个有
- `ShowText|pysssss` —— 1/15 个有
- `YC Color Match` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
