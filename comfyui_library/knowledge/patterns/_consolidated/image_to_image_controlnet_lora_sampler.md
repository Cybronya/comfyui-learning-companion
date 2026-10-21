---
name: image_to_image_controlnet_lora_sampler
type: Image To Image
frequency: 19
level: moderate
coverage: 0.475789
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetUnionControlNetType, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, MaskBlur+, PlaySound|pysssss, easy cleanGpuUsed, CR SDXL Aspect Ratio, MaskPreview+, LayerUtility: ImageScaleByAspectRatio V2, YC Color Match]
members: [图片生成/图生图/超强动漫转真人洗图-梦幻版_2107076681474338817.json, 图片生成/图生图/超强动漫转真人洗图-梦幻版_2107082036916875265.json, 图片生成/文生图/1986307410748997634.json, 图片生成/文生图/1988058768057503745.json, 图片生成/文生图/1988491119791095810.json, 图片生成/文生图/1988493280465829890.json, 图片生成/文生图/1988646135671775233.json, 图片生成/文生图/Qwen-image 文生图+图生图_2005139027424673794.json, 图片生成/文生图/Qwen-image超强Lora人像写真洗图-文生图_2079019496894984194.json, 图片生成/文生图/Qwen-image超强动漫转真人洗图_2062789194577174529.json, 图片生成/文生图/Qwen-image超强动漫转真人洗图形成_2087700951057653761.json, 图片生成/文生图/Qwen-image超强动漫转真人洗图（文生图）_2019221584623443970.json, 图片生成/文生图/Qwen-image超强动漫转真人洗图（梦幻版）_文生图_2067176994948861954.json, 图片生成/文生图/Qwen-image超强动漫转真人洗图（梦幻版）_文生图_2089546473515077633.json, 图片生成/文生图/Qwen-image超强洗图-动漫转真人_2058737952150343681.json, 图片生成/文生图/qwen-image2512工作流全合集 字体设计-洗图-图生图-文生图_2011082357918404610.json, 图片生成/文生图/人像写真丨Qwen-Image＋SeedVR2丨参考重绘·高清增强_2100465259931852802.json, 数字人/数字人/洗图，去ai感觉，高清！ Qwen-image_2100044842897338369.json, 视频生成/图生视频/洗图，去ai感觉，高清！_Qwen-image_2101218100065689602.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/超强动漫转真人洗图-梦幻版_2107076681474338817.json、图片生成/图生图/超强动漫转真人洗图-梦幻版_2107082036916875265.json、图片生成/文生图/1986307410748997634.json、图片生成/文生图/1988058768057503745.json、图片生成/文生图/1988491119791095810.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 19 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ControlNetInpaintingAliMamaApply` —— 18/19 个有
- `Fast Groups Bypasser (rgthree)` —— 18/19 个有
- `InpaintModelConditioning` —— 18/19 个有
- `JoinStrings` —— 18/19 个有
- `LanPaint_MaskBlend` —— 18/19 个有
- `MaskBlur+` —— 18/19 个有
- `MaskPreview+` —— 18/19 个有
- `PreviewBridge` —— 18/19 个有
- `Qwen3_VQA` —— 18/19 个有
- `SeedVR2` —— 18/19 个有
- `SeedVR2BlockSwap` —— 18/19 个有
- `SeedVR2ExtraArgs` —— 18/19 个有
- `TextInput_` —— 18/19 个有
- `VAEDecodeTiled` —— 18/19 个有
- `easy showAnything` —— 18/19 个有
- `Int` —— 15/19 个有
- `LayerUtility: ImageReel` —— 15/19 个有
- `LayerUtility: ImageReelComposit` —— 15/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 15/19 个有
- `GetNode` —— 5/19 个有
- `SetNode` —— 5/19 个有
- `PlaySound|pysssss` —— 4/19 个有
- `FastGroupsBypassSwitch` —— 3/19 个有
- `SeedVR2LoadDiTModel` —— 2/19 个有
- `SeedVR2LoadVAEModel` —— 2/19 个有
- `SeedVR2VideoUpscaler` —— 2/19 个有
- `CR Text` —— 1/19 个有
- `ColorCorrect` —— 1/19 个有
- `EmptyImage` —— 1/19 个有
- `EmptySD3LatentImage` —— 1/19 个有
- `INTConstant` —— 1/19 个有
- `LoraLoader` —— 1/19 个有
- `MemoryCleaner` —— 1/19 个有
- `PrimitiveStringMultiline` —— 1/19 个有
- `StringConcatenate` —— 1/19 个有
- `YC Color Match` —— 1/19 个有
- `easy imageConcat` —— 1/19 个有
- `easy seed` —— 1/19 个有
- `llama_cpp_instruct_adv` —— 1/19 个有
- `llama_cpp_model_loader` —— 1/19 个有
- `llama_cpp_parameters` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 19 | 55% |
| Prompt 约束强度(CFG) | 1.53 | 1 - 1.53 | 19 | 89% |
| 采样算法 | res_2s | - | 19 | 89% |
| 调度器 | bong_tangent | - | 19 | 84% |
| 重绘幅度 | 0.35 | 0.35 - 1 | 19 | 52% |
| ControlNet 权重 | 1 | 1 - 1 | 19 | 100% |
| LoRA 模型强度 | 1.5 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 52/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，19 个样本
- Prompt 约束强度(CFG) 中位数 1.53，观测区间 1 - 1.53，19 个样本，取值集中（一致性 89%）
- 采样算法 最常用 res_2s，19 个样本，一致性 89%
- 调度器 最常用 bong_tangent，19 个样本，一致性 84%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 1，19 个样本
- ControlNet 权重 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（52/19 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、MaskBlur+、PlaySound|pysssss、easy cleanGpuUsed
