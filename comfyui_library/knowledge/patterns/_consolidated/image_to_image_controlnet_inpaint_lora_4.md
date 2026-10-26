---
name: image_to_image_controlnet_inpaint_lora_4
type: Image To Image
frequency: 6
level: moderate
coverage: 0.864667
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image  完美扩图_1988908747290456066.json, 图片生成/图生图/Qwen image 扩图-Expand Image_1966523505372278786.json, 图片生成/图生图/Qwen局部重绘官方升级版_1966335141402619905.json, 图片生成/图生图/☯️千问-局部重绘_1972193619526479874.json, 图片生成/图生图/前端交互式裁剪扩图+qwen扩图流_2050196356471508993.json, 图片生成/图生图/图生图-Qwen image- 扩图-Expand Image_2052553332648103938.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen image  完美扩图_1988908747290456066.json、图片生成/图生图/Qwen image 扩图-Expand Image_1966523505372278786.json、图片生成/图生图/Qwen局部重绘官方升级版_1966335141402619905.json、图片生成/图生图/☯️千问-局部重绘_1972193619526479874.json、图片生成/图生图/前端交互式裁剪扩图+qwen扩图流_2050196356471508993.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 4/6 个有
- `InvertMask` —— 4/6 个有
- `MaskBlur+` —— 4/6 个有
- `SetLatentNoiseMask` —— 4/6 个有
- `LayerUtility: ExtendCanvasV2` —— 3/6 个有
- `LayerMask: MaskGrow` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `CFGNorm` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `ShowText` —— 1/6 个有
- `YC_FiveTextCombineNode` —— 1/6 个有
- `ycImageCropInteractive` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 6 | 68% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 6 | 65% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
