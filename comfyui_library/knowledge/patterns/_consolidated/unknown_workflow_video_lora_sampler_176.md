---
name: unknown_workflow_video_lora_sampler_176
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8567
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, INTConstant, ImageResize+, JWInteger, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [LayerUtility: PurgeVRAM, SimpleMath+, easy cleanGpuUsed, CR Prompt Text, ImageResize+]
members: [图片生成/文生图/1980937502708158465.json, 视频生成/图生视频/1952002049745563650.json, 视频生成/图生视频/1956601025757151233.json, 视频生成/图生视频/1956583088841261058.json, 视频生成/图生视频/1952012888850509826.json, 视频生成/图生视频/1996851492734869506.json, 视频生成/图生视频/1981935370910744577.json, 视频生成/图生视频/1952320153679794177.json, 视频生成/图生视频/1978297110992969730.json, 视频生成/图生视频/1963913944572248066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_176

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1980937502708158465.json、视频生成/图生视频/1952002049745563650.json、视频生成/图生视频/1956601025757151233.json、视频生成/图生视频/1956583088841261058.json、视频生成/图生视频/1952012888850509826.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `ImageResize+`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
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
- `AddLabel` —— 6/10 个有
- `EmptyImage` —— 6/10 个有
- `GetImageSizeAndCount` —— 6/10 个有
- `ImageConcatMulti` —— 6/10 个有
- `SimpleMath+` —— 3/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `GetNode` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `PrimitiveBoolean` —— 1/10 个有
- `easy ifElse` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、SimpleMath+、easy cleanGpuUsed、CR Prompt Text、ImageResize+
