---
name: text_to_image_lora_sampler_clip_94
type: Text To Image
frequency: 14
level: strong
coverage: 0.8815
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1多宫格分镜图V2图生图处理工具_2102559055175835650.json, 图片生成/图生图/Qwen Image 2.1多宫格分镜图V2，图生图快速产出多格故事板方案_2103263596930232322.json, 图片生成/图生图/Qwen Image 2.1官方原版图生图工作流，通义千问7B DiT轻量高效方案_2103198014163742721.json, 图片生成/图生图/Qwen Image 2.1指定抠图模式图生图处理生成工具_2102459788658569217.json, 图片生成/图生图/Qwen Image 2.1换头换脸Face Swap模特换头加换脸，图生图面部替换_2105790956023926785.json, 图片生成/图生图/Qwen Image 2.1换头换脸Face Swap模特换头加换脸，图生图面部替换工具_2105730994383974402.json, 图片生成/图生图/Qwen Image 2.1换头换脸Face Swap模特换头加换脸，图生图面部替换工具_2106109794053607425.json, 图片生成/图生图/Qwen Image 2.1最强开源图像编辑多图模特换装图生图处理工具_2102088091476512769.json, 图片生成/图生图/Qwen Image 2.1电商换装神器｜模特服装自动替换一键完成_2103671470185603074.json, 图片生成/图生图/Qwen Image 2.1自动抠图透明背景，图生图一键去底处理工具_2103602803808759810.json, 图片生成/图生图/Qwen image 2.1 turbo图生图 快速改图直出方案_2110353791806697473.json, 图片生成/图生图/Qwen image 2.1多图编辑int8版｜自带提示词增强｜图生图低显存友好_2102210466104832001.json, 图片生成/图生图/Qwen image 2.1多宫格分镜图V2.2 多场景批量出图方案_2105381690167349250.json, 图片生成/文生图/qen image 2.1turbo图片编辑，文生图图生图双修_2111229917986910209.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_94

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1多宫格分镜图V2图生图处理工具_2102559055175835650.json、图片生成/图生图/Qwen Image 2.1多宫格分镜图V2，图生图快速产出多格故事板方案_2103263596930232322.json、图片生成/图生图/Qwen Image 2.1官方原版图生图工作流，通义千问7B DiT轻量高效方案_2103198014163742721.json、图片生成/图生图/Qwen Image 2.1指定抠图模式图生图处理生成工具_2102459788658569217.json、图片生成/图生图/Qwen Image 2.1换头换脸Face Swap模特换头加换脸，图生图面部替换_2105790956023926785.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 11/14 个有
- `ResolutionSelector` —— 11/14 个有
- `TextGenerateLTX2Prompt` —— 10/14 个有
- `BatchImagesNode` —— 7/14 个有
- `PrimitiveStringMultiline` —— 7/14 个有
- `easy showAnything` —— 5/14 个有
- `RHLLMChatNode` —— 3/14 个有
- `StringConcatenate` —— 3/14 个有
- `ZNGB_ImageBatchMulti` —— 3/14 个有
- `CR Text` —— 2/14 个有
- `KSamplerSelect` —— 2/14 个有
- `ManualSigmas` —— 2/14 个有
- `PrimitiveBoolean` —— 2/14 个有
- `SamplerCustom` —— 2/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/14 个有
- `MultiTextConcatenate` —— 1/14 个有
- `Note Plus (mtb)` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（17/14 个样本）：Steps较低可能导致细节不足
