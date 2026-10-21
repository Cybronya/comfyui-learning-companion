---
name: text_to_image_lora_sampler_clip_160
type: Text To Image
frequency: 7
level: strong
coverage: 0.866714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2102588489098424321.json, 图片生成/文生图/Anima文生图 高质量图片生成处理工具_2100652917832376321.json, 图片生成/文生图/Anima文生图｜动漫图像生成一键直出创作_2090189762333335553.json, 图片生成/文生图/Anima生图｜文生图动漫风格_2090465768436752386.json, 图片生成/文生图/G Image2低价版文生图工作流，低成本文本到图像生成方案_2106128186449944577.json, 图片生成/文生图/G2 文生图低价版｜省币跑图更划算的文生图选择_2096890572521951233.json, 图片生成/文生图/Qwen Image 2.1 PE文生图优化版｜出图质量再打磨｜细节党放心冲_2102587044131336194.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_160

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2102588489098424321.json、图片生成/文生图/Anima文生图 高质量图片生成处理工具_2100652917832376321.json、图片生成/文生图/Anima文生图｜动漫图像生成一键直出创作_2090189762333335553.json、图片生成/文生图/Anima生图｜文生图动漫风格_2090465768436752386.json、图片生成/文生图/G Image2低价版文生图工作流，低成本文本到图像生成方案_2106128186449944577.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 6/7 个有
- `ClownsharKSampler_Beta` —— 3/7 个有
- `LoraLoader` —— 3/7 个有
- `PreviewAny` —— 2/7 个有
- `QwenPECanvasT8` —— 2/7 个有
- `QwenPERewriteT8` —— 2/7 个有
- `RH_RhartImageG2TextToImage` —— 2/7 个有
- `QwenImage21Cache` —— 1/7 个有
- `SaveText` —— 1/7 个有
- `TextEncodeQwenImage21` —— 1/7 个有
- `TextInput` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
