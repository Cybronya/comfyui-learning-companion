---
name: image_to_image_lora_sampler_unet_44
type: Image To Image
frequency: 12
level: strong
coverage: 0.886917
common_nodes: [CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-edit2511-风格多样化 创意玩法_2010195628764176385.json, 图片生成/图生图/Qwen-image-edit2511三图融合--标准版--（必收藏）_2049911848614543361.json, 图片生成/图生图/Qwen-image-edit2511双图编辑--标准版--（必收藏）_2049875414901903362.json, 图片生成/图生图/Qwen-image-edit2511：创意变色龙！一张底图，指尖轻点解锁数十种风格_2010011563326967809.json, 图片生成/图生图/Qwen20角度训练集_正式版lora训练集_2086043197633028097.json, 图片生成/图生图/Qwen2511多角度控制_2009846604588654594.json, 图片生成/图生图/QwenMultiangle2511图片多角度自由控制_2058843387687690241.json, 图片生成/图生图/Qwen_Edit_2511_Multiangle图片角度自由控制_2077221377760911362.json, 图片生成/图生图/修改角度工作流_2042886227157848065.json, 图片生成/图生图/全能生图 千问 2511多角度变换_2012356861068054529.json, 图片生成/图生图/千问edit2511：创意变色龙解锁数十种风格26127_2016127266601832449.json, 图片生成/图生图/手动调整场景角度（免费版）_2010620776700973058.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_44

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen-image-edit2511-风格多样化 创意玩法_2010195628764176385.json、图片生成/图生图/Qwen-image-edit2511三图融合--标准版--（必收藏）_2049911848614543361.json、图片生成/图生图/Qwen-image-edit2511双图编辑--标准版--（必收藏）_2049875414901903362.json、图片生成/图生图/Qwen-image-edit2511：创意变色龙！一张底图，指尖轻点解锁数十种风格_2010011563326967809.json、图片生成/图生图/Qwen20角度训练集_正式版lora训练集_2086043197633028097.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `CFGNorm` —— 10/12 个有
- `QwenMultiangleCameraNode` —— 7/12 个有
- `INTConstant` —— 6/12 个有
- `PreviewImage` —— 5/12 个有
- `easy promptList` —— 5/12 个有
- `easy showAnything` —— 5/12 个有
- `MultiTextConcatenate` —— 4/12 个有
- `JjkText` —— 3/12 个有
- `Text` —— 3/12 个有
- `VNCCS_VisualPositionControl` —— 3/12 个有
- `easy anythingIndexSwitch` —— 3/12 个有
- `Int` —— 2/12 个有
- `Text Multiline` —— 2/12 个有
- `ConstrainImage|pysssss` —— 1/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `FluxKontextImageScale` —— 1/12 个有
- `RH_Nano_Banana2_Image2Image` —— 1/12 个有
- `Text Concatenate` —— 1/12 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 8 | 12 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（31/12 个样本）：Steps较低可能导致细节不足
