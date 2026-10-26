---
name: text_to_image_sampler_clip_unet_230
type: Text To Image
frequency: 2
level: weak
coverage: 0.8515
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingSD3, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Y1-Image_wan2_2_14B_t2v_1960231389213962242.json, 图片生成/文生图/电商生成真实人物图片 MagicWanImage_1991348310250467330.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_230

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Y1-Image_wan2_2_14B_t2v_1960231389213962242.json、图片生成/文生图/电商生成真实人物图片 MagicWanImage_1991348310250467330.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingSD3`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `SDXL Resolutions (JPS)` —— 1/2 个有
- `SeargePromptCombiner` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1072 | - | 2 | 72% |
| 高度 | 896 | - | 2 | 86% |
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.6 | - | 2 | 33% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1072，样本不足，未给区间，2 个样本
- 高度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
