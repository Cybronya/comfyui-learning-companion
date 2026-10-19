---
name: unknown_workflow_video_lora_sampler_48
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.952333
common_nodes: [INTConstant, ImageResize+, JWInteger, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2016405301691420673.json, 视频生成/图生视频/2049487704492085249.json, 视频生成/图生视频/课件25：WAN2.2首尾帧视频工作流（开源）_2103640919990951938.json, 视频生成/图生视频/2021050024263684097.json, 视频生成/图生视频/2033052828255657985.json, 视频生成/图生视频/1993144269496057857.json, 视频生成/图生视频/2011275998205054977.json, 视频生成/图生视频/2013608630863536130.json, 视频生成/图生视频/2014220447117746178.json, 视频生成/图生视频/2020055419988746242.json, 视频生成/图生视频/2054450000423333890.json, 视频生成/图生视频/2068009866219835393.json, 视频生成/图生视频/2063448324002373634.json, 视频生成/图生视频/2037500087261208578.json, 视频生成/图生视频/1983929785862782977.json, 视频生成/图生视频/1967833229766045698.json, 视频生成/图生视频/1983506063989350402.json, 视频生成/图生视频/1984560751979479042.json, 视频生成/图生视频/1975787669600997377.json, 视频生成/图生视频/1976838603810787330.json, 视频生成/图生视频/2007622545448640513.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_48

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/2016405301691420673.json、视频生成/图生视频/2049487704492085249.json、视频生成/图生视频/课件25：WAN2.2首尾帧视频工作流（开源）_2103640919990951938.json、视频生成/图生视频/2021050024263684097.json、视频生成/图生视频/2033052828255657985.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 21 个 workflow 都包含：
- `INTConstant`
- `ImageResize+`
- `JWInteger`
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
- `LayerUtility: PurgeVRAM` —— 20/21 个有
- `WanVideoDecode` —— 20/21 个有
- `WanVideoImageToVideoEncode` —— 20/21 个有
- `CreateCFGScheduleFloatList` —— 11/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/21 个有
- `LoadImage` —— 11/21 个有
- `SimpleMath+` —— 11/21 个有
- `CR Prompt Text` —— 10/21 个有
- `ImageLoader` —— 10/21 个有
- `easy cleanGpuUsed` —— 10/21 个有
- `GetNode` —— 8/21 个有
- `SetNode` —— 8/21 个有
- `DF_Int_to_Float` —— 5/21 个有
- `Bjornulf_ShowFloat` —— 1/21 个有
- `CR SDXL Aspect Ratio` —— 1/21 个有
- `Fast Groups Bypasser (rgthree)` —— 1/21 个有
- `MuyeTextEditOutput` —— 1/21 个有
- `PrimitiveInt` —— 1/21 个有
- `PrimitiveStringMultiline` —— 1/21 个有
- `RHHiddenNodes` —— 1/21 个有
- `RIFE VFI` —— 1/21 个有
- `SaveImage` —— 1/21 个有
- `TT_img_enc_v2` —— 1/21 个有
- `WanVideoLoraSelectMulti` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
