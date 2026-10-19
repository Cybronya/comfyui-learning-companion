---
name: unknown_workflow_video_sampler_vae_12
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.76295
common_nodes: [CR Text, ImpactSwitch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, SetNode, Text Concatenate, VHS_VideoCombine, Wan22PromptSelector, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1982787419013558274.json, 视频生成/图生视频/1980177122574635010.json, 视频生成/图生视频/1984097038935752706.json, 视频生成/图生视频/1984151178600742913.json, 视频生成/图生视频/1972860649577598978.json, 视频生成/图生视频/1981513970995609601.json, 视频生成/图生视频/2031711000294068225.json, 视频生成/图生视频/1954097767838838785.json, 视频生成/图生视频/1953607536056389634.json, 视频生成/图生视频/1951650390871887873.json, 视频生成/图生视频/1971957035292160001.json, 视频生成/图生视频/1972913233726230530.json, 视频生成/图生视频/1982270135106977794.json, 视频生成/图生视频/1993575888398860290.json, 视频生成/图生视频/1988496401766203394.json, 视频生成/图生视频/1980267588691386370.json, 视频生成/图生视频/1997289089927954433.json, 视频生成/图生视频/2039624462835916801.json, 视频生成/图生视频/2041677614804373505.json, 视频生成/图生视频/2032756294041477121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_12

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/1982787419013558274.json、视频生成/图生视频/1980177122574635010.json、视频生成/图生视频/1984097038935752706.json、视频生成/图生视频/1984151178600742913.json、视频生成/图生视频/1972860649577598978.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 20 个 workflow 都包含：
- `CR Text`
- `ImpactSwitch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `SetNode`
- `Text Concatenate`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 19/20 个有
- `WanVideoTextEncode` —— 19/20 个有
- `CreateCFGScheduleFloatList` —— 18/20 个有
- `INTConstant` —— 17/20 个有
- `GetImageSizeAndCount` —— 16/20 个有
- `RIFE VFI` —— 16/20 个有
- `RH_LLMAPI_NODE` —— 13/20 个有
- `ShowText|pysssss` —— 13/20 个有
- `WanVideoBlockSwap` —— 13/20 个有
- `WanVideoModelLoader` —— 13/20 个有
- `WanVideoTorchCompileSettings` —— 13/20 个有
- `easy showAnything` —— 13/20 个有
- `WanVideoSetLoRAs` —— 12/20 个有
- `WanVideoLoraSelectMulti` —— 10/20 个有
- `Fast Groups Bypasser (rgthree)` —— 8/20 个有
- `LayerUtility: PurgeVRAM V2` —— 7/20 个有
- `PreviewImage` —— 7/20 个有
- `PrimitiveFloat` —— 7/20 个有
- `RHHiddenNodes` —— 7/20 个有
- `RH_Nano_Banana_Image2Image` —— 7/20 个有
- `WanVideoLoraSelect` —— 4/20 个有
- `Primitive integer [Crystools]` —— 3/20 个有
- `FloatToSigmas` —— 2/20 个有
- `StringToFloatList` —— 2/20 个有
- `easy cleanGpuUsed` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
