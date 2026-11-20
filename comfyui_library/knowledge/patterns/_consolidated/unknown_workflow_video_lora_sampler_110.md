---
name: unknown_workflow_video_lora_sampler_110
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.938438
common_nodes: [CreateCFGScheduleFloatList, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/59tsspws_2052395707415441409.json, 数字人/数字人/wan2.2图生视频+丝袜美女转圈=艾橘溪_2039691203502940162.json, 视频生成/图生视频/004.Wan视频之源005.首尾关键帧_2035336872209162242.json, 视频生成/图生视频/360度旋转版本(Wan2.2万相)工作流_2014940591578157057.json, 视频生成/图生视频/Work-Fisher_Wan2.2-I2V增强版_1972312939401310209.json, 视频生成/图生视频/wan2.2图生视频+丝袜美女转圈=艾橘溪_1893899363629051906.json, 视频生成/图生视频/wan2.2图生视频+双模出图(结构+细节)_2052404579370848257.json, 视频生成/图生视频/wan2.2图生视频+美女转圈_2075491553438683138.json, 视频生成/图生视频/wan2.2图生视频+美女转圈。绝绝子，好用！_2031551233101664258.json, 视频生成/图生视频/wan2.2图生视频+美女转圈。绝绝子，好用！_2043583359116382210.json, 视频生成/图生视频/wan2.2图生视频_2080097509229293570.json, 视频生成/图生视频/通义万相WAN2.2_KJ加速版_高低噪声双lora在线本地通用_补帧_1952913426868858882.json, 视频生成/图生视频/通义万相WAN2.2_KJ加速版_高噪声lora在线本地通用_补帧_1952709897437777921.json, 视频生成/文生视频/Work-Fisher_Wan2.2增强版合集_1972651753634242561.json, 视频生成/文生视频/rlinhe_Wan2.2增强版合集 by B站 Work-Fisher_1975195105038569473.json, 视频生成/文生视频/漫剧最强工具Wan2.2超强一致性_2049103222916259841.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_110

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/反推提示词/59tsspws_2052395707415441409.json、数字人/数字人/wan2.2图生视频+丝袜美女转圈=艾橘溪_2039691203502940162.json、视频生成/图生视频/004.Wan视频之源005.首尾关键帧_2035336872209162242.json、视频生成/图生视频/360度旋转版本(Wan2.2万相)工作流_2014940591578157057.json、视频生成/图生视频/Work-Fisher_Wan2.2-I2V增强版_1972312939401310209.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 16 个 workflow 都包含：
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
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 15/16 个有
- `Int` —— 15/16 个有
- `VHS_VideoCombine` —— 15/16 个有
- `WanVideoTorchCompileSettings` —— 15/16 个有
- `WanVideoSetBlockSwap` —— 12/16 个有
- `WanVideoSetLoRAs` —— 12/16 个有
- `LayerUtility: PurgeVRAM` —— 8/16 个有
- `SimpleMath+` —— 8/16 个有
- `RIFE VFI` —— 7/16 个有
- `Fast Groups Bypasser (rgthree)` —— 4/16 个有
- `WanVideoLoraSelectMulti` —— 4/16 个有
- `Fast Groups Muter (rgthree)` —— 3/16 个有
- `WanVideoEmptyEmbeds` —— 3/16 个有
- `CreateVideo` —— 1/16 个有
- `JjkText` —— 1/16 个有
- `RTXVideoSuperResolution` —— 1/16 个有
- `SaveVideo` —— 1/16 个有
- `ShellAgentPluginSaveImage` —— 1/16 个有
- `WanVideoSLG` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
