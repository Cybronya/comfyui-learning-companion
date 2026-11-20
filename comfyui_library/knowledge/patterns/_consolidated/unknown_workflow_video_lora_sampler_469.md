---
name: unknown_workflow_video_lora_sampler_469
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.901571
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, INTConstant, ImageResize+, JWInteger, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/首尾帧视频-WAN2.2高质量（快速版）_1983506063989350402.json, 视频生成/图生视频/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_1984560751979479042.json, 视频生成/图生视频/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_2065457354044436482.json, 视频生成/图生视频/首尾帧视频加速版-WAN2.2高质量版（2分钟版））_1975787669600997377.json, 视频生成/图生视频/首尾帧视频加速版-WAN2.2高质量版（2分钟版））_1976838603810787330.json, 视频生成/图生视频/高质量WAN2.2首尾帧极速版_2007622545448640513.json, 视频生成/文生视频/02 Wan2.2 Smooth Mix I2V首尾帧生视频+全节点注释_2055549969884565506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_469

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/首尾帧视频-WAN2.2高质量（快速版）_1983506063989350402.json、视频生成/图生视频/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_1984560751979479042.json、视频生成/图生视频/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_2065457354044436482.json、视频生成/图生视频/首尾帧视频加速版-WAN2.2高质量版（2分钟版））_1975787669600997377.json、视频生成/图生视频/首尾帧视频加速版-WAN2.2高质量版（2分钟版））_1976838603810787330.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `ImageResize+`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 6/7 个有
- `SimpleMath+` —— 6/7 个有
- `WanVideoDecode` —— 6/7 个有
- `WanVideoImageToVideoEncode` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `DF_Int_to_Float` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `Bjornulf_ShowFloat` —— 1/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `Float` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `WanVideoLoraSelectMulti` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
