---
name: unknown_workflow_sampler_clip_vae_26
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.705
common_nodes: [Anything Everywhere, BasicGuider, BasicScheduler, CLIPTextEncode, CM_IntToBool, CR Text, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxResolutionNode, Image Comparer (rgthree), ImageResize+, ImpactConditionalBranch, Int, KSamplerSelect, LoadImage, MathExpression|pysssss, ModelSamplingFlux, NunchakuFluxDiTLoader, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/100种不同风格图片转绘-加速稳定版_2022624756767399937.json, 图片生成/图生图/Flux 破损黑白照片修复上色_1948974283469594626.json, 图片生成/图生图/Kontext Dev 一键去图片水印_1945730379670233089.json, 图片生成/图生图/Kontext Dev 简易一键去图片水印_1946786876764381186.json, 图片生成/图生图/Kontext dev 动漫角色一致性_1943214888284282882.json, 图片生成/图生图/Kontext dev 去除水印_1947229755512934402.json, 图片生成/图生图/【老照片顶级修复V3】Flux-Kontext-Dev（plus-48G版）_1938603945344294913.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_26

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/100种不同风格图片转绘-加速稳定版_2022624756767399937.json、图片生成/图生图/Flux 破损黑白照片修复上色_1948974283469594626.json、图片生成/图生图/Kontext Dev 一键去图片水印_1945730379670233089.json、图片生成/图生图/Kontext Dev 简易一键去图片水印_1946786876764381186.json、图片生成/图生图/Kontext dev 动漫角色一致性_1943214888284282882.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 7 个 workflow 都包含：
- `Anything Everywhere`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CM_IntToBool`
- `CR Text`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxResolutionNode`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImpactConditionalBranch`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_Translator` —— 4/7 个有
- `GetNode` —— 3/7 个有
- `RHHiddenNodes` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `AIO_Preprocessor` —— 2/7 个有
- `ApplyInstantID` —— 2/7 个有
- `CFGGuider` —— 2/7 个有
- `CheckpointLoader|pysssss` —— 2/7 个有
- `ControlNetApplySD3` —— 2/7 个有
- `ControlNetLoader` —— 2/7 个有
- `Float` —— 2/7 个有
- `InstantIDFaceAnalysis` —— 2/7 个有
- `InstantIDModelLoader` —— 2/7 个有
- `LoraLoader|pysssss` —— 2/7 个有
- `SetUnionControlNetType` —— 2/7 个有
- `easy imageConcat` —— 2/7 个有
- `CR Text Concatenate` —— 1/7 个有
- `ColorCorrectOfUtils` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `SeedVR2` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 7 | 100% |
| 高度 | 512 | 512 - 512 | 7 | 100% |
| LoRA 模型强度 | 0.5 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.2 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
