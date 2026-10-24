---
name: image_to_image_controlnet_inpaint_lora_10
type: Image To Image
frequency: 4
level: strong
coverage: 0.83025
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 局部重绘，极小区域重绘（完美无缝加速版-InstantX）_1966480322672144386.json, 图片生成/图生图/千问Qwen-Image-inpaint完美加速扩图工作流_1967425764293533698.json, 图片生成/图生图/千问局部重绘（Qwen Inpaint-InstantX）加速V2_1966468855948324866.json, 图片生成/图生图/千问扩图（完美加速版-InstantX）_1966457213625774081.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen 局部重绘，极小区域重绘（完美无缝加速版-InstantX）_1966480322672144386.json、图片生成/图生图/千问Qwen-Image-inpaint完美加速扩图工作流_1967425764293533698.json、图片生成/图生图/千问局部重绘（Qwen Inpaint-InstantX）加速V2_1966468855948324866.json、图片生成/图生图/千问扩图（完美加速版-InstantX）_1966457213625774081.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `TextInput_` —— 3/4 个有
- `GrowMaskWithBlur` —— 2/4 个有
- `ImagePadForOutpaint` —— 2/4 个有
- `InpaintCropImproved` —— 1/4 个有
- `InpaintStitchImproved` —— 1/4 个有
- `Int` —— 1/4 个有
- `JWFloat` —— 1/4 个有
- `LayerMask: MaskGrow` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
