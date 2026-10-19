---
name: image_to_image_controlnet_inpaint_lora
type: Image To Image
frequency: 10
level: strong
coverage: 0.4138
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetInpaintingAliMamaApply, ControlNetLoader, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, InpaintModelConditioning, JoinStrings, KSampler, LanPaint_MaskBlend, LoadImage, LoraLoaderModelOnly, MaskBlur+, MaskPreview+, ModelSamplingAuraFlow, PreviewBridge, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetUnionControlNetType, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, MaskBlur+, PlaySound|pysssss, easy cleanGpuUsed, CR SDXL Aspect Ratio, MaskPreview+, LayerUtility: ImageScaleByAspectRatio V2, YC Color Match]
members: [图片生成/图生图/超强动漫转真人洗图-梦幻版_2107076681474338817.json, 图片生成/图生图/超强动漫转真人洗图-梦幻版_2107082036916875265.json, 图片生成/文生图/1986307410748997634.json, 图片生成/文生图/1988058768057503745.json, 图片生成/文生图/1988491119791095810.json, 图片生成/文生图/1988493280465829890.json, 图片生成/文生图/1988646135671775233.json, 图片生成/文生图/人像写真丨Qwen-Image＋SeedVR2丨参考重绘·高清增强_2100465259931852802.json, 数字人/数字人/洗图，去ai感觉，高清！ Qwen-image_2100044842897338369.json, 视频生成/图生视频/洗图，去ai感觉，高清！_Qwen-image_2101218100065689602.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/超强动漫转真人洗图-梦幻版_2107076681474338817.json、图片生成/图生图/超强动漫转真人洗图-梦幻版_2107082036916875265.json、图片生成/文生图/1986307410748997634.json、图片生成/文生图/1988058768057503745.json、图片生成/文生图/1988491119791095810.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：41%

## 共有节点

全部 10 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `JoinStrings`
- `KSampler`
- `LanPaint_MaskBlend`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskBlur+`
- `MaskPreview+`
- `ModelSamplingAuraFlow`
- `PreviewBridge`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 7/10 个有
- `LayerUtility: ImageReelComposit` —— 7/10 个有
- `Int` —— 6/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/10 个有
- `GetNode` —— 4/10 个有
- `PlaySound|pysssss` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `FastGroupsBypassSwitch` —— 3/10 个有
- `EmptyImage` —— 1/10 个有
- `YC Color Match` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 10 | 54% |
| Prompt 约束强度(CFG) | 1.53 | 1.53 - 1.53 | 10 | 100% |
| 采样算法 | res_2s | - | 10 | 90% |
| 调度器 | bong_tangent | - | 10 | 90% |
| 重绘幅度 | 0.35 | 0.35 - 0.35 | 10 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，10 个样本
- Prompt 约束强度(CFG) 中位数 1.53，观测区间 1.53 - 1.53，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，10 个样本，一致性 90%
- 调度器 最常用 bong_tangent，10 个样本，一致性 90%
- 重绘幅度 中位数 0.35，观测区间 0.35 - 0.35，10 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（22/10 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageReel、LayerUtility: ImageReelComposit、MaskBlur+、PlaySound|pysssss、easy cleanGpuUsed
