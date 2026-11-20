---
name: unknown_workflow_controlnet_ipadapter_lora
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.908667
common_nodes: [BNK_CLIPTextEncodeAdvanced, BrushNet, BrushNetLoader, CR Latent Batch Size, CheckpointLoaderSimple, ControlNetApplySD3, ControlNetLoader, DepthAnythingV2Preprocessor, Fast Groups Bypasser (rgthree), IPAdapterAdvanced, IPAdapterUnifiedLoader, ImageResizeKJ, InvertMask, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerUtility: PurgeVRAM, LoadImage, LoraLoader, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2002007625766191105.json, 图片生成/图生图/电商产品换背景_XL+cn+IPA参考_1941356267518717953.json, 图片生成/图生图/电商产品换背景丨主卧大床电商产品丨主卧大床_1935169460531568641.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_lora

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2002007625766191105.json、图片生成/图生图/电商产品换背景_XL+cn+IPA参考_1941356267518717953.json、图片生成/图生图/电商产品换背景丨主卧大床电商产品丨主卧大床_1935169460531568641.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `BNK_CLIPTextEncodeAdvanced`
- `BrushNet`
- `BrushNetLoader`
- `CR Latent Batch Size`
- `CheckpointLoaderSimple`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DepthAnythingV2Preprocessor`
- `Fast Groups Bypasser (rgthree)`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `ImageResizeKJ`
- `InvertMask`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoader`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `Text` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 3.5 - 3.8 | 3 | 96% |
| 采样算法 | euler_ancestral | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 0.1 | 0.1 - 0.1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 3.5 - 3.8，3 个样本，取值集中（一致性 96%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.1，观测区间 0.1 - 0.1，3 个样本，取值集中（一致性 100%）
