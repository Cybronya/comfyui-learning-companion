---
name: unknown_workflow_video_lora_sampler_147
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.76025
common_nodes: [GetNode, LoadImage, LoadWanVideoT5TextEncoder, SetNode, String Literal, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetRadialAttention, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVAELoader, easy globalSeed, easy seed]
problems: []
missing: [String Literal, easy globalSeed, easy seed, easy float, easy int]
members: [视频生成/图生视频/2001919692862308354.json, 视频生成/图生视频/1979417916649148417.json, 视频生成/图生视频/2019227457009750018.json, 视频生成/图生视频/1981374201879773186.json, 视频生成/文生视频/1973043672696623106.json, 视频生成/文生视频/1978022050193362945.json, 视频生成/文生视频/1978390766324224001.json, 视频生成/文生视频/1978408031887233025.json, 视频生成/文生视频/1978411441667592194.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V4_2072999500995928064.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5+lynx_2072999497908920320.json, 视频生成/文生视频/Wan2.2文生视频性价比极致加速V5+lynx_2072999499213348864.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_147

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/2001919692862308354.json、视频生成/图生视频/1979417916649148417.json、视频生成/图生视频/2019227457009750018.json、视频生成/图生视频/1981374201879773186.json、视频生成/文生视频/1973043672696623106.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：76%

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
- `WanVideoTorchCompileSettings` —— 11/12 个有
- `ImageResizeKJv2` —— 10/12 个有
- `Int` —— 10/12 个有
- `PreviewImage` —— 10/12 个有
- `WanVideoImageToVideoEncode` —— 10/12 个有
- `easy showAnything` —— 10/12 个有
- `LoadLynxResampler` —— 9/12 个有
- `LynxEncodeFaceIP` —— 9/12 个有
- `LynxInsightFaceCrop` —— 9/12 个有
- `RH_Captioner` —— 9/12 个有
- `WanVideoAddLynxEmbeds` —— 9/12 个有
- `WanVideoExtraModelSelect` —— 9/12 个有
- `WanVideoTextEncodeCached` —— 9/12 个有
- `WanVideoEmptyEmbeds` —— 2/12 个有
- `WanVideoVACEEncode` —— 2/12 个有
- `WanVideoVACEModelSelect` —— 2/12 个有
- `easy float` —— 2/12 个有
- `easy int` —— 2/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：String Literal、easy globalSeed、easy seed、easy float、easy int
