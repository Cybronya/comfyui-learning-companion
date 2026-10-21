---
name: unknown_workflow_video_lora_sampler_70
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.970444
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1983525120713138178.json, 视频生成/图生视频/1983529460303601666.json, 视频生成/图生视频/1992060788846252034.json, 视频生成/图生视频/1963555388825358337.json, 视频生成/图生视频/2027622896310427649.json, 视频生成/图生视频/1981195312264110081.json, 视频生成/图生视频/1992174428303806466.json, 视频生成/图生视频/2019656861171060738.json, 视频生成/图生视频/1998010318326497281.json, 视频生成/图生视频/2000475113990520833.json, 视频生成/图生视频/2026893415455133697.json, 视频生成/图生视频/2018932205057216513.json, 视频生成/图生视频/2018481658378330113.json, 视频生成/图生视频/2025740661340774402.json, 视频生成/图生视频/1971037021902905346.json, 视频生成/图生视频/1976556715808264194.json, 视频生成/图生视频/2041413117292318723.json, 视频生成/图生视频/2065457354044436482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_70

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/1983525120713138178.json、视频生成/图生视频/1983529460303601666.json、视频生成/图生视频/1992060788846252034.json、视频生成/图生视频/1963555388825358337.json、视频生成/图生视频/2027622896310427649.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 18 个 workflow 都包含：
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
- `INTConstant` —— 17/18 个有
- `ImageResize+` —— 17/18 个有
- `JWInteger` —— 17/18 个有
- `LayerUtility: PurgeVRAM` —— 17/18 个有
- `LoadWanVideoClipTextEncoder` —— 17/18 个有
- `SimpleMath+` —— 17/18 个有
- `WanVideoClipVisionEncode` —— 17/18 个有
- `easy cleanGpuUsed` —— 17/18 个有
- `CR Prompt Text` —— 16/18 个有
- `CreateCFGScheduleFloatList` —— 16/18 个有
- `LoadImage` —— 16/18 个有
- `ColorMatch` —— 9/18 个有
- `WanVideoSLG` —— 9/18 个有
- `Float` —— 8/18 个有
- `RIFE VFI` —— 6/18 个有
- `DF_Int_to_Float` —— 3/18 个有
- `ImageLoader` —— 2/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/18 个有
- `MultiplePathsInput` —— 2/18 个有
- `Qwen3_VQA` —— 2/18 个有
- `easy showAnything` —— 2/18 个有
- `Int` —— 1/18 个有
- `Label (rgthree)` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
