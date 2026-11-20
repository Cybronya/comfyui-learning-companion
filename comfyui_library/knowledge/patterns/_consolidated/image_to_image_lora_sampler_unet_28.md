---
name: image_to_image_lora_sampler_unet_28
type: Image To Image
frequency: 15
level: moderate
coverage: 0.8624
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2511-AnyPose用参考图实现姿势控制_2065718964432494594.json, 图片生成/图生图/Qwen-Image-2511-AnyPose用参考图实现姿势控制_2006282960210763777.json, 图片生成/图生图/Qwen_千问一键丰胸工作流_2003473370219986945.json, 图片生成/图生图/yj丰胸_2011686538739982337.json, 图片生成/图生图/一键丰胸神器，即刻变美！_2005605400391151618.json, 图片生成/图生图/一键丰胸神器，完美丰胸！_2033013429618872322.json, 图片生成/图生图/一键改变人物视角_1991135857899864066.json, 图片生成/图生图/一键生成图片视角转变_2049739021416443905.json, 图片生成/图生图/一键生成图片视角转变_2049751286458884098.json, 图片生成/图生图/产品六视图生成-直接宫格_2043952379636228098.json, 图片生成/图生图/产品六视图生成-组合图分析_2044290263606104065.json, 图片生成/图生图/姿势控制 Qwen2511-AnyPose_2065745202484170754.json, 图片生成/图生图/支持三张图上传-产品多视图生成_2045049085916356609.json, 图片生成/图生图/支持两张图上传-产品多视图生成_2044716033809846273.json, 图片生成/图生图/支持单张图上传-产品多视图生成_2044719135245996033.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_28

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/2511-AnyPose用参考图实现姿势控制_2065718964432494594.json、图片生成/图生图/Qwen-Image-2511-AnyPose用参考图实现姿势控制_2006282960210763777.json、图片生成/图生图/Qwen_千问一键丰胸工作流_2003473370219986945.json、图片生成/图生图/yj丰胸_2011686538739982337.json、图片生成/图生图/一键丰胸神器，即刻变美！_2005605400391151618.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 15 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `ImageScaleToTotalPixels` —— 12/15 个有
- `ImageUpscaleWithModel` —— 11/15 个有
- `PreviewImage` —— 11/15 个有
- `UpscaleModelLoader` —— 11/15 个有
- `Image Comparer (rgthree)` —— 10/15 个有
- `easy imageSize` —— 6/15 个有
- `PIP_图像联结` —— 5/15 个有
- `ImageResizePresetNode` —— 3/15 个有
- `AnyBooleanSwitch` —— 2/15 个有
- `ImageResize` —— 2/15 个有
- `ImageResizeKJv2` —— 2/15 个有
- `ImageTile+` —— 2/15 个有
- `ImageUntile+` —— 2/15 个有
- `RMBG` —— 2/15 个有
- `Anything Everywhere` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 15 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 15 | 58% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 36/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，15 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（36/15 个样本）：Steps较低可能导致细节不足
