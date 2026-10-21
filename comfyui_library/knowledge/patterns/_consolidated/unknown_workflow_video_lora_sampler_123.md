---
name: unknown_workflow_video_lora_sampler_123
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.938923
common_nodes: [CreateCFGScheduleFloatList, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2053486047740350466.json, 视频生成/图生视频/1952003952139292673.json, 视频生成/图生视频/2061786208002465793.json, 视频生成/图生视频/2061806465001803778.json, 视频生成/图生视频/1950495596585144322.json, 视频生成/图生视频/1952283809247080449.json, 视频生成/图生视频/1968577373975261186.json, 视频生成/图生视频/2015424489110118402.json, 视频生成/图生视频/1949986819199909890.json, 视频生成/图生视频/1950060354116214786.json, 视频生成/图生视频/1955263438596423682.json, 视频生成/图生视频/1950132208273154049.json, 视频生成/文生视频/1950433801442910210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_123

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2053486047740350466.json、视频生成/图生视频/1952003952139292673.json、视频生成/图生视频/2061786208002465793.json、视频生成/图生视频/2061806465001803778.json、视频生成/图生视频/1950495596585144322.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 12/13 个有
- `WanVideoImageToVideoEncode` —— 12/13 个有
- `WanVideoTorchCompileSettings` —— 11/13 个有
- `ImageResizeKJv2` —— 10/13 个有
- `INTConstant` —— 9/13 个有
- `MathExpression|pysssss` —— 4/13 个有
- `Primitive integer [Crystools]` —— 4/13 个有
- `Text Multiline` —— 4/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/13 个有
- `CreateVideo` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `GetImageSize` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `LayerUtility: PurgeVRAM` —— 1/13 个有
- `PreViewVideo` —— 1/13 个有
- `RIFE VFI` —— 1/13 个有
- `Seed (rgthree)` —— 1/13 个有
- `WanVideoEmptyEmbeds` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
