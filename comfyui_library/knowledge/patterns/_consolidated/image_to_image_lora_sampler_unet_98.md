---
name: image_to_image_lora_sampler_unet_98
type: Image To Image
frequency: 6
level: strong
coverage: 0.854833
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王009.打光神器_2034627699192369153.json, 图片生成/图生图/AI脑洞狮--相机多角度出图_2033939766948925441.json, 图片生成/图生图/Edit-2509-光线迁移优化模型_2000043637197205506.json, 图片生成/图生图/GS-多视角人物场景都可_2061465943561293825.json, 图片生成/图生图/QWEN一键单图直出多角度场景图生图_2061991338425536513.json, 图片生成/图生图/Qwen-Edit-一键角度编辑器_1990319553639051265.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_98

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王009.打光神器_2034627699192369153.json、图片生成/图生图/AI脑洞狮--相机多角度出图_2033939766948925441.json、图片生成/图生图/Edit-2509-光线迁移优化模型_2000043637197205506.json、图片生成/图生图/GS-多视角人物场景都可_2061465943561293825.json、图片生成/图生图/QWEN一键单图直出多角度场景图生图_2061991338425536513.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `CameraControlPromptNode` —— 1/6 个有
- `Color Input (mtb)` —— 1/6 个有
- `Display Any (rgthree)` —— 1/6 个有
- `ImageCompositeMasked` —— 1/6 个有
- `LayerUtility: ColorImage V2` —— 1/6 个有
- `LayerUtility: ColorPicker` —— 1/6 个有
- `QwenMultiangleCameraNode` —— 1/6 个有
- `ThresholdMask` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 6 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（20/6 个样本）：Steps较低可能导致细节不足
