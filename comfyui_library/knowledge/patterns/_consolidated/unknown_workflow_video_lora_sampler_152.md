---
name: unknown_workflow_video_lora_sampler_152
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.981583
common_nodes: [CreateCFGScheduleFloatList, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/59tsspws_2052395707415441409.json, 数字人/数字人/wan2.2图生视频+丝袜美女转圈=艾橘溪_2039691203502940162.json, 视频生成/图生视频/004.Wan视频之源005.首尾关键帧_2035336872209162242.json, 视频生成/图生视频/360度旋转版本(Wan2.2万相)工作流_2014940591578157057.json, 视频生成/图生视频/wan2.2图生视频+丝袜美女转圈=艾橘溪_1893899363629051906.json, 视频生成/图生视频/wan2.2图生视频+双模出图(结构+细节)_2052404579370848257.json, 视频生成/图生视频/wan2.2图生视频+美女转圈_2075491553438683138.json, 视频生成/图生视频/wan2.2图生视频+美女转圈。绝绝子，好用！_2031551233101664258.json, 视频生成/图生视频/wan2.2图生视频+美女转圈。绝绝子，好用！_2043583359116382210.json, 视频生成/图生视频/wan2.2图生视频_2080097509229293570.json, 视频生成/图生视频/通义万相WAN2.2_KJ加速版_高低噪声双lora在线本地通用_补帧_1952913426868858882.json, 视频生成/图生视频/通义万相WAN2.2_KJ加速版_高噪声lora在线本地通用_补帧_1952709897437777921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_152

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/反推提示词/59tsspws_2052395707415441409.json、数字人/数字人/wan2.2图生视频+丝袜美女转圈=艾橘溪_2039691203502940162.json、视频生成/图生视频/004.Wan视频之源005.首尾关键帧_2035336872209162242.json、视频生成/图生视频/360度旋转版本(Wan2.2万相)工作流_2014940591578157057.json、视频生成/图生视频/wan2.2图生视频+丝袜美女转圈=艾橘溪_1893899363629051906.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `GetImageSizeAndCount` —— 11/12 个有
- `Int` —— 11/12 个有
- `VHS_VideoCombine` —— 11/12 个有
- `WanVideoTorchCompileSettings` —— 11/12 个有
- `LayerUtility: PurgeVRAM` —— 8/12 个有
- `SimpleMath+` —— 8/12 个有
- `Fast Groups Muter (rgthree)` —— 3/12 个有
- `RIFE VFI` —— 3/12 个有
- `CreateVideo` —— 1/12 个有
- `JjkText` —— 1/12 个有
- `RTXVideoSuperResolution` —— 1/12 个有
- `SaveVideo` —— 1/12 个有
- `WanVideoLoraSelectMulti` —— 1/12 个有
- `WanVideoSLG` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
