---
name: text_to_image_sampler_clip_unet_36
type: Text To Image
frequency: 14
level: moderate
coverage: 0.912071
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ComfyUI_桌布V3_2053374663803326465.json, 图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2044578596047560706.json, 图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2047608589782622210.json, 图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2069658196112920577.json, 图片生成/文生图/ERNIE-Image-文生图_2044602654369783809.json, 图片生成/文生图/Kook_Flux_klein_亚洲人像_2019704034847891458.json, 图片生成/文生图/Krea 2 甜美人像_2082369312555356161.json, 图片生成/文生图/Krea2_T2I_noLora_2089078237040308226.json, 图片生成/文生图/Magic-Wan2.2-V2文生图工作流_1993696801660354561.json, 图片生成/文生图/N-Super Z-image 3.0+lota文生图_2020339880995332097.json, 图片生成/文生图/YJ-APP-Zimage-文生图-瑶光_2038252771387908097.json, 图片生成/文生图/Z-image 超清快速30秒文生图 省时省币_2038518587316506625.json, 图片生成/文生图/Z-image 超清快速文生图_2008571327392784386.json, 图片生成/文生图/文生图精简版+全节点注释_2067404118905409537.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_36

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/ComfyUI_桌布V3_2053374663803326465.json、图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2044578596047560706.json、图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2047608589782622210.json、图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2069658196112920577.json、图片生成/文生图/ERNIE-Image-文生图_2044602654369783809.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 13/14 个有
- `Text` —— 4/14 个有
- `PrimitiveInt` —— 3/14 个有
- `LoadImage` —— 2/14 个有
- `DuckHideNode` —— 1/14 个有
- `TextEncodeQwenImageEditPlus` —— 1/14 个有
- `TextInput_` —— 1/14 个有
- `easy imageScaleDownToSize` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 28 | 14 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 14 | 35% |
| 采样算法 | euler | - | 14 | 79% |
| 调度器 | simple | - | 14 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 1024 | 720 - 1920 | 14 | 74% |
| 高度 | 1536 | 1024 - 1920 | 14 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 28，14 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，14 个样本，取值分散，一致性仅 35%
- 采样算法 最常用 euler，14 个样本，一致性 79%
- 调度器 最常用 simple，14 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 720 - 1920，14 个样本
- 高度 中位数 1536，观测区间 1024 - 1920，14 个样本，取值集中（一致性 81%）
