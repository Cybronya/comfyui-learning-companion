---
name: unknown_workflow_video_lora_sampler_266
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.899667
common_nodes: [CreateCFGScheduleFloatList, INTConstant, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/大家一起来冲浪（Lora版）_2073033317150187521.json, 视频生成/图生视频/已做生图动画_1954716501561491457.json, 视频生成/图生视频/扭起来_1997179060881133570.json, 视频生成/图生视频/抖音坐着自拍_1959215164312727553.json, 视频生成/图生视频/抖音扭一扭_1957833676750159874.json, 视频生成/图生视频/抖音摇摆_1957824248537776130.json, 视频生成/图生视频/抖音涨粉利器真实跳舞抖胸_1979579693227741185.json, 视频生成/图生视频/抖音走路_1958894026126733314.json, 视频生成/图生视频/自拍2_1972314410939248641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_266

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/大家一起来冲浪（Lora版）_2073033317150187521.json、视频生成/图生视频/已做生图动画_1954716501561491457.json、视频生成/图生视频/扭起来_1997179060881133570.json、视频生成/图生视频/抖音坐着自拍_1959215164312727553.json、视频生成/图生视频/抖音扭一扭_1957833676750159874.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `CR Prompt Text` —— 8/9 个有
- `LayerUtility: PurgeVRAM` —— 8/9 个有
- `CR Text Concatenate` —— 7/9 个有
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `DownloadAndLoadGIMMVFIModel` —— 6/9 个有
- `GIMMVFI_interpolate` —— 6/9 个有
- `RHHiddenNodes` —— 6/9 个有
- `GetImageSizeAndCount` —— 5/9 个有
- `ImageUpscaleWithModel` —— 4/9 个有
- `UpscaleModelLoader` —— 4/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `GetNode` —— 1/9 个有
- `RH_Captioner` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `ShowText` —— 1/9 个有
- `StringReplace` —— 1/9 个有
- `WanVideoContextOptions` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
