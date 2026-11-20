---
name: unknown_workflow_sampler_unet_vae_77
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.802818
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/image_qwen_image_2_1_edit_anything_ref_2102668719456604161.json, 图片生成/图生图/image_qwen_image_2_1_ref2i_2102667025813426177.json, 图片生成/图生图/qwen2.1 漫剧角色三视图生成_2110530131713421314.json, 图片生成/图生图/qwen2.1_漫剧角色三视图生成_2114273135901110273.json, 图片生成/图生图/qwen_image_2.1_图编辑_2104046121885720577.json, 图片生成/图生图/qwen_image_2.1图像编辑_2103699751001747458.json, 图片生成/图生图/qwen_image_2_1_图像编辑-文本换装_2104452144555450369.json, 图片生成/图生图/qwen_image_2_1_手持指定物品_2104438895411818497.json, 图片生成/文生图/qwen_image_2_1_图像编辑-换背景和姿态_2102217040533745665.json, 视频生成/图生视频/Qwen_Image_2.1图片透明分层！_生成透明图层_2104453762017484802.json, 视频生成/图生视频/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102960653840510977.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_77

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/image_qwen_image_2_1_edit_anything_ref_2102668719456604161.json、图片生成/图生图/image_qwen_image_2_1_ref2i_2102667025813426177.json、图片生成/图生图/qwen2.1 漫剧角色三视图生成_2110530131713421314.json、图片生成/图生图/qwen2.1_漫剧角色三视图生成_2114273135901110273.json、图片生成/图生图/qwen_image_2.1_图编辑_2104046121885720577.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 8/11 个有
- `PreviewImage` —— 8/11 个有
- `EmptyImage` —— 7/11 个有
- `QwenImage21Cache` —— 6/11 个有
- `PrimitiveStringMultiline` —— 5/11 个有
- `BatchImagesNode` —— 2/11 个有
- `CR Prompt Text` —— 2/11 个有
- `ImageCompositeMasked` —— 2/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `JjkText` —— 2/11 个有
- `PreviewAny` —— 2/11 个有
- `TextGenerateLTX2Prompt` —— 2/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `TextCombinerSix` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 11 | 100% |
| 高度 | 1024 | 1024 - 1536 | 11 | 86% |
| 采样步数 | 25 | 25 - 50 | 11 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，11 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，11 个样本，取值集中（一致性 86%）
- 采样步数 中位数 25，观测区间 25 - 50，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
