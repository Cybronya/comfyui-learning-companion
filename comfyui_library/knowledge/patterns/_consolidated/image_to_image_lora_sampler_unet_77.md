---
name: image_to_image_lora_sampler_unet_77
type: Image To Image
frequency: 9
level: weak
coverage: 0.577556
common_nodes: [CFGNorm, CLIPLoader, ComfySwitchNode, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN_CAMERA摄像机镜头角度切换图像编辑工作流_2066750376380035073.json, 图片生成/图生图/QWEN_多图编辑工作流（用于图像合成）_2066759807960440834.json, 图片生成/图生图/小红书firered_图像编辑_2029929480688504834.json, 图片生成/文生图/2.最强编辑融合，单图，双图，三图编辑qwen_image_edit_2511_2066121923188322306.json, 图片生成/文生图/Qwen_Image_Edit图像编辑模型_2105216109094981633.json, 图片生成/文生图/qwen动漫转真人+全节点注释_2055793141466320898.json, 图片生成/文生图/千问多角度templates-qwen_multiangle+全节点注释_2055470741176504322.json, 图片生成/文生图/参考图片打光+全节点注释_2055855007165108225.json, 平台全量/【CQ808】换装，小红书firered_图像编辑_2034601985034428417.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_77

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/QWEN_CAMERA摄像机镜头角度切换图像编辑工作流_2066750376380035073.json、图片生成/图生图/QWEN_多图编辑工作流（用于图像合成）_2066759807960440834.json、图片生成/图生图/小红书firered_图像编辑_2029929480688504834.json、图片生成/文生图/2.最强编辑融合，单图，双图，三图编辑qwen_image_edit_2511_2066121923188322306.json、图片生成/文生图/Qwen_Image_Edit图像编辑模型_2105216109094981633.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：58%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ComfySwitchNode`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus` —— 8/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/9 个有
- `JjkText` —— 2/9 个有
- `QwenMultiangleCameraNode` —— 2/9 个有
- `TextConcatenate` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `CR Text Concatenate` —— 1/9 个有
- `EmptyLatentImage` —— 1/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `Image Saver` —— 1/9 个有
- `Qwen3_VQA` —— 1/9 个有
- `ReferenceLatent` —— 1/9 个有
- `TextEncodeQwenImageEdit` —— 1/9 个有
- `ttN text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 40 | 9 | 11% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 9 | 39% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1920 | - | 1 | 100% |
| 高度 | 1080 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 40，9 个样本，取值分散，一致性仅 11%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，9 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（5/9 个样本）：Steps较低可能导致细节不足
