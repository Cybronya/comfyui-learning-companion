---
name: unknown_workflow_video_lora_sampler_360
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.888833
common_nodes: [CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1950805737444417537.json, 视频生成/图生视频/1984649451941806082.json, 视频生成/图生视频/1984646206687232002.json, 视频生成/图生视频/1970593449990889473.json, 视频生成/图生视频/1970558556393119746.json, 视频生成/图生视频/1982131363547619329.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_360

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1950805737444417537.json、视频生成/图生视频/1984649451941806082.json、视频生成/图生视频/1984646206687232002.json、视频生成/图生视频/1970593449990889473.json、视频生成/图生视频/1970558556393119746.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
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
- `Float` —— 5/6 个有
- `GetImageSizeAndCount` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `JWInteger` —— 5/6 个有
- `WanVideoScheduler` —— 5/6 个有
- `WanVideoSigmaToStep` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `LayerUtility: PurgeVRAM` —— 4/6 个有
- `RH_LLMAPI_NODE` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `AILab_QwenVL` —— 2/6 个有
- `CLIPLoader` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `KSampler` —— 2/6 个有
- `RH_Nano_Banana_Image2Image` —— 2/6 个有
- `RH_Translator` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `Text` —— 2/6 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/6 个有
- `UNETLoader` —— 2/6 个有
- `VAEDecode` —— 2/6 个有
- `VAELoader` —— 2/6 个有
- `ImageFromBatch+` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta57 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta57，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
