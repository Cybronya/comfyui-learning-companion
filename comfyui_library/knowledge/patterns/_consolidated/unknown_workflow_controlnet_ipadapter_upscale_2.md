---
name: unknown_workflow_controlnet_ipadapter_upscale_2
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.650333
common_nodes: [AIO_Preprocessor, Any Switch (rgthree), CLIPTextEncode, CLIPVisionLoader, CR Text, CR Text Concatenate, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, CoreMLDetailerHookProvider, DownloadAndLoadFlorence2Model, FaceDetailer, Fast Groups Bypasser (rgthree), Florence2Run, GetNode, IPAdapterAdvanced, IPAdapterModelLoader, IPAdapterNoise, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, MaskPreview+, MediaPipeFaceMeshDetectorProvider //Inspire, PreviewImage, RHHiddenNodes, RH_Translator, SAMLoader, SDXLEmptyLatentSizePicker+, SaveImage, SetNode, ShowText|pysssss, StringFunction|pysssss, UltimateSDUpscale, UltralyticsDetectorProvider, UpscaleModelLoader, VAEDecode, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/SDXL 动漫角色设计图 上色优化工作流 面部修复 二次放大_2048465481165709314.json, 图片生成/图生图/SDXL 动漫角色设计图 上色优化工作流 面部修复 二次放大_2061282081497501697.json, 图片生成/图生图/SDXL+动漫角色设计图+上色优化工作流+面部修复+二次放大_2057627831169015809.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_upscale_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SDXL 动漫角色设计图 上色优化工作流 面部修复 二次放大_2048465481165709314.json、图片生成/图生图/SDXL 动漫角色设计图 上色优化工作流 面部修复 二次放大_2061282081497501697.json、图片生成/图生图/SDXL+动漫角色设计图+上色优化工作流+面部修复+二次放大_2057627831169015809.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CoreMLDetailerHookProvider`
- `DownloadAndLoadFlorence2Model`
- `FaceDetailer`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `GetNode`
- `IPAdapterAdvanced`
- `IPAdapterModelLoader`
- `IPAdapterNoise`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `MaskPreview+`
- `MediaPipeFaceMeshDetectorProvider //Inspire`
- `PreviewImage`
- `RHHiddenNodes`
- `RH_Translator`
- `SAMLoader`
- `SDXLEmptyLatentSizePicker+`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `UltimateSDUpscale`
- `UltralyticsDetectorProvider`
- `UpscaleModelLoader`
- `VAEDecode`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.35 | 0.35 - 0.35 | 3 | 100% |
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 768x1280 (0.6) | - | 3 | 100% |
| 高度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.7 | 0.7 - 0.7 | 3 | 100% |
| LoRA 文本强度 | 0.7 | 0.7 - 0.7 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.35，观测区间 0.35 - 0.35，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 最常用 768x1280 (0.6)，3 个样本，一致性 100%
- 高度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
