---
name: text_to_image_lora_sampler_clip_90
type: Text To Image
frequency: 14
level: strong
coverage: 0.8155
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, SaveImageAdvanced, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1元素移除局部重绘擦除图生图处理工具_2102524212488531970.json, 图片生成/图生图/Qwen Image 2.1元素移除｜局部重绘擦除一体｜图生图去杂物不留痕_2102293368142389249.json, 图片生成/图生图/Qwen Image 2.1图像编辑 官方模板，原生2K支持图生图方案_2103547482436358146.json, 图片生成/图生图/Qwen Image 2.1图像编辑 局部修改指令式操作_2105347589154627586.json, 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102095974146596866.json, 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102100461598892034.json, 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102192876569583617.json, 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102517800026861570.json, 图片生成/图生图/Qwen Image 2.1图像编辑｜热门IP写实图生图 修图改图全能手_2104104246579916802.json, 图片生成/图生图/Qwen Image 2.1扩图局部重绘图生图处理工具_2102522537514196994.json, 图片生成/图生图/Qwen Image 2.1扩图局部重绘｜图生图边缘补全双修｜画幅随意切换_2102291809056681986.json, 图片生成/图生图/Qwen Image 2.1智能扩图｜画面边缘自然延展｜图生图补全构图神器_2102258886488186882.json, 图片生成/图生图/Qwen Image 2.1生图改图拼图三合一，多参考高精度可控图生图方案_2103257263350829057.json, 图片生成/图生图/写实图像编辑 Qwen Image 2.1热门IP风格改图_2104280927772958722.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_90

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1元素移除局部重绘擦除图生图处理工具_2102524212488531970.json、图片生成/图生图/Qwen Image 2.1元素移除｜局部重绘擦除一体｜图生图去杂物不留痕_2102293368142389249.json、图片生成/图生图/Qwen Image 2.1图像编辑 官方模板，原生2K支持图生图方案_2103547482436358146.json、图片生成/图生图/Qwen Image 2.1图像编辑 局部修改指令式操作_2105347589154627586.json、图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102095974146596866.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 14 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 9/14 个有
- `ResizeImageMaskNode` —— 7/14 个有
- `GetNode` —— 6/14 个有
- `SetNode` —— 6/14 个有
- `DrawMaskOnImage` —— 5/14 个有
- `GetImageSize` —— 5/14 个有
- `PreviewImage` —— 5/14 个有
- `PrimitiveStringMultiline` —— 5/14 个有
- `ImageCompare` —— 4/14 个有
- `ImagePadForOutpaint` —— 3/14 个有
- `GrowMaskWithBlur` —— 2/14 个有
- `ModelAttentionBackend` —— 2/14 个有
- `ResizeMask` —— 2/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
