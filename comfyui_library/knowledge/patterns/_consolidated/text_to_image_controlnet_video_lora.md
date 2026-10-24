---
name: text_to_image_controlnet_video_lora
type: Text To Image
frequency: 4
level: strong
coverage: 0.8185
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, GetImageSizeAndCount, ImageBlend, ImageConcanate, ImageResizeKJv2, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SetUnionControlNetType, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAELoader, WanVideoVACEModelSelect, easy cleanGpuUsed, easy int, easy saveText, easy seed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/生图-写实真人洗图-Qwen-image-2512-8步_1988666051044978689.json, 图片生成/图生图/生图-写实真人洗图-Qwen-image-2512-8步_2066055902303940608.json, 图片生成/图生图/生图-写实真人转动漫-Qwen-image-2512-8步_1988654444919308290.json, 图片生成/图生图/生图-动漫转写实真人-Qwen-image-2512-8步_1988641228445147138.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_video_lora

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/生图-写实真人洗图-Qwen-image-2512-8步_1988666051044978689.json、图片生成/图生图/生图-写实真人洗图-Qwen-image-2512-8步_2066055902303940608.json、图片生成/图生图/生图-写实真人转动漫-Qwen-image-2512-8步_1988654444919308290.json、图片生成/图生图/生图-动漫转写实真人-Qwen-image-2512-8步_1988641228445147138.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `ImageBlend`
- `ImageConcanate`
- `ImageResizeKJv2`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanVideoVACEModelSelect`
- `easy cleanGpuUsed`
- `easy int`
- `easy saveText`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `Qwen3_VQA` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1.01 | 1.01 - 1.01 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 100% |
| 调度器 | bong_tangent | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.01，观测区间 1.01 - 1.01，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 100%
- 调度器 最常用 bong_tangent，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
