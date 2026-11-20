---
name: unknown_workflow_controlnet_ipadapter_lora_2
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.808
common_nodes: [AIO_Preprocessor, ControlNetApplyAdvanced, DualCLIPLoader, EmptyLatentImage, Image Comparer (rgthree), KSampler, LayerUtility: GetImageSize, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, MZ_ChatGLM3Loader, MZ_ChatGLM3_V2, MZ_IPAdapterAdvancedKolors, MZ_IPAdapterModelLoaderKolors, MZ_KolorsCLIPVisionLoader, MZ_KolorsControlNetLoader, MZ_KolorsUNETLoaderV2, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/动漫画风迁移_1944739173305864193.json, 平台全量/动漫画风迁移_1977339279456247810.json, 平台全量/动漫画风迁移_2037413427727044610.json, 视频生成/图生视频/动漫画风迁移_2011331952636338177.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_lora_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/动漫画风迁移_1944739173305864193.json、平台全量/动漫画风迁移_1977339279456247810.json、平台全量/动漫画风迁移_2037413427727044610.json、视频生成/图生视频/动漫画风迁移_2011331952636338177.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `ControlNetApplyAdvanced`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: GetImageSize`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `MZ_ChatGLM3Loader`
- `MZ_ChatGLM3_V2`
- `MZ_IPAdapterAdvancedKolors`
- `MZ_IPAdapterModelLoaderKolors`
- `MZ_KolorsCLIPVisionLoader`
- `MZ_KolorsControlNetLoader`
- `MZ_KolorsUNETLoaderV2`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 4 | 100% |
| LoRA 文本强度 | 0.8 | 0.8 - 0.8 | 4 | 100% |
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 0.8 | 0.8 - 0.8 | 4 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 4 | 100% |
| 高度 | 1448 | 1448 - 1448 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.8，观测区间 0.8 - 0.8，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，观测区间 0.8 - 0.8，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1448，观测区间 1448 - 1448，4 个样本，取值集中（一致性 100%）
