---
name: unknown_workflow_video_upscale_lora_17
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.492667
common_nodes: [CR Text, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetNode, ImageScaleToMegapixels, ImpactControlBridge, ImpactInt, ImpactSwitch, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadJsonFromText, LoadWanVideoT5TextEncoder, RHHiddenNodes, RH_Captioner, RH_LLMAPI_NODE, Seed (rgthree), SetNode, StringFunction|pysssss, UpscaleModelLoader, VHS_VideoCombine, WanVideoApplyNAG, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTextEncodeSingle, WanVideoVAELoader, easy ifElse, easy mathInt, easy negative, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1971101417341652994.json, 视频生成/图生视频/1981765455167791105.json, 视频生成/图生视频/1973100539745538049.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_17

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1971101417341652994.json、视频生成/图生视频/1981765455167791105.json、视频生成/图生视频/1973100539745538049.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Text`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetNode`
- `ImageScaleToMegapixels`
- `ImpactControlBridge`
- `ImpactInt`
- `ImpactSwitch`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadJsonFromText`
- `LoadWanVideoT5TextEncoder`
- `RHHiddenNodes`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `Seed (rgthree)`
- `SetNode`
- `StringFunction|pysssss`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`
- `easy ifElse`
- `easy mathInt`
- `easy negative`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GLM_Vision_ImageToPrompt` —— 2/3 个有
- `ImageCASharpening+` —— 1/3 个有
- `Note Plus (mtb)` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
