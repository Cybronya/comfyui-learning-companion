---
name: unknown_workflow_video_lora_sampler_162
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.952
common_nodes: [CreateCFGScheduleFloatList, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/360度旋转版本(Wan2.2万相)工作流_2014940591578157057.json, 视频生成/图生视频/8-图转视频 Wan2.2 14b Optional Last Frame_2053486047740350466.json, 视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_1952003952139292673.json, 视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_2061786208002465793.json, 视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_2061806465001803778.json, 视频生成/图生视频/CG迷-Wan2.2 Kijai图生视频工作流（支持gguf）_1950495596585144322.json, 视频生成/图生视频/CG迷-Wan2.2 Kijai首尾帧频工作流（支持gguf）_1952283809247080449.json, 视频生成/图生视频/KJ版Wan2.2 图生视频超级加速+镜头切换V2版_1950822532939186177.json, 视频生成/图生视频/KJ版Wan2.2 图生视频超级加速+镜头切换_1950805737444417537.json, 视频生成/图生视频/WAN2.2图生视频（KJ8步+可做数据集）_1958716775745667074.json, 视频生成/图生视频/Wan2.2 kijai 4步lora 快速图生视频极速版_1978124333073719297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_162

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/360度旋转版本(Wan2.2万相)工作流_2014940591578157057.json、视频生成/图生视频/8-图转视频 Wan2.2 14b Optional Last Frame_2053486047740350466.json、视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_1952003952139292673.json、视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_2061786208002465793.json、视频生成/图生视频/AIwood-Wan2.2首尾帧Kijai版_2061806465001803778.json…）

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
- `INTConstant` —— 9/11 个有
- `WanVideoTorchCompileSettings` —— 8/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/11 个有
- `ImageResizeKJv2` —— 5/11 个有
- `CR Prompt Text` —— 4/11 个有
- `ImageFromBatch+` —— 4/11 个有
- `LayerUtility: PurgeVRAM` —— 4/11 个有
- `JWInteger` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `MathExpression|pysssss` —— 2/11 个有
- `RIFE VFI` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有
- `FloatToSigmas` —— 1/11 个有
- `Int` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有
- `Seed (rgthree)` —— 1/11 个有
- `StringToFloatList` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
