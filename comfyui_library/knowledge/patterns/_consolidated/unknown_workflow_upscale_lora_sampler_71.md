---
name: unknown_workflow_upscale_lora_sampler_71
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.53
common_nodes: [AIO_Preprocessor, Anything Everywhere, CLIPLoader, ConditioningZeroOut, Fast Groups Bypasser (rgthree), FlashVSRNode, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LayerColor: Brightness & Contrast, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TextEncodeQwenImageEditPlusPro_lrzjason, UnetLoaderGGUF, VAEDecode, VAELoader, easy imageRemBg]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511-照片质感转换&重打光_2069983182677700610.json, 图片生成/图生图/YZ金鱼-Qwen-Edit-2509-进阶高清修复&照片质感转换&重打光_1990318149092429825.json, 平台全量/Qwen-2509-老照片修复（重上色重打光）_2013140024610529281.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_71

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511-照片质感转换&重打光_2069983182677700610.json、图片生成/图生图/YZ金鱼-Qwen-Edit-2509-进阶高清修复&照片质感转换&重打光_1990318149092429825.json、平台全量/Qwen-2509-老照片修复（重上色重打光）_2013140024610529281.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `FlashVSRNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerColor: Brightness & Contrast`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `LayerColor: BrightnessContrastV2` —— 2/3 个有
- `PlaySound|pysssss` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta57 | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta57，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
