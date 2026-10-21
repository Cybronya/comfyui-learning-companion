---
name: unknown_workflow_upscale_lora_sampler_33
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5625
common_nodes: [AILab_QwenVL, BasicGuider, BasicScheduler, CLIPTextEncode, ConditioningZeroOut, DetailDaemonSamplerNode, DualCLIPLoader, FluxGuidance, GetNode, ImageSmartSharpen+, InjectLatentNoise+, KSamplerSelect, LatentPixelScale, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoaderV2, RandomNoise, RebatchLatents, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Text, CR Text Concatenate, ImageSmartSharpen+, LayerUtility: ImageScaleByAspectRatio V2, InjectLatentNoise+, CR Aspect Ratio, LayerUtility: TextJoin]
members: [图片生成/文生图/1914029963945934850.json, 图片生成/文生图/1928883725826953218.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_33

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1914029963945934850.json、图片生成/文生图/1928883725826953218.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `ImageSmartSharpen+`
- `InjectLatentNoise+`
- `KSamplerSelect`
- `LatentPixelScale`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoaderV2`
- `RandomNoise`
- `RebatchLatents`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `CR Aspect Ratio` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `EnhanceDetail` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: TextJoin` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `StyleModelApply` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有
- `Text` —— 1/2 个有
- `VAEEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、ImageSmartSharpen+、LayerUtility: ImageScaleByAspectRatio V2、InjectLatentNoise+
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
