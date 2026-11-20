---
name: text_to_image_lora_sampler_clip_131
type: Text To Image
frequency: 12
level: strong
coverage: 0.676167
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveInt, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1人物定装照多视图生成，四视图六视图角色设计图生图_2103175719546347522.json, 图片生成/图生图/Qwen Image 2.1人物替换加图片换人 角色一致性改图_2110354127594278914.json, 图片生成/图生图/Qwen Image 2.1十图编辑工作流，支持多图同时编辑的图生图处理工具_2106103497006604290.json, 图片生成/图生图/Qwen Image 2.1双图替换保留姿态，图片换人图生图利器_2112639487665852418.json, 图片生成/图生图/Qwen Image 2.1图片换人 双图替换保留姿态工具_2114075800545878017.json, 图片生成/图生图/Qwen Image 2.1故事分镜三模式｜九宫四宫随心切｜参考图直接生成分镜_2102591631139622913.json, 图片生成/图生图/Qwen Image 2.1故事分镜参考图生成，支持九宫格六宫格四宫格三种模式_2102820825970855938.json, 图片生成/图生图/千问2.1人物定装照生成｜四视图六视图角色设定全搞定_2103038149676060673.json, 图片生成/文生图/Qwen Image 2.1合集文生图单图多图编辑加提示词增强，角色一致性全覆盖_2102888298095140865.json, 视频生成/图生视频/Qwen Image 2.1故事分镜参考图生成支持九宫格六宫格四宫格，图生视频方案_2107217385190158338.json, 视频生成/图生视频/Qwen_Image_2.1合集文生图单图多图编辑加提示词增强，角色一致性全覆盖_2105107539770830850.json, 视频生成/图生视频/Qwen_Image_2.1故事分镜参考图生成，支持九宫格六宫格四宫格三种模式_2106549378277273601.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_131

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1人物定装照多视图生成，四视图六视图角色设计图生图_2103175719546347522.json、图片生成/图生图/Qwen Image 2.1人物替换加图片换人 角色一致性改图_2110354127594278914.json、图片生成/图生图/Qwen Image 2.1十图编辑工作流，支持多图同时编辑的图生图处理工具_2106103497006604290.json、图片生成/图生图/Qwen Image 2.1双图替换保留姿态，图片换人图生图利器_2112639487665852418.json、图片生成/图生图/Qwen Image 2.1图片换人 双图替换保留姿态工具_2114075800545878017.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 10/12 个有
- `PrimitiveBoolean` —— 9/12 个有
- `GetNode` —— 8/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/12 个有
- `PreviewAny` —— 8/12 个有
- `SetNode` —— 8/12 个有
- `easy seed` —— 8/12 个有
- `PrimitiveStringMultiline` —— 7/12 个有
- `RHLLMChatNode` —— 4/12 个有
- `StringConcatenate` —— 4/12 个有
- `EmptyImage` —— 3/12 个有
- `ImageResizeKJv2` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `ResolutionSelector` —— 3/12 个有
- `easy imageConcat` —— 3/12 个有
- `BatchImagesNode` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `ImageScale` —— 2/12 个有
- `SaveImageAdvanced` —— 2/12 个有
- `TextGenerateLTX2Prompt` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `ComfyMathExpression` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
