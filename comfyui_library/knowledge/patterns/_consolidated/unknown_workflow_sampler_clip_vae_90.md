---
name: unknown_workflow_sampler_clip_vae_90
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9485
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxPuLIDApplyV2, NunchakuPuLIDLoaderV2, NunchakuTextEncoderLoaderV2, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Nunchaku Pulid参考面部快速一致性人物生成_1990021673283932162.json, 平台全量/nunchaku-flux-krea-pulid_1990700940913250305.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_90

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Nunchaku Pulid参考面部快速一致性人物生成_1990021673283932162.json、平台全量/nunchaku-flux-krea-pulid_1990700940913250305.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxPuLIDApplyV2`
- `NunchakuPuLIDLoaderV2`
- `NunchakuTextEncoderLoaderV2`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有
- `SeedVR2GGUF` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
