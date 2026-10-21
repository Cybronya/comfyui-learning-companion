---
name: unknown_workflow_video_lora_sampler_713
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.912
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Prompt Text, CreateCFGScheduleFloatList, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, INTConstant, ImageResize+, JWInteger, KSamplerSelect, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, LoraLoader, RH_Translator, RandomNoise, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: [LayerUtility: PurgeVRAM, SimpleMath+, easy cleanGpuUsed, CR Prompt Text, ImageResize+]
members: [图片生成/文生图/1970871370110377986.json, 视频生成/图生视频/1970871370110377986.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_713

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1970871370110377986.json、视频生成/图生视频/1970871370110377986.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `INTConstant`
- `ImageResize+`
- `JWInteger`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `LoraLoader`
- `RH_Translator`
- `RandomNoise`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| LoRA 模型强度 | 0.6 | - | 2 | 100% |
| LoRA 文本强度 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、SimpleMath+、easy cleanGpuUsed、CR Prompt Text、ImageResize+
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
