---
name: unknown_workflow_video_lora_sampler_149
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.946385
common_nodes: [CreateCFGScheduleFloatList, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2 图生视频工作量_1974850739472306178.json, 视频生成/图生视频/wan2.2 图生视频，kj版8步加速_1960977035327934465.json, 视频生成/图生视频/wan2.2首尾帧(KJ版)_1951645924265283586.json, 视频生成/图生视频/【Wan2.2首尾帧】最新万相14B FLF2V 首尾帧视频加速版 图生视频_1972187694434545666.json, 视频生成/图生视频/角色-wan2.2单帧视频-带bounce-lora_2049487704492085249.json, 视频生成/图生视频/首尾帧视频-WAN2.2_1983929785862782977.json, 视频生成/图生视频/首尾帧视频-WAN2.2高质量版_1967833229766045698.json, 视频生成/图生视频/首尾帧视频-WAN2.2高质量（快速版）_1983506063989350402.json, 视频生成/图生视频/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_1984560751979479042.json, 视频生成/图生视频/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_2065457354044436482.json, 视频生成/图生视频/首尾帧视频加速版-WAN2.2高质量版（2分钟版））_1975787669600997377.json, 视频生成/图生视频/首尾帧视频加速版-WAN2.2高质量版（2分钟版））_1976838603810787330.json, 视频生成/图生视频/高质量WAN2.2首尾帧极速版_2007622545448640513.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_149

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/wan2.2 图生视频工作量_1974850739472306178.json、视频生成/图生视频/wan2.2 图生视频，kj版8步加速_1960977035327934465.json、视频生成/图生视频/wan2.2首尾帧(KJ版)_1951645924265283586.json、视频生成/图生视频/【Wan2.2首尾帧】最新万相14B FLF2V 首尾帧视频加速版 图生视频_1972187694434545666.json、视频生成/图生视频/角色-wan2.2单帧视频-带bounce-lora_2049487704492085249.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 13 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 12/13 个有
- `JWInteger` —— 12/13 个有
- `WanVideoDecode` —— 12/13 个有
- `WanVideoImageToVideoEncode` —— 12/13 个有
- `WanVideoClipVisionEncode` —— 11/13 个有
- `CR Prompt Text` —— 10/13 个有
- `ImageResize+` —— 10/13 个有
- `LoadWanVideoClipTextEncoder` —— 10/13 个有
- `SimpleMath+` —— 9/13 个有
- `LayerUtility: PurgeVRAM` —— 8/13 个有
- `easy cleanGpuUsed` —— 8/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/13 个有
- `DF_Int_to_Float` —— 3/13 个有
- `GetImageSizeAndCount` —— 3/13 个有
- `Bjornulf_ShowFloat` —— 1/13 个有
- `CLIPVisionLoader` —— 1/13 个有
- `CR SDXL Aspect Ratio` —— 1/13 个有
- `Float` —— 1/13 个有
- `GetNode` —— 1/13 个有
- `MathExpression|pysssss` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有
- `RIFE VFI` —— 1/13 个有
- `SetNode` —— 1/13 个有
- `TrimVideoLatent` —— 1/13 个有
- `WanVideoLoraSelectMulti` —— 1/13 个有
- `easy seed` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
