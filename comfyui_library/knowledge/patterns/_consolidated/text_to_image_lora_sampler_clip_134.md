---
name: text_to_image_lora_sampler_clip_134
type: Text To Image
frequency: 11
level: strong
coverage: 0.802364
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1好玩的LoRA工作流，风格迁移换脸其他创意处理工具_2107235837036556290.json, 图片生成/图生图/Qwen Image 2.1角色资产生成工作流，角色一致性角色设计场景道具工具_2107206693816983553.json, 图片生成/图生图/Qwen Image 2.1角色资产生成工作流，角色一致性角色设计场景道具工具_2107552763440877569.json, 图片生成/图生图/Qwen Image 2.1角色资产生成｜角色一致性设计场景道具_2106939499853991937.json, 图片生成/图生图/Qwen Image 2.1趣味Lora合集｜风格迁移换脸创意玩法_2106937988050669569.json, 图片生成/图生图/QwenImage2.1 I2I官方提示词助手｜图生图有帮手｜描述写不好也能改图_2102637170602364929.json, 图片生成/图生图/QwenImage2.1图片编辑加提示词助手｜局部重绘超顺手_2103087888484356098.json, 图片生成/图生图/QwenImage2.1图生图搭配官方提示词助手，I2I编辑效率大幅提升_2102838137943838722.json, 图片生成/文生图/Qwen Image 2.1官方流程混合流｜文生图编辑二合一_2106946249093107713.json, 视频生成/图生视频/Qwen Image 2.1角色资产生成角色一致性设计场景道具工作流，图生视频处理方案_2108325914386980866.json, 视频生成/图生视频/Qwen_Image_2.1趣味Lora合集｜风格迁移换脸创意玩法_2107643764289392642.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_134

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1好玩的LoRA工作流，风格迁移换脸其他创意处理工具_2107235837036556290.json、图片生成/图生图/Qwen Image 2.1角色资产生成工作流，角色一致性角色设计场景道具工具_2107206693816983553.json、图片生成/图生图/Qwen Image 2.1角色资产生成工作流，角色一致性角色设计场景道具工具_2107552763440877569.json、图片生成/图生图/Qwen Image 2.1角色资产生成｜角色一致性设计场景道具_2106939499853991937.json、图片生成/图生图/Qwen Image 2.1趣味Lora合集｜风格迁移换脸创意玩法_2106937988050669569.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 10/11 个有
- `BatchImagesNode` —— 8/11 个有
- `CR Prompt Text` —— 8/11 个有
- `ComfySwitchNode` —— 8/11 个有
- `Fast Groups Bypasser (rgthree)` —— 8/11 个有
- `ImageResizeKJv2` —— 8/11 个有
- `MuyeTextEditOutput` —— 8/11 个有
- `TTResolutionSelector` —— 8/11 个有
- `easy cleanGpuUsed` —— 8/11 个有
- `PreviewImage` —— 7/11 个有
- `PrimitiveStringMultiline` —— 7/11 个有
- `GetNode` —— 6/11 个有
- `SetNode` —— 6/11 个有
- `ImageStitch` —— 4/11 个有
- `AddLabel` —— 3/11 个有
- `Any Switch (rgthree)` —— 3/11 个有
- `Image Comparer (rgthree)` —— 3/11 个有
- `ImageBatchMulti` —— 3/11 个有
- `ImageConcatMulti` —— 3/11 个有
- `ImageScaleToTotalPixels` —— 3/11 个有
- `JsonExtractString` —— 3/11 个有
- `TextConcatenator` —— 3/11 个有
- `EmptyImage` —— 2/11 个有
- `JWStringConcat` —— 1/11 个有
- `StringMergeNode` —— 1/11 个有
- `ZML_AnyTypeSwitch` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足
