---
name: unknown_workflow_lora_sampler_vae_26
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9025
common_nodes: [CR Prompt Text, DownloadAndLoadHyVideoTextEncoder, GetImageSizeAndCount, HyVideoBlockSwap, HyVideoEncode, HyVideoEnhanceAVideo, HyVideoI2VEncode, HyVideoLoraSelect, HyVideoModelLoader, HyVideoSampler, HyVideoTeaCache, HyVideoVAELoader, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, Note _O, SaveImage, SaveLatent]
problems: []
missing: []
members: [图片生成/图生图/混元--图生视频--保存latent版_1912332210211385345.json, 视频生成/图生视频/（自用）混元一致性修复图生视频Latent工作流_1911249083103703042.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_26

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/混元--图生视频--保存latent版_1912332210211385345.json、视频生成/图生视频/（自用）混元一致性修复图生视频Latent工作流_1911249083103703042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `DownloadAndLoadHyVideoTextEncoder`
- `GetImageSizeAndCount`
- `HyVideoBlockSwap`
- `HyVideoEncode`
- `HyVideoEnhanceAVideo`
- `HyVideoI2VEncode`
- `HyVideoLoraSelect`
- `HyVideoModelLoader`
- `HyVideoSampler`
- `HyVideoTeaCache`
- `HyVideoVAELoader`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Note _O`
- `SaveImage`
- `SaveLatent`

**可变部分**（部分 workflow 才有）：
- `HyVideoDecode` —— 1/2 个有
- `LoadLatent` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
