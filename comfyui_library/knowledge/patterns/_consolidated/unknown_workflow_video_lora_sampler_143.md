---
name: unknown_workflow_video_lora_sampler_143
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.782667
common_nodes: [GetNode, LoadImage, LoadWanVideoT5TextEncoder, SetNode, String Literal, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetRadialAttention, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVAELoader, easy globalSeed, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频增益加速V4_2001919692862308354.json, 视频生成/图生视频/Wan2.2图生视频极致加速V5+lynx_1979417916649148417.json, 视频生成/图生视频/Wan2.2图生视频网感十足_2019227457009750018.json, 视频生成/图生视频/效果拉满V5-1022顶配图生视频_1981374201879773186.json, 视频生成/文生视频/1022对比测试_1981324716671664130.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V3_1973043672696623106.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V4_1978022050193362945.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5+lynx_1978408031887233025.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-1022版_1981325230595629057.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-1030-非人_1984904372494680065.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-moe-人物适用_1978390766324224001.json, 视频生成/文生视频/Wan2.2文生视频性价比极致加速V5+lynx_1978411441667592194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_143

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频增益加速V4_2001919692862308354.json、视频生成/图生视频/Wan2.2图生视频极致加速V5+lynx_1979417916649148417.json、视频生成/图生视频/Wan2.2图生视频网感十足_2019227457009750018.json、视频生成/图生视频/效果拉满V5-1022顶配图生视频_1981374201879773186.json、视频生成/文生视频/1022对比测试_1981324716671664130.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 12 个 workflow 都包含：
- `GetNode`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetRadialAttention`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy globalSeed`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 11/12 个有
- `Int` —— 11/12 个有
- `PreviewImage` —— 11/12 个有
- `WanVideoImageToVideoEncode` —— 11/12 个有
- `WanVideoTorchCompileSettings` —— 11/12 个有
- `easy showAnything` —— 11/12 个有
- `LoadLynxResampler` —— 6/12 个有
- `LynxEncodeFaceIP` —— 6/12 个有
- `LynxInsightFaceCrop` —— 6/12 个有
- `RH_Captioner` —— 6/12 个有
- `WanVideoAddLynxEmbeds` —— 6/12 个有
- `WanVideoExtraModelSelect` —— 6/12 个有
- `WanVideoTextEncodeCached` —— 6/12 个有
- `AddLabel` —— 1/12 个有
- `FloatToSigmas` —— 1/12 个有
- `INTConstant` —— 1/12 个有
- `ImageConcatMulti` —— 1/12 个有
- `StringToFloatList` —— 1/12 个有
- `WanVideoEmptyEmbeds` —— 1/12 个有
- `WanVideoVACEEncode` —— 1/12 个有
- `WanVideoVACEModelSelect` —— 1/12 个有
- `easy float` —— 1/12 个有
- `easy int` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
