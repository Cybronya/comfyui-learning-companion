---
name: unknown_workflow_controlnet_video_lora_29
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8715
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Prompt Text, ControlNetApplySD3, ControlNetLoader, EmptySD3LatentImage, ImageConcanate, ImageFromBatch+, ImageResizeKJ, JWInteger, KSampler, LayerUtility: PurgeVRAM, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveLatent, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy anythingIndexSwitch, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/1965693287438929921.json, 视频生成/图生视频/1965691739010945025.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_29

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1965693287438929921.json、视频生成/图生视频/1965691739010945025.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `EmptySD3LatentImage`
- `ImageConcanate`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `JWInteger`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadWanVideoT5TextEncoder`
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
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 1/2 个有
- `ImageMirror` —— 1/2 个有
- `ImageRepeat` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `VHS_MergeImages` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/2 个有
- `WanVideoUni3C_embeds` —— 1/2 个有
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
