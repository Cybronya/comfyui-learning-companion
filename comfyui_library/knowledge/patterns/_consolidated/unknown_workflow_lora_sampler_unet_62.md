---
name: unknown_workflow_lora_sampler_unet_62
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8448
common_nodes: [ConditioningZeroOut, DiptychCreate, DualCLIPLoader, FluxGuidance, ICEFConditioning, ImageCrop, InContextEditInstruction, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/IC+Edit全能图片G4o创成式填充服务端_1921536493649608705.json, 图片生成/图生图/IC-EDIT官方工作流优化版  提示词修改图片_1924492642829463553.json, 图片生成/图生图/ICEdit 工作流_1921046053074698242.json, 图片生成/图生图/ICEdit-MoE 最新图像编辑处理，低显存运行_1923196553685889025.json, 图片生成/图生图/ICEdit官方稳定版（一致性超强，成功率超高）_1920531109803655169.json, 图片生成/图生图/ICEdit官方稳定版（一致性超强，成功率超高）_1920674826652942338.json, 平台全量/ComfyUI In-Context Edit_1921752752244867074.json, 平台全量/ICEdit-MoE图像编辑_1918326947334520834.json, 平台全量/ICEdit图像编辑工作流_1921021423777677313.json, 平台全量/一句话编辑图片 免费全能图片G4o icedit_1923312039849021442.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_62

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/IC+Edit全能图片G4o创成式填充服务端_1921536493649608705.json、图片生成/图生图/IC-EDIT官方工作流优化版  提示词修改图片_1924492642829463553.json、图片生成/图生图/ICEdit 工作流_1921046053074698242.json、图片生成/图生图/ICEdit-MoE 最新图像编辑处理，低显存运行_1923196553685889025.json、图片生成/图生图/ICEdit官方稳定版（一致性超强，成功率超高）_1920531109803655169.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `ConditioningZeroOut`
- `DiptychCreate`
- `DualCLIPLoader`
- `FluxGuidance`
- `ICEFConditioning`
- `ImageCrop`
- `InContextEditInstruction`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 8/10 个有
- `MaskPreview` —— 8/10 个有
- `UpscaleModelLoader` —— 8/10 个有
- `RH_Translator` —— 5/10 个有
- `Image Comparer (rgthree)` —— 3/10 个有
- `Anything Everywhere` —— 1/10 个有
- `DeepTranslatorTextNode` —— 1/10 个有
- `ImageScaleBy` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `Note _O` —— 1/10 个有
- `Seed Everywhere` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有
- `VHS_DuplicateLatents` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 10 | 90% |
| Prompt 约束强度(CFG) | 28 | 28 - 28 | 10 | 100% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler | - | 10 | 100% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，10 个样本，一致性 90%
- Prompt 约束强度(CFG) 中位数 28，观测区间 28 - 28，10 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 100%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 28，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
