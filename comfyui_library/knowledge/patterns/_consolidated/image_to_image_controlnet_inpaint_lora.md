---
name: image_to_image_controlnet_inpaint_lora
type: Image To Image
frequency: 17
level: moderate
coverage: 0.868824
common_nodes: [CLIPLoader, CLIPTextEncode, ControlNetInpaintingAliMamaApply, ControlNetLoader, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问qwen2512扩图（上、下、左、右按像素精准扩图）_1981271690015662082.json, 图片生成/图生图/千问局部重绘工作流_2005603751757053954.json, 图片生成/图生图/千问局部重绘工作流_2010317606443552769.json, 图片生成/图生图/千问扩图工作流_2005599741033541633.json, 图片生成/图生图/千问扩图工作流_2010274187272785921.json, 图片生成/图生图/啊癫 千问【最新】扩图工作流_2026689029210644481.json, 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_1966292208708128769.json, 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_1971006146779717633.json, 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_2028275236034060289.json, 图片生成/图生图/局部重绘-QWen-Image【Instantx-Controlnet】_1966421780745400322.json, 图片生成/图生图/扩图重绘-QWen-Image-Instantx-Controlnet_1966296641936461825.json, 图片生成/图生图/扩图重绘-千问-Image-【Instantx-Controlnet】_1966428766404816897.json, 图片生成/图生图/调色局部重绘-QWen-Image-Instantx-Controlnet_2026552365544902657.json, 图片生成/文生图/Qwen千问扩图【加速 LoRA 提速版】：原版 fp8_e4m3f + 低配 GGUF_2004037122640257026.json, 图片生成/文生图/千问局部重绘工作流_1989153552679448577.json, 图片生成/文生图/千问扩图工作流_1989155186948059137.json, 图片生成/文生图/局部重绘_1968599107654832130.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/千问qwen2512扩图（上、下、左、右按像素精准扩图）_1981271690015662082.json、图片生成/图生图/千问局部重绘工作流_2005603751757053954.json、图片生成/图生图/千问局部重绘工作流_2010317606443552769.json、图片生成/图生图/千问扩图工作流_2005599741033541633.json、图片生成/图生图/千问扩图工作流_2010274187272785921.json…）

- **类型**：Image To Image
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 16/17 个有
- `ImageAndMaskPreview` —— 11/17 个有
- `ImagePadForOutpaint` —— 8/17 个有
- `ImageStitch` —— 8/17 个有
- `PDImageResizeV2` —— 5/17 个有
- `ConditioningZeroOut` —— 3/17 个有
- `UnetLoaderGGUF` —— 3/17 个有
- `CLIPLoaderGGUF` —— 2/17 个有
- `Image Comparer (rgthree)` —— 2/17 个有
- `ImageUpscaleWithModel` —— 1/17 个有
- `UpscaleModelLoader` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 20 | 17 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 17 | 56% |
| 采样算法 | euler | - | 17 | 94% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 20，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，17 个样本
- 采样算法 最常用 euler，17 个样本，一致性 94%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（9/17 个样本）：Steps较低可能导致细节不足
