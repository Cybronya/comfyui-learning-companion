---
name: image_to_image_video_lora_sampler_20
type: Image To Image
frequency: 2
level: weak
coverage: 0.9815
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, DF_Get_image_size, DualCLIPLoader, FluxGuidance, ImageFromBatch+, KSampler, LayerUtility: ImageBlendAdvance, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, ModelSamplingSD3, OpenposePreprocessor, RH_Translator, RMBG, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/可爱玩偶小人动作同步_1951314559233675266.json, 视频生成/图生视频/可爱玩偶小人动作同步（Wan2.2版）_1951653280789286913.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/可爱玩偶小人动作同步_1951314559233675266.json、视频生成/图生视频/可爱玩偶小人动作同步（Wan2.2版）_1951653280789286913.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `DF_Get_image_size`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageFromBatch+`
- `KSampler`
- `LayerUtility: ImageBlendAdvance`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `OpenposePreprocessor`
- `RH_Translator`
- `RMBG`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 10.5 | - | 2 | 10% |
| 采样算法 | 3.5 | - | 1 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 10.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 10%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
