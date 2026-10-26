---
name: unknown_workflow_upscale_lora_sampler_57
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.838667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageLoader, ImageScaleToTotalPixels, KSamplerSelect, LoraLoaderModelOnly, MultiTextConcatenate, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, TextInputNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [图片生成/图生图/3D、VAM、二次元动漫转真人图像-Klein+ZIT超强双重洗图_2041715230685798401.json, 图片生成/图生图/3D、VAM、二次元动漫转真人图像-自动提示词加强版 Klein超强洗图工作流_2041703569144946690.json, 图片生成/图生图/3D、VAM、二次元动漫转真人图像-自定义提示词控制版 Klein超强洗图工作流_2041712187827298306.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_57

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/3D、VAM、二次元动漫转真人图像-Klein+ZIT超强双重洗图_2041715230685798401.json、图片生成/图生图/3D、VAM、二次元动漫转真人图像-自动提示词加强版 Klein超强洗图工作流_2041703569144946690.json、图片生成/图生图/3D、VAM、二次元动漫转真人图像-自定义提示词控制版 Klein超强洗图工作流_2041712187827298306.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageLoader`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MultiTextConcatenate`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `TextInputNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `MultiplePathsInput` —— 2/3 个有
- `Qwen3_VQA` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CR Seed` —— 1/3 个有
- `GenerateNoise` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `LGNoiseInjectionLatent` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `kkGetImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | dpmpp_2s_ancestral | - | 1 | 100% |
| 调度器 | bong_tangent | - | 1 | 100% |
| 重绘幅度 | 0.3 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
