---
name: image_to_image_controlnet_inpaint_lora_4
type: Image To Image
frequency: 8
level: moderate
coverage: 0.829875
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/image_qwen_image_instantx_inpainting_controlnet.json, "图片生成/图生图/Qwen Image, Instantx, Inpainting 局部重绘_1987174155143548929.json", 图片生成/图生图/qwen-image-蒙版-局部重绘_1983723157448237057.json, 图片生成/图生图/千问Qwen-2512-局部重绘_2061631721447182337.json, 图片生成/图生图/千问Qwen-2512-局部重绘_2067057839675371521.json, 图片生成/图生图/千问Qwen-2512-局部重绘_2067170819138220034.json, 图片生成/图生图/千问Qwen-inpainting-扩图_2061654605532061697.json, 图片生成/图生图/大碗有料-Qwen扩图-（拆解）_2009535083581022210.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora_4

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（comfyui-workflow-templates-json/image_qwen_image_instantx_inpainting_controlnet.json、图片生成/图生图/Qwen Image, Instantx, Inpainting 局部重绘_1987174155143548929.json、图片生成/图生图/qwen-image-蒙版-局部重绘_1983723157448237057.json、图片生成/图生图/千问Qwen-2512-局部重绘_2061631721447182337.json、图片生成/图生图/千问Qwen-2512-局部重绘_2067057839675371521.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 7/8 个有
- `MaskPreview` —— 7/8 个有
- `GrowMask` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `ModelSamplingAuraFlow` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `MaskBlur+` —— 4/8 个有
- `ImageCompositeMasked` —— 3/8 个有
- `ImagePadForOutpaint` —— 3/8 个有
- `ImageScaleToMaxDimension` —— 3/8 个有
- `Mask Fill Holes` —— 3/8 个有
- `ImageConcanate` —— 2/8 个有
- `2a4b2cc0-db37-4302-a067-da392f38f06b` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `GrowMaskWithBlur` —— 1/8 个有
- `ImageAndMaskPreview` —— 1/8 个有
- `MaskPreview+` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `cade3e30-0eb2-4fd2-bf6e-8518f3a96e0c` —— 1/8 个有
- `f93c215e-c393-460e-9534-ed2c3d8a652e` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 8 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 8 | 58% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，8 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
