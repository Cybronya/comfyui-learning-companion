---
name: unknown_workflow_upscale_lora_sampler_72
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.633667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ConditioningZeroOut, DetailDaemonSamplerNode, DualCLIPLoader, FluxGuidance, GetNode, ImageSmartSharpen+, InjectLatentNoise+, KSamplerSelect, LatentPixelScale, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoaderV2, RandomNoise, RebatchLatents, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/🈚️flux.1 nunchakun i2i-基础图生图_洗图-4bit加速_1929169338916356098.json, 图片生成/文生图/🈚️flux.1 nunchakun-基础 文生图-4bit加速文生图_1928883725826953218.json, 图片生成/文生图/😯Flux.1 nunchaku+Redux 图片参考 图生图_垫图_洗图_1914029963945934850.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_72

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/🈚️flux.1 nunchakun i2i-基础图生图_洗图-4bit加速_1929169338916356098.json、图片生成/文生图/🈚️flux.1 nunchakun-基础 文生图-4bit加速文生图_1928883725826953218.json、图片生成/文生图/😯Flux.1 nunchaku+Redux 图片参考 图生图_垫图_洗图_1914029963945934850.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
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
- `AILab_QwenVL` —— 2/3 个有
- `CR Text` —— 2/3 个有
- `CR Text Concatenate` —— 2/3 个有
- `EnhanceDetail` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `RepeatLatentBatch` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `CLIPVisionEncode` —— 1/3 个有
- `CLIPVisionLoader` —— 1/3 个有
- `CR Aspect Ratio` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `JanusImage2Text` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有
- `LoadJanusModel` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `StyleModelApply` —— 1/3 个有
- `StyleModelLoader` —— 1/3 个有
- `Text` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
