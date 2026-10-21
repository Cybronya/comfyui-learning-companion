---
name: unknown_workflow_video_lora_sampler_73
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.881222
common_nodes: [CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, SimpleMath+, easy int]
members: [视频生成/图生视频/1993142430524440578.json, 视频生成/图生视频/1994312738337914882.json, 视频生成/图生视频/1996499644534366210.json, 视频生成/图生视频/2011412752325152769.json, 视频生成/图生视频/2012112616382009345.json, 视频生成/图生视频/1967820040437399554.json, 视频生成/图生视频/2053672042368643074.json, 视频生成/图生视频/2055116157123874818.json, 视频生成/图生视频/产品360度旋转展示电商工作流_2104518822836396034.json, 视频生成/图生视频/产品360度旋转展示电商工作流_2104568082445455362.json, 视频生成/图生视频/2002715305803673601.json, 视频生成/图生视频/2051581112060792834.json, 视频生成/图生视频/产品360度旋转工作流_2089693661624889346.json, 视频生成/图生视频/1961871235888168961.json, 视频生成/图生视频/2018213623105064961.json, 视频生成/图生视频/1962385933666488322.json, 视频生成/文生视频/1973229498395136001.json, 视频生成/文生视频/API - Wan2.2 文生视频_2066912966418722817.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_73

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/1993142430524440578.json、视频生成/图生视频/1994312738337914882.json、视频生成/图生视频/1996499644534366210.json、视频生成/图生视频/2011412752325152769.json、视频生成/图生视频/2012112616382009345.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 18 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 17/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 17/18 个有
- `LoadImage` —— 17/18 个有
- `SimpleMath+` —— 17/18 个有
- `WanVideoImageToVideoEncode` —— 17/18 个有
- `GetImageSizeAndCount` —— 16/18 个有
- `JWInteger` —— 16/18 个有
- `WanVideoLoraSelectMulti` —— 12/18 个有
- `ImageUpscaleWithModel` —— 11/18 个有
- `UpscaleModelLoader` —— 11/18 个有
- `JjkText` —— 9/18 个有
- `WanVideoLoraSelect` —— 5/18 个有
- `INTConstant` —— 4/18 个有
- `MathExpression|pysssss` —— 3/18 个有
- `easy int` —— 3/18 个有
- `Anything Everywhere` —— 2/18 个有
- `WanVideoTorchCompileSettings` —— 2/18 个有
- `RHHiddenNodes` —— 1/18 个有
- `Text _O` —— 1/18 个有
- `WanVideoEmptyEmbeds` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、MathExpression|pysssss、SimpleMath+、easy int
