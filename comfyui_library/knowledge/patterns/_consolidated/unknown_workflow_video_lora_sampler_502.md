---
name: unknown_workflow_video_lora_sampler_502
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.91375
common_nodes: [CLIPLoader, CR Prompt Text, CreateCFGScheduleFloatList, Float, INTConstant, JWInteger, LoadWanVideoT5TextEncoder, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Qwen Edit Plus +  全能图片V1 + Wan2.2 制作一个手办然后让他跳舞_1970593449990889473.json, 视频生成/图生视频/Qwen Edit Plus +  全能图片V1 + Wan2.2 生成并欣赏手办_1970558556393119746.json, 视频生成/图生视频/Smooth Mix VS LightX2V I2V 版_2073241002395136001.json, 视频生成/文生视频/Smooth Mix 2.0 VS LightX2V T2V_2073238743884062721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_502

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Qwen Edit Plus +  全能图片V1 + Wan2.2 制作一个手办然后让他跳舞_1970593449990889473.json、视频生成/图生视频/Qwen Edit Plus +  全能图片V1 + Wan2.2 生成并欣赏手办_1970558556393119746.json、视频生成/图生视频/Smooth Mix VS LightX2V I2V 版_2073241002395136001.json、视频生成/文生视频/Smooth Mix 2.0 VS LightX2V T2V_2073238743884062721.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `Float`
- `INTConstant`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `WanVideoImageToVideoEncode` —— 3/4 个有
- `CLIPTextEncode` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `KSampler` —— 2/4 个有
- `KSamplerAdvanced` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `ModelSamplingSD3` —— 2/4 个有
- `RH_LLMAPI_NODE` —— 2/4 个有
- `RH_Nano_Banana_Image2Image` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `Text` —— 2/4 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/4 个有
- `WanImageToVideo` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CLIPVisionEncode` —— 1/4 个有
- `CLIPVisionLoader` —— 1/4 个有
- `WanVideoEmptyEmbeds` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 8 | 4 | 22% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | beta57 | - | 4 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 8，4 个样本，取值分散，一致性仅 22%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 beta57，4 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
