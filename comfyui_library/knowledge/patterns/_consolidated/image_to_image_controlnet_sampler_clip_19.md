---
name: image_to_image_controlnet_sampler_clip_19
type: Image To Image
frequency: 3
level: strong
coverage: 0.796
common_nodes: [AIO_Preprocessor, Any Switch (rgthree), CLIPTextEncode, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, Fast Groups Muter (rgthree), Fast Muter (rgthree), INTConstant, Image Comparer (rgthree), KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchLoader, Mute / Bypass Repeater (rgthree), OpenAI_Chat_API, PreviewImage, SDPoseDrawKeypoints, SDPoseKeypointExtractor, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAEEncode, ZImageFunControlnet, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/豹豹喵呜制作：白玉双采洗图工作流_2062834397220528129.json, 图片生成/图生图/🦊Z-image双采洗图工作流_2116861389779329026.json, 平台全量/CN控制-双采洗图工作流_2074392296161894402.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/豹豹喵呜制作：白玉双采洗图工作流_2062834397220528129.json、图片生成/图生图/🦊Z-image双采洗图工作流_2116861389779329026.json、平台全量/CN控制-双采洗图工作流_2074392296161894402.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `Fast Groups Muter (rgthree)`
- `Fast Muter (rgthree)`
- `INTConstant`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchLoader`
- `Mute / Bypass Repeater (rgthree)`
- `OpenAI_Chat_API`
- `PreviewImage`
- `SDPoseDrawKeypoints`
- `SDPoseKeypointExtractor`
- `SaveImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `ZImageFunControlnet`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
