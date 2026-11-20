---
name: image_to_image_sampler_clip_unet_42
type: Image To Image
frequency: 8
level: weak
coverage: 0.83825
common_nodes: [CLIPLoader, CLIPTextEncode, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/image_qwen_image_controlnet_patch.json, 图片生成/图生图/001.Z-image生图巅峰010.图生图-洗图去重_2033739991351828481.json, 图片生成/图生图/001.Z-image生图巅峰012.姿势控制洗图_2033741966416023553.json, 图片生成/图生图/Qwen Image Uinon ControlNet  lora（多合一）之 canny 工作流_1959598906571173889.json, 图片生成/图生图/qwen_image_Inpaint-4步-局部重绘_1960511806496190466.json, 图片生成/图生图/qwen_image_canny-4步_1960506014829375490.json, 图片生成/图生图/qwen_image_depth-4步-吉卜力风格_1960527308945764353.json, 图片生成/文生图/Qwen万能控制网lora版_1959874321042845698.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_42

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（comfyui-workflow-templates-json/image_qwen_image_controlnet_patch.json、图片生成/图生图/001.Z-image生图巅峰010.图生图-洗图去重_2033739991351828481.json、图片生成/图生图/001.Z-image生图巅峰012.姿势控制洗图_2033741966416023553.json、图片生成/图生图/Qwen Image Uinon ControlNet  lora（多合一）之 canny 工作流_1959598906571173889.json、图片生成/图生图/qwen_image_Inpaint-4步-局部重绘_1960511806496190466.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `Canny` —— 5/8 个有
- `ModelPatchLoader` —— 5/8 个有
- `QwenImageDiffsynthControlnet` —— 5/8 个有
- `AIO_Preprocessor` —— 2/8 个有
- `ReferenceLatent` —— 2/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `DWPreprocessor` —— 1/8 个有
- `DepthAnythingV2Preprocessor` —— 1/8 个有
- `LineArtPreprocessor` —— 1/8 个有
- `easy imageIndexSwitch` —— 1/8 个有
- `easy imagePixelPerfect` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 20 | 8 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 8 | 58% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 0.6 - 1 | 8 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 20，8 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，8 个样本，取值集中（一致性 86%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
