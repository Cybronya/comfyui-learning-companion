---
name: unknown_workflow_controlnet_video_lora_28
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.826
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Prompt Text, ControlNetApplySD3, ControlNetLoader, EmptySD3LatentImage, INTConstant, ImageConcanate, ImageConcatMulti, ImageFromBatch+, ImageResizeKJv2, JWInteger, KSampler, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveLatent, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy anythingIndexSwitch, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1966695132777099266.json, 视频生成/图生视频/1965695977791344642.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1966695132777099266.json、视频生成/图生视频/1965695977791344642.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `INTConstant`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `JWInteger`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveLatent`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `Float` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadWanVideoT5TextEncoder` —— 1/2 个有
- `PDIMAGE_LongerSize` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `StringToFloatList` —— 1/2 个有
- `WanVideoAddControlEmbeds` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoLoraSelectMulti` —— 1/2 个有
- `WanVideoScheduler` —— 1/2 个有
- `WanVideoSigmaToStep` —— 1/2 个有
- `WanVideoTextEmbedBridge` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoTextEncodeCached` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `WanVideoVACEEncode` —— 1/2 个有
- `WanVideoVACEModelSelect` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| 采样步数 | 15 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 15，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
