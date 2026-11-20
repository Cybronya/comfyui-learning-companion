---
name: unknown_workflow_controlnet_sampler_clip_3
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.874286
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSamplerAdvanced, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AIGC人像系列-Z-image-turbo前5步CN控制采样+后5步采样的双采样_2029083151829569537.json, 图片生成/图生图/z-image-turbo_fun_controlnet2.0_2000859546035814402.json, 图片生成/图生图/z-image-turbo_fun_controlnet_base_1996418811291115522.json, 图片生成/图生图/z-image-turbo_fun_controlnet_qwenvl_1996420678859497473.json, 图片生成/图生图/工作流基础系列6-Z-Image-Turbo+CN控制工作流+双采样工作流-基础向讲解此工作流_2044661677328703490.json, 图片生成/图生图/组件系列7-Z-image-turbo双采样洗图_2058751468982849537.json, 图片生成/文生图/ZIT+CN+base双采样_2056090416516222978.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/AIGC人像系列-Z-image-turbo前5步CN控制采样+后5步采样的双采样_2029083151829569537.json、图片生成/图生图/z-image-turbo_fun_controlnet2.0_2000859546035814402.json、图片生成/图生图/z-image-turbo_fun_controlnet_base_1996418811291115522.json、图片生成/图生图/z-image-turbo_fun_controlnet_qwenvl_1996420678859497473.json、图片生成/图生图/工作流基础系列6-Z-Image-Turbo+CN控制工作流+双采样工作流-基础向讲解此工作流_2044661677328703490.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `AILab_QwenVL` —— 3/7 个有
- `DJZImageScaleToTotalPixels` —— 3/7 个有
- `GetImageSize` —— 3/7 个有
- `Seed (rgthree)` —— 3/7 个有
- `SimpleMath+` —— 3/7 个有
- `Anything Everywhere` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `LatentFrequencyEnhancer_lrzjason` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `SeargeIntegerMath` —— 1/7 个有
- `ShowAnything|Mie` —— 1/7 个有
- `ttN text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 57% |
| Prompt 约束强度(CFG) | 10 | 8 - 12 | 7 | 87% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 10，观测区间 8 - 12，7 个样本，取值集中（一致性 87%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
