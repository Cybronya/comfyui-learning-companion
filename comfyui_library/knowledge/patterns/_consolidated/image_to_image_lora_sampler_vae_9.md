---
name: image_to_image_lora_sampler_vae_9
type: Image To Image
frequency: 11
level: moderate
coverage: 0.856909
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-edit2509（双截棍版）-图像编辑_1993588971607441409.json, 图片生成/图生图/apple sharp高斯泼溅成图_2011269417006534657.json, 图片生成/图生图/apple sharp高斯泼溅成图_2025921551727595521.json, 图片生成/图生图/comfyui图像转钢笔插画_1985699102325448705.json, 图片生成/图生图/image_qwen_image_edit_2509-三图人物+动物+场景融合_1970991494343598082.json, 图片生成/图生图/image_qwen_image_edit_2509-双图人物姿态控制_1970987586586058753.json, 图片生成/图生图/image_qwen_image_edit_2509-双图人物指定换装和饰品_1970981672911020033.json, 图片生成/图生图/qwen Edit 2511 单图编辑_2051921199571193858.json, 图片生成/图生图/qwen image edit_2070040758069063682.json, 图片生成/图生图/qwen-edit-2509姿势迁移_1982348327364771842.json, 图片生成/图生图/姿态控制_1985545203467624449.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_9

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen-edit2509（双截棍版）-图像编辑_1993588971607441409.json、图片生成/图生图/apple sharp高斯泼溅成图_2011269417006534657.json、图片生成/图生图/apple sharp高斯泼溅成图_2025921551727595521.json、图片生成/图生图/comfyui图像转钢笔插画_1985699102325448705.json、图片生成/图生图/image_qwen_image_edit_2509-三图人物+动物+场景融合_1970991494343598082.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `EmptySD3LatentImage` —— 5/11 个有
- `Image Comparer (rgthree)` —— 5/11 个有
- `PreviewImage` —— 5/11 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/11 个有
- `AIO_Preprocessor` —— 2/11 个有
- `JoinStrings` —— 2/11 个有
- `PreviewAny` —— 2/11 个有
- `PrimitiveStringMultiline` —— 2/11 个有
- `RH_Captioner` —— 2/11 个有
- `Anything Everywhere` —— 1/11 个有
- `GetNode` —— 1/11 个有
- `ImageConcatMulti` —— 1/11 个有
- `ImageScaleToMegapixels` —— 1/11 个有
- `JWImageResizeByLongerSide` —— 1/11 个有
- `NunchakuQwenImageDiTLoader` —— 1/11 个有
- `SetNode` —— 1/11 个有
- `UpscaleModelLoader` —— 1/11 个有
- `VAEDecodeTiled` —— 1/11 个有
- `VAEEncodeTiled` —— 1/11 个有
- `easy imageScaleToNormPixels` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 11 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 0.35 - 1 | 11 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，11 个样本，取值集中（一致性 80%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
