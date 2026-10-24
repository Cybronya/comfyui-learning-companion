---
name: image_to_image_lora_sampler_unet_53
type: Image To Image
frequency: 11
level: moderate
coverage: 0.891091
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511图像编辑多合一工作流_2003654587804467201.json, 图片生成/图生图/Qwen-Image-Edit-2509 图像编辑 图像替换 多图融合 在线免费应用 免费下载部署_1982283626857545730.json, 图片生成/图生图/comfyui图像转钢笔插画_1985699102325448705.json, 图片生成/图生图/image_qwen_image_edit_2509-三图人物+动物+场景融合_1970991494343598082.json, 图片生成/图生图/image_qwen_image_edit_2509-双图人物姿态控制_1970987586586058753.json, 图片生成/图生图/image_qwen_image_edit_2509-双图人物指定换装和饰品_1970981672911020033.json, 图片生成/图生图/image_qwen_image_edit_2509-双图参考+参考色调重打光_2011594156342255617.json, 图片生成/图生图/image_qwen_image_edit_2509-提示词改变主体_1970979185940406274.json, 图片生成/图生图/qwen Edit 2511 单图编辑+修改表情_2059458819733942274.json, 图片生成/图生图/qwen Edit_2028751468630646786.json, 图片生成/图生图/qwen2509_1997815157244014594.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_53

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511图像编辑多合一工作流_2003654587804467201.json、图片生成/图生图/Qwen-Image-Edit-2509 图像编辑 图像替换 多图融合 在线免费应用 免费下载部署_1982283626857545730.json、图片生成/图生图/comfyui图像转钢笔插画_1985699102325448705.json、图片生成/图生图/image_qwen_image_edit_2509-三图人物+动物+场景融合_1970991494343598082.json、图片生成/图生图/image_qwen_image_edit_2509-双图人物姿态控制_1970987586586058753.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
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
- `EmptySD3LatentImage` —— 7/11 个有
- `ConditioningZeroOut` —— 2/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有
- `InpaintModelConditioning` —— 1/11 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/11 个有
- `MaskFillHoles` —— 1/11 个有
- `PixelSmileConditioning` —— 1/11 个有
- `QwenMultiangleCameraNode` —— 1/11 个有
- `Textbox` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 11 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 11 | 62% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（14/11 个样本）：Steps较低可能导致细节不足
