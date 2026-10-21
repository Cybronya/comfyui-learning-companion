---
name: text_to_image_lora_sampler_clip_20
type: Text To Image
frequency: 23
level: weak
coverage: 0.948783
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima Aesthetic 1.1｜1.5倍放大_2078374859184365569.json, 图片生成/文生图/Anima Aesthetic 1.1｜三阶高质量渲染_2078374835163582465.json, 图片生成/文生图/Anima+Aesthetic+1.1｜DMDX+四步极速版_2078701772113272834.json, 图片生成/文生图/Anima+Aesthetic+1.1｜文生图_2078701764664184833.json, 图片生成/文生图/Anima+Aesthetic+1.1｜文生图_2079573127385927682.json, 图片生成/文生图/Qwen Image 文生图，千问基础文生图_2005132413141479426.json, 图片生成/文生图/Qwen image 2512 我的50年_Qwen-Image-2512_2006650484186157057.json, 图片生成/文生图/Qwen image 2512文生图_2008433887889858562.json, 图片生成/文生图/Qwen-Image-2512 + LoRA 文生图_2091487545254301698.json, 图片生成/文生图/Qwen-Image-2512 文生图 8步加速_2014683752181538818.json, 图片生成/文生图/Qwen-Image-2512 最新文生图_2006383515574738946.json, 图片生成/文生图/Qwen-Image-2512不用LoRA实现人物一致性_2006694730360430594.json, 图片生成/文生图/Qwen-Image-2512卡通女孩LoRA_2007803177848020993.json, 图片生成/文生图/Qwen-Image-2512四步10秒出图Qwen image 2512_2006497445919854594.json, 图片生成/文生图/Qwen-Image-2512文生图_2006354179845005313.json, 图片生成/文生图/Qwen-Image-2512的Bill_LoRA_2007418345481576449.json, 图片生成/文生图/Qwen-Image2512中文渲染全系列工作流_2010150714567299074.json, 图片生成/文生图/Qwen2.1文生图（写实风格）_2104831851583066113.json, 图片生成/文生图/Qwen2512JK制服甜妹_2018334963661283330.json, 图片生成/文生图/Qwen2512油亮丝袜马油连裤袜美女_2018144682206826497.json, 图片生成/文生图/Z-image + LoRA 文生图工作流_2058875529981415425.json, 图片生成/文生图/Z-image 文生图工作流（含加速器）_2046950465908252673.json, 图片生成/文生图/潦草线条铅笔画_2017271179677016065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/文生图/Anima Aesthetic 1.1｜1.5倍放大_2078374859184365569.json、图片生成/文生图/Anima Aesthetic 1.1｜三阶高质量渲染_2078374835163582465.json、图片生成/文生图/Anima+Aesthetic+1.1｜DMDX+四步极速版_2078701772113272834.json、图片生成/文生图/Anima+Aesthetic+1.1｜文生图_2078701764664184833.json、图片生成/文生图/Anima+Aesthetic+1.1｜文生图_2079573127385927682.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 21/23 个有
- `ModelSamplingAuraFlow` —— 18/23 个有
- `PreviewImage` —— 9/23 个有
- `ClownsharKSampler_Beta` —— 5/23 个有
- `FluxResolutionNode` —— 5/23 个有
- `XB_UNetNameBroadcaster` —— 5/23 个有
- `EnhancedLoadDiffusionModel` —— 2/23 个有
- `LatentUpscaleBy` —— 2/23 个有
- `JjkText` —— 1/23 个有
- `Text Concatenate` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1664 | 23 | 78% |
| 高度 | 1024 | 512 - 1920 | 23 | 72% |
| 采样步数 | 7 | 4 - 30 | 18 | 26% |
| Prompt 约束强度(CFG) | 1 | 1 - 30 | 23 | 0% |
| 采样算法 | euler | - | 23 | 78% |
| 调度器 | simple | - | 23 | 78% |
| 重绘幅度 | 1 | 1 - 4.5 | 23 | 35% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1664，23 个样本
- 高度 中位数 1024，观测区间 512 - 1920，23 个样本
- 采样步数 中位数 7，观测区间 4 - 30，18 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 30，23 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，23 个样本，一致性 78%
- 调度器 最常用 simple，23 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 4.5，23 个样本，取值分散，一致性仅 35%
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 4.5，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 高发问题（15/23 个样本）：Steps较低可能导致细节不足
