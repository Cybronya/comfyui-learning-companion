---
name: unknown_workflow_lora_sampler_unet_120
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.847333
common_nodes: [ConditioningZeroOut, DiptychCreate, DualCLIPLoader, FluxGuidance, ICEFConditioning, ImageCrop, InContextEditInstruction, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/IC+Edit全能图片G4o创成式填充服务端_1921536493649608705.json, 图片生成/图生图/IC-EDIT官方工作流优化版  提示词修改图片_1924492642829463553.json, 图片生成/图生图/ICEdit 工作流_1921046053074698242.json, 图片生成/图生图/ICEdit-MoE 最新图像编辑处理，低显存运行_1923196553685889025.json, 图片生成/图生图/ICEdit官方稳定版（一致性超强，成功率超高）_1920531109803655169.json, 图片生成/图生图/ICEdit官方稳定版（一致性超强，成功率超高）_1920674826652942338.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_120

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/IC+Edit全能图片G4o创成式填充服务端_1921536493649608705.json、图片生成/图生图/IC-EDIT官方工作流优化版  提示词修改图片_1924492642829463553.json、图片生成/图生图/ICEdit 工作流_1921046053074698242.json、图片生成/图生图/ICEdit-MoE 最新图像编辑处理，低显存运行_1923196553685889025.json、图片生成/图生图/ICEdit官方稳定版（一致性超强，成功率超高）_1920531109803655169.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
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
- `MaskPreview` —— 5/6 个有
- `ImageUpscaleWithModel` —— 4/6 个有
- `RH_Translator` —— 4/6 个有
- `UpscaleModelLoader` —— 4/6 个有
- `Anything Everywhere` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageScaleBy` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `Seed Everywhere` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `VHS_DuplicateLatents` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 100% |
| Prompt 约束强度(CFG) | 28 | 28 - 28 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 28，观测区间 28 - 28，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 28，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
