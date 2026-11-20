---
name: unknown_workflow_video_lora_sampler_330
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.956889
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/CG迷-WAN2.2 multitalk对口型工作流_1952358621646655489.json, 视频生成/图生视频/CG迷-Wan2.2 Kijai图生视频工作流（支持gguf）_1950495596585144322.json, 视频生成/图生视频/CG迷-Wan2.2 Kijai首尾帧频工作流（支持gguf）_1952283809247080449.json, 视频生成/图生视频/KJ版Wan2.2 图生视频超级加速+镜头切换V2版_1950822532939186177.json, 视频生成/图生视频/KJ版Wan2.2 图生视频超级加速+镜头切换_1950805737444417537.json, 视频生成/图生视频/WAN2.2图生视频_1963873192061521922.json, 视频生成/图生视频/WAN2.2图生视频（KJ8步+可做数据集）_1958716775745667074.json, 视频生成/图生视频/Wan2.2 kijai 4步lora 快速图生视频极速版_1978124333073719297.json, 视频生成/图生视频/灵动传媒短视频生成（最新版）_1954808332802506754.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_330

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/CG迷-WAN2.2 multitalk对口型工作流_1952358621646655489.json、视频生成/图生视频/CG迷-Wan2.2 Kijai图生视频工作流（支持gguf）_1950495596585144322.json、视频生成/图生视频/CG迷-Wan2.2 Kijai首尾帧频工作流（支持gguf）_1952283809247080449.json、视频生成/图生视频/KJ版Wan2.2 图生视频超级加速+镜头切换V2版_1950822532939186177.json、视频生成/图生视频/KJ版Wan2.2 图生视频超级加速+镜头切换_1950805737444417537.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
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
- `INTConstant` —— 7/9 个有
- `CR Prompt Text` —— 5/9 个有
- `ImageFromBatch+` —— 5/9 个有
- `LayerUtility: PurgeVRAM` —— 5/9 个有
- `WanVideoTorchCompileSettings` —— 4/9 个有
- `JWInteger` —— 3/9 个有
- `LoadAudio` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `DownloadAndLoadWav2VecModel` —— 1/9 个有
- `FloatToSigmas` —— 1/9 个有
- `InversionDemoLazyIndexSwitch` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `MultiTalkModelLoader` —— 1/9 个有
- `MultiTalkWav2VecEmbeds` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有
- `Random Number` —— 1/9 个有
- `StringToFloatList` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
