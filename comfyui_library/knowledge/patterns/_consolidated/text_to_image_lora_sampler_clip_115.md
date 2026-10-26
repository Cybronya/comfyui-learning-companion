---
name: text_to_image_lora_sampler_clip_115
type: Text To Image
frequency: 13
level: strong
coverage: 0.894
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1文生图25步_2102298549261266945.json, 图片生成/文生图/Qwen Image 2.1文生图25步官流处理生成工具_2102098942266798082.json, 图片生成/文生图/Qwen Image 2.1文生图25步精修版｜提示词直出高质量大片_2103672970286813186.json, 图片生成/文生图/Qwen Image 2.1文生图6步加速无PE工作流，文生图高效文本到图像方案_2107548461108387841.json, 图片生成/文生图/Qwen Image 2.1文生图t2i工作流，7B开源模型2K高清文字渲染方案_2103216666237820930.json, 图片生成/文生图/Qwen Image 2.1文生图上手版｜高质量出图简单易跑_2104575500873191425.json, 图片生成/文生图/Qwen Image 2.1文生图加4步加速，高质量文本到图像生成工作流_2103932568507863042.json, 图片生成/文生图/Qwen Image 2.1文生图增强版照片级写实创意插画商业宣传物料概念设计_2108659062555635713.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工作流_2102103619591036930.json, 图片生成/文生图/Qwen Image 2.1文生图处理生成工具_2102470456296169473.json, 图片生成/文生图/Qwen Image 2.1文生图工作流，最强开源模型中文提示词直接出图_2102861587425091586.json, 图片生成/文生图/Qwen image 2.1文生图基础款｜角色设计海报制作｜文字直出创意图_2112075461353365506.json, 视频生成/文生视频/Qwen_Image_2.1文生图工作流，最强开源模型中文提示词直接出图_2105513820637716482.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_115

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1文生图25步_2102298549261266945.json、图片生成/文生图/Qwen Image 2.1文生图25步官流处理生成工具_2102098942266798082.json、图片生成/文生图/Qwen Image 2.1文生图25步精修版｜提示词直出高质量大片_2103672970286813186.json、图片生成/文生图/Qwen Image 2.1文生图6步加速无PE工作流，文生图高效文本到图像方案_2107548461108387841.json、图片生成/文生图/Qwen Image 2.1文生图t2i工作流，7B开源模型2K高清文字渲染方案_2103216666237820930.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 12/13 个有
- `TextEncodeQwenImage21` —— 12/13 个有
- `孤海注释` —— 11/13 个有
- `SaveImageAdvanced` —— 6/13 个有
- `TextGenerateLTX2Prompt` —— 5/13 个有
- `Text Multiline` —— 4/13 个有
- `easy showAnything` —— 4/13 个有
- `PrimitiveStringMultiline` —— 3/13 个有
- `Text` —— 3/13 个有
- `easy seed` —— 3/13 个有
- `ImpactSwitch` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `ComfySwitchNode` —— 1/13 个有
- `ConditioningZeroOut` —— 1/13 个有
- `EmptyImage` —— 1/13 个有
- `ModelAttentionBackend` —— 1/13 个有
- `RH_LLMAPI_Pro_Node` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（16/13 个样本）：Steps较低可能导致细节不足
