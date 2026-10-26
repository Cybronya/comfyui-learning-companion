---
name: unknown_workflow_upscale_latent_upscale_lora_58
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5566
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, Fast Groups Bypasser (rgthree), FloatConstant, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerAdvanced, LatentUpscaleBy, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SimpleMath+, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/ZIBT 高清写真图生图20260407_2041177396161810433.json, 图片生成/文生图/Moody文生图_2034202713419948033.json, 图片生成/文生图/YZ金鱼-Moody ZIB+ZIT 文生图_2033524845866127361.json, 图片生成/文生图/ZIB+ZIT-双采文生图_2054942630194229249.json, 图片生成/文生图/双Z高清文生图_2035896757829242882.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_58

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/ZIBT 高清写真图生图20260407_2041177396161810433.json、图片生成/文生图/Moody文生图_2034202713419948033.json、图片生成/文生图/YZ金鱼-Moody ZIB+ZIT 文生图_2033524845866127361.json、图片生成/文生图/ZIB+ZIT-双采文生图_2054942630194229249.json、图片生成/文生图/双Z高清文生图_2035896757829242882.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `FloatConstant`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerAdvanced`
- `LatentUpscaleBy`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `llama_cpp_instruct_adv` —— 4/5 个有
- `llama_cpp_model_loader` —— 4/5 个有
- `CR Prompt Text` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `DuckHideNode` —— 1/5 个有
- `Int` —— 1/5 个有
- `Lora Loader Stack (rgthree)` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `ProcessString` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `SomethingToString` —— 1/5 个有
- `TT_img_enc_v2` —— 1/5 个有
- `TextConcatenate` —— 1/5 个有
- `ZML_SwitchOutput` —— 1/5 个有
- `easy promptLine` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 15 | 5 | 89% |
| 采样算法 | 1 | 1 - 4 | 5 | 33% |
| 调度器 | sa_solver | - | 5 | 60% |
| 重绘幅度 | beta | - | 5 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 15，5 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 33%
- 调度器 最常用 sa_solver，5 个样本，一致性 60%
- 重绘幅度 最常用 beta，5 个样本，一致性 60%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
