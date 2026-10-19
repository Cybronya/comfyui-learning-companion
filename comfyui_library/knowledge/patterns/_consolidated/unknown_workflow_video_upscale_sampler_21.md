---
name: unknown_workflow_video_upscale_sampler_21
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.912
common_nodes: [ApplyFBCacheOnModel, BasicGuider, BasicScheduler, CLIPVisionEncode, CLIPVisionLoader, CR Text, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, HunyuanImageToVideo, ImageUpscaleWithModel, KSamplerSelect, LTXVPromptEnhancer, LTXVPromptEnhancerLoader, LoadImage, ModelSamplingSD3, Note Plus (mtb), RandomNoise, SaveWEBM, ShowText|pysssss, TeaCacheHunyuanVideoSampler_FOK, TextEncodeHunyuanVideo_ImageToVideo, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/1901022708078125058.json, 视频生成/图生视频/1898150330008588290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_21

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1901022708078125058.json、视频生成/图生视频/1898150330008588290.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `BasicGuider`
- `BasicScheduler`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `HunyuanImageToVideo`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LTXVPromptEnhancer`
- `LTXVPromptEnhancerLoader`
- `LoadImage`
- `ModelSamplingSD3`
- `Note Plus (mtb)`
- `RandomNoise`
- `SaveWEBM`
- `ShowText|pysssss`
- `TeaCacheHunyuanVideoSampler_FOK`
- `TextEncodeHunyuanVideo_ImageToVideo`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LTXVApplySTG` —— 1/2 个有
- `LTXVConditioning` —— 1/2 个有
- `LTXVImgToVideo` —— 1/2 个有
- `LTXVScheduler` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `SamplerCustom` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有
- `TeaCache` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `WanVideoTeaCacheKJ` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 1 | 100% |
| 采样算法 | uni_pc | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 1/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 高发问题（1/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
