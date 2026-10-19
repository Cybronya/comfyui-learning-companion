---
name: unknown_workflow_video_lora_sampler_50
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.89985
common_nodes: [CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1973229498395136001.json, 视频生成/图生视频/1958323802964967425.json, 视频生成/图生视频/1962130657587695617.json, 视频生成/图生视频/1990675353976922114.json, 视频生成/图生视频/1963496019524816898.json, 视频生成/图生视频/1960986981260038145.json, 视频生成/图生视频/1956914143121039362.json, 视频生成/图生视频/1991827663358849025.json, 视频生成/图生视频/1993179574894788609.json, 视频生成/图生视频/2064953118089113601.json, 视频生成/图生视频/1986361069599916033.json, 视频生成/图生视频/2007643731159162882.json, 视频生成/图生视频/1980795448254484481.json, 视频生成/图生视频/1955015931215822850.json, 视频生成/图生视频/1955449911829565441.json, 视频生成/图生视频/1950571192820420609.json, 视频生成/图生视频/1955912718601650177.json, 视频生成/图生视频/1957829417538088962.json, 视频生成/图生视频/1953992101455548418.json, 视频生成/图生视频/1973675102011305986.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_50

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/1973229498395136001.json、视频生成/图生视频/1958323802964967425.json、视频生成/图生视频/1962130657587695617.json、视频生成/图生视频/1990675353976922114.json、视频生成/图生视频/1963496019524816898.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 20 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
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
- `INTConstant` —— 19/20 个有
- `DF_Integer` —— 18/20 个有
- `GetImageSizeAndCount` —— 18/20 个有
- `MathExpression|pysssss` —— 18/20 个有
- `SimpleMath+` —— 18/20 个有
- `JWInteger` —— 17/20 个有
- `easy int` —— 17/20 个有
- `JjkText` —— 11/20 个有
- `WanVideoTorchCompileSettings` —— 8/20 个有
- `RH_Captioner` —— 7/20 个有
- `RH_Translator` —— 7/20 个有
- `Text Multiline` —— 7/20 个有
- `PrimitiveBoolean` —— 6/20 个有
- `RH_LLMAPI_NODE` —— 6/20 个有
- `ShowText|pysssss` —— 6/20 个有
- `easy ifElse` —— 6/20 个有
- `string_util_StrReplace` —— 6/20 个有
- `Fast Groups Bypasser (rgthree)` —— 2/20 个有
- `Anything Everywhere` —— 1/20 个有
- `Display Int (rgthree)` —— 1/20 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/20 个有
- `GIMMVFI_interpolate` —— 1/20 个有
- `ImpactInt` —— 1/20 个有
- `PreviewImage` —— 1/20 个有
- `ShowText` —— 1/20 个有
- `easy batchAnything` —— 1/20 个有
- `easy forLoopEnd` —— 1/20 个有
- `easy forLoopStart` —— 1/20 个有
- `easy imageIndexSwitch` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
