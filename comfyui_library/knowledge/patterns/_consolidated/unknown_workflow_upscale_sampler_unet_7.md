---
name: unknown_workflow_upscale_sampler_unet_7
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.892167
common_nodes: [BasicGuider, CLIPLoader, CR Prompt Text, ComfyMathExpression, CreateVideo, DF_Int_to_Float, EasyCache, Fast Groups Bypasser (rgthree), GetVideoComponents, ImpactSwitch, KSamplerSelect, LTXVConcatAVLatent, LoadAudio, LoadImage, LoadVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowAnything|Mie, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/b25-49混合模型提示词优化反推_2110794014583771137.json, 视频生成/图生视频/h3提示词优化反推加速双采_2097892087424438274.json, 视频生成/图生视频/h3提示词优化反推加速双采_2110570373136871425.json, 视频生成/图生视频/h3提示词优化反推加速双采_2111011900757729281.json, 视频生成/文生视频/h3提示词优化反推加速双采_2097892087424438274.json, 视频生成/文生视频/双采高低采singularity模型加速版vdn高步数-MiniMax H3｜多参图像音频极速生视频_2097862187531456514.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_7

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/b25-49混合模型提示词优化反推_2110794014583771137.json、视频生成/图生视频/h3提示词优化反推加速双采_2097892087424438274.json、视频生成/图生视频/h3提示词优化反推加速双采_2110570373136871425.json、视频生成/图生视频/h3提示词优化反推加速双采_2111011900757729281.json、视频生成/文生视频/h3提示词优化反推加速双采_2097892087424438274.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `CreateVideo`
- `DF_Int_to_Float`
- `EasyCache`
- `Fast Groups Bypasser (rgthree)`
- `GetVideoComponents`
- `ImpactSwitch`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowAnything|Mie`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 5/6 个有
- `DapaoH3LocalPromptNode` —— 5/6 个有
- `DapaoH3PromptBoxNode` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 5/6 个有
- `PreviewAny` —— 5/6 个有
- `SolAttnMiniMax` —— 5/6 个有
- `VAEEncode` —— 5/6 个有
- `VAEEncodeAudio` —— 5/6 个有
- `RandomSeedNoise` —— 4/6 个有
- `SaveAudio` —— 4/6 个有
- `T8_IndexTTS25_EmotionControl` —— 4/6 个有
- `T8_IndexTTS25_Generate` —— 4/6 个有
- `T8_IndexTTS25_ModelLoader` —— 4/6 个有
- `ManualSigmas` —— 2/6 个有
- `GoohaiUniversalSlider` —— 1/6 个有
- `LTXVSeparateAVLatent` —— 1/6 个有
- `Lora Loader Stack (rgthree)` —— 1/6 个有
- `MiniMaxH3SparkAttentionAuto` —— 1/6 个有
- `MinimaxH3LatentUpscaler3D` —— 1/6 个有
- `SplitSigmas` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
