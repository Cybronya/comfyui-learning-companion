---
name: text_to_image_lora_sampler_clip_137
type: Text To Image
frequency: 11
level: weak
coverage: 0.894909
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima Aesthetic 1.1｜1.5倍放大_2078374859184365569.json, 图片生成/文生图/Anima Aesthetic 1.1｜三阶高质量渲染_2078374835163582465.json, 图片生成/文生图/Anima+Aesthetic+1.1｜DMDX+四步极速版_2078701772113272834.json, 图片生成/文生图/Anima+Aesthetic+1.1｜文生图_2078701764664184833.json, 图片生成/文生图/Anima+Aesthetic+1.1｜文生图_2079573127385927682.json, 图片生成/文生图/Kang文生图Qwen_image_4步_1957421621072031746.json, 图片生成/文生图/Qwen-Image-2512 + LoRA 文生图_2091487545254301698.json, 图片生成/文生图/Qwen2.1文生图（写实风格）_2104831851583066113.json, 图片生成/文生图/Z-image + LoRA 文生图工作流_2058875529981415425.json, 图片生成/文生图/Z-image 文生图工作流（含加速器）_2046950465908252673.json, 图片生成/文生图/qwen image  文生图 超细致彩色铅笔_2079613769243774977.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_137

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Anima Aesthetic 1.1｜1.5倍放大_2078374859184365569.json、图片生成/文生图/Anima Aesthetic 1.1｜三阶高质量渲染_2078374835163582465.json、图片生成/文生图/Anima+Aesthetic+1.1｜DMDX+四步极速版_2078701772113272834.json、图片生成/文生图/Anima+Aesthetic+1.1｜文生图_2078701764664184833.json、图片生成/文生图/Anima+Aesthetic+1.1｜文生图_2079573127385927682.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 10/11 个有
- `UNETLoader` —— 9/11 个有
- `ModelSamplingAuraFlow` —— 6/11 个有
- `ClownsharKSampler_Beta` —— 5/11 个有
- `FluxResolutionNode` —— 5/11 个有
- `XB_UNetNameBroadcaster` —— 5/11 个有
- `EnhancedLoadDiffusionModel` —— 2/11 个有
- `LatentUpscaleBy` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1536 | 11 | 79% |
| 高度 | 1024 | 512 - 1920 | 11 | 64% |
| 采样步数 | 8 | 4 - 25 | 6 | 36% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 30 | 11 | 0% |
| 采样算法 | euler | - | 11 | 55% |
| 调度器 | simple | - | 11 | 45% |
| 重绘幅度 | 1 | 1 - 4.5 | 11 | 34% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1536，11 个样本
- 高度 中位数 1024，观测区间 512 - 1920，11 个样本
- 采样步数 中位数 8，观测区间 4 - 25，6 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 30，11 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，11 个样本，一致性 55%
- 调度器 最常用 simple，11 个样本，一致性 45%
- 重绘幅度 中位数 1，观测区间 1 - 4.5，11 个样本，取值分散，一致性仅 34%
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 4.5，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
