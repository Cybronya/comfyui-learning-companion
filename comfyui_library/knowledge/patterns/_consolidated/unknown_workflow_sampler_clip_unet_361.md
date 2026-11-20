---
name: unknown_workflow_sampler_clip_unet_361
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.95175
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Kontext 多图融合_1952011457573629953.json, 平台全量/CG迷-kontext手动设置宽高换装工作流_1938594591647916033.json, 平台全量/Kontext 单图-万能改图去水印改风格抠图万能集合提示词改即可_1954738880698302465.json, 平台全量/Kontext 单图转换正交等距视图_1946109217210068994.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_361

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Kontext 多图融合_1952011457573629953.json、平台全量/CG迷-kontext手动设置宽高换装工作流_1938594591647916033.json、平台全量/Kontext 单图-万能改图去水印改风格抠图万能集合提示词改即可_1954738880698302465.json、平台全量/Kontext 单图转换正交等距视图_1946109217210068994.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 3/4 个有
- `FluxResolutionNode` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `ImageStitch` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `LayerMask: BenUltra` —— 1/4 个有
- `LayerMask: LoadBenModel` —— 1/4 个有
- `LayerUtility: ImageScaleRestore` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `RBGImageStitchPlus` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1280 | 1280 - 1280 | 3 | 100% |
| LoRA 模型强度 | 0.85 | - | 1 | 100% |
| LoRA 文本强度 | 0.85 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
