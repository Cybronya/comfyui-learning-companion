---
name: unknown_workflow_controlnet_ipadapter_lora_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.722
common_nodes: [ACN_AdvancedControlNetApply, AnyLinePreprocessor, BNK_CLIPTextEncodeAdvanced, CR Prompt Text, CR Text Replace, CheckpointLoaderSimple, ControlNetLoaderAdvanced, DownloadAndLoadFlorence2Model, EmptyLatentImage, Fast Groups Bypasser (rgthree), Florence2Run, GetNode, GoogleTranslateTextNode, IPAdapterAdvanced, IPAdapterUnifiedLoader, JWImageResizeByLongerSide, KSamplerAdvanced //Inspire, LoadImage, Lora Loader Stack (rgthree), PreviewImage, SDXLPromptStyler, SaveImage, ScaledSoftControlNetWeights, SetNode, ShowText|pysssss, Text Concatenate, VAEDecode, VAELoader, easy getNode, easy imageSize, easy seed, easy setNode]
problems: []
missing: []
members: [图片生成/图生图/建筑草图生成效果图S2I_1898741346922876929.json, 图片生成/图生图/旧房改造_1980467289382412289.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_lora_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/建筑草图生成效果图S2I_1898741346922876929.json、图片生成/图生图/旧房改造_1980467289382412289.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_AdvancedControlNetApply`
- `AnyLinePreprocessor`
- `BNK_CLIPTextEncodeAdvanced`
- `CR Prompt Text`
- `CR Text Replace`
- `CheckpointLoaderSimple`
- `ControlNetLoaderAdvanced`
- `DownloadAndLoadFlorence2Model`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `GetNode`
- `GoogleTranslateTextNode`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `JWImageResizeByLongerSide`
- `KSamplerAdvanced //Inspire`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `PreviewImage`
- `SDXLPromptStyler`
- `SaveImage`
- `ScaledSoftControlNetWeights`
- `SetNode`
- `ShowText|pysssss`
- `Text Concatenate`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy imageSize`
- `easy seed`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral_cfg_pp | - | 2 | 100% |
| 重绘幅度 | AYS SDXL | - | 2 | 100% |
| ControlNet 权重 | 0.5 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral_cfg_pp，2 个样本，一致性 100%
- 重绘幅度 最常用 AYS SDXL，2 个样本，一致性 100%
- ControlNet 权重 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
