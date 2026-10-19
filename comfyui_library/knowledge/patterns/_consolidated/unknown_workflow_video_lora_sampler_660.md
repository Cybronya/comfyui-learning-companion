---
name: unknown_workflow_video_lora_sampler_660
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.675667
common_nodes: [CreateCFGScheduleFloatList, GetNode, INTConstant, ImageResizeKJv2, Int, LoadImage, LoadWanVideoT5TextEncoder, RH_Captioner, RH_Prompter, SetNode, TextCombinerTwo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1950019769790545922.json, 视频生成/图生视频/1950922029769891841.json, 视频生成/图生视频/1956166218438901761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_660

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1950019769790545922.json、视频生成/图生视频/1950922029769891841.json、视频生成/图生视频/1956166218438901761.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RH_Captioner`
- `RH_Prompter`
- `SetNode`
- `TextCombinerTwo`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `GIMMVFI_interpolate` —— 1/3 个有
- `LayerColor: Brightness & Contrast` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `Primitive integer [Crystools]` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `TextBox` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
