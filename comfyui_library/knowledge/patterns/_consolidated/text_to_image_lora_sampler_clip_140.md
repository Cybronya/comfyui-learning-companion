---
name: text_to_image_lora_sampler_clip_140
type: Text To Image
frequency: 8
level: strong
coverage: 0.861875
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MuyeTextEditOutput, QwenImage21Cache, ResolutionSelector, SaveImage, SaveImageAdvanced, TTResolutionSelector, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1好玩的LoRA工作流，风格迁移换脸其他创意处理工具_2107235837036556290.json, 图片生成/图生图/Qwen Image 2.1角色资产生成工作流，角色一致性角色设计场景道具工具_2107206693816983553.json, 图片生成/文生图/Qwen Image 2.1官方流程混合流｜文生图编辑二合一_2106946249093107713.json, 视频生成/图生视频/Qwen Image 2.1角色资产生成角色一致性设计场景道具工作流，图生视频处理方案_2108325914386980866.json, 视频生成/图生视频/Qwen_Image_2.1人物姿势编辑迁移｜图片处理姿势随心改_2107277724539768834.json, 视频生成/图生视频/Qwen_Image_2.1官方流程混合流｜文生图编辑二合一_2107271722138431489.json, 视频生成/图生视频/Qwen_Image_2.1角色资产生成｜角色一致性设计场景道具_2107642152498057218.json, 视频生成/图生视频/Qwen_Image_2.1趣味Lora合集｜风格迁移换脸创意玩法_2107643764289392642.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_140

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1好玩的LoRA工作流，风格迁移换脸其他创意处理工具_2107235837036556290.json、图片生成/图生图/Qwen Image 2.1角色资产生成工作流，角色一致性角色设计场景道具工具_2107206693816983553.json、图片生成/文生图/Qwen Image 2.1官方流程混合流｜文生图编辑二合一_2106946249093107713.json、视频生成/图生视频/Qwen Image 2.1角色资产生成角色一致性设计场景道具工作流，图生视频处理方案_2108325914386980866.json、视频生成/图生视频/Qwen_Image_2.1人物姿势编辑迁移｜图片处理姿势随心改_2107277724539768834.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 8 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SaveImageAdvanced`
- `TTResolutionSelector`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 7/8 个有
- `ComfySwitchNode` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 6/8 个有
- `EmptyImage` —— 4/8 个有
- `孤海注释` —— 4/8 个有
- `ImageStitch` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `AddLabel` —— 2/8 个有
- `GetNode` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `JWStringConcat` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `StringMergeNode` —— 2/8 个有
- `ZML_AnyTypeSwitch` —— 2/8 个有
- `AnyLineArtPreprocessor_aux` —— 1/8 个有
- `DWPreprocessor` —— 1/8 个有
- `DepthPro` —— 1/8 个有
- `Hina.PoseEditor3D` —— 1/8 个有
- `LoadDepthPro` —— 1/8 个有
- `MetricDepthToRelative` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
