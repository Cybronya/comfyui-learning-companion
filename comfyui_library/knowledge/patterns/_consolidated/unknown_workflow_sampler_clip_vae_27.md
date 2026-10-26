---
name: unknown_workflow_sampler_clip_vae_27
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.788857
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/5s出图  仿写小红书美女  FluxRedux+Nunchaku_1916865920277614594.json, 图片生成/图生图/Flex.1 alpha Redux 基础工作流_1908349003488964610.json, 图片生成/图生图/Flex.1-alpha 512 Redux Adapter_1911803573087236098.json, 图片生成/图生图/FluxRedux学习必看  attn类型降低redux影响力_1916475712205950977.json, 图片生成/图生图/学习必看  Redux高阶应用  蒙版区域起作用_1916884651116265473.json, 图片生成/图生图/文生图风格迁移   FluxRedux+条件合并  使得提示词发挥作用_1917400738257895425.json, 图片生成/图生图/最新Redux多图融合  可调节强度_1917413870846017538.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_27

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/5s出图  仿写小红书美女  FluxRedux+Nunchaku_1916865920277614594.json、图片生成/图生图/Flex.1 alpha Redux 基础工作流_1908349003488964610.json、图片生成/图生图/Flex.1-alpha 512 Redux Adapter_1911803573087236098.json、图片生成/图生图/FluxRedux学习必看  attn类型降低redux影响力_1916475712205950977.json、图片生成/图生图/学习必看  Redux高阶应用  蒙版区域起作用_1916884651116265473.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 6/7 个有
- `CLIPVisionLoader` —— 6/7 个有
- `EmptySD3LatentImage` —— 6/7 个有
- `StyleModelApply` —— 6/7 个有
- `GetNode` —— 5/7 个有
- `INTConstant` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `VAELoader` —— 5/7 个有
- `NunchakuFluxDiTLoader` —— 3/7 个有
- `NunchakuFluxLoraLoader` —— 3/7 个有
- `NunchakuTextEncoderLoader` —— 3/7 个有
- `CheckpointLoaderSimple` —— 2/7 个有
- `DualCLIPLoader` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `UNETLoader` —— 2/7 个有
- `AdvancedVisionLoader` —— 1/7 个有
- `ConditioningCombine` —— 1/7 个有
- `LayerMask: MaskPreview` —— 1/7 个有
- `LayerMask: PersonMaskUltra V2` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `ReduxAdvanced` —— 1/7 个有
- `VAEEncode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
